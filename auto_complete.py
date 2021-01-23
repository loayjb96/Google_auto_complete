from dataclasses import dataclass
import re
from config import pure_dilemeters
from load_data import TrieFactory


@dataclass
class AutoCompleteData:
    """
    class to save the relevant information about the sentence
    """
    completed_sentence: str # the sentence the system returns
    offset: int # the index of the users input from the full sentence
    score: int # the score to order the most relevant sentence

    def get_sentence(self):
        return self.completed_sentence

    def get_score(self):
        return self.score


def get_list_from_trie(word, k, l_completed, score):
    """
    this function takes the input of the user then searches the trie for a match to get the completed sentence
    :param word:
    the user's input
    :param k:
        maximum sentences to return
    :param l_completed:
        a list of sentences from the trie
    :param score:
        the score of the user's input
    :return:
    returns how many values left to return
    """
    completed = trie_db.trie.query(word)
    for sentence in completed:
        if k == 0:
            break
        sentence_s = sentence.lower()
        offset = sentence_s.index(word)
        l_completed.append(AutoCompleteData(sentence, offset, score))
        k -= 1
    return k


def get_best_k_completions(word: str, k=5):
    """
    this function returns the best k completions from the trie
    the first step: it searches the trie if there is a match between the user's input
    and the trie if k suggestions fulfilled the function returns them.
    second step : if k didn't hit zero the function searches the trie again, this time the function,
    assumes the user has miss spilled the word , it fixes the word and searches the trie.
    :param word:
        users input
    :param k:
        maximum suggestion to return
    :return:
        returns the sorted list of suggestion based on there score

    """
    global trie_db
    regex = re.compile(pure_dilemeters)
    word = regex.sub("", word)
    word = word.lower()
    default_score = len(word)
    l_completed = []
    k = get_list_from_trie(word, k, l_completed, default_score * 2)
    temp_set = dict()
    l_completed, k = get_deleted_replaced_added_character(word, k, l_completed, replace_index, temp_set)

    l_completed, k = get_deleted_replaced_added_character(word, k, l_completed, add_index, temp_set)

    l_completed, k = get_deleted_replaced_added_character(word, k, l_completed, delete_index, temp_set)

    return sorted(l_completed, key=lambda x: x.score, reverse=True)


def get_deleted_replaced_added_character(word, k, l_completed, func, temp_set):
    """
    this function corrects the miss spelling that the user has entered,
    wether if he forgot a character, replaced the character with another , or extra character
    :param word:
        users input
    :param k:
        maximum suggestion to return
    :param l_completed:
        a list of sentences from the trie
    :param func:
        pointer to function
    :param temp_set:
        a set to filter the repeated words
    :return:
    list of best k suggestions
    """
    default_score = len(word)

    for i in range(len(word) - 1, -1, -1):
        for new_val, default_score in func(word, i, default_score):
            if k != 0:
                k = get_list_from_trie(new_val, k, l_completed, default_score)
                default_score = len(word)
            if k == 0:
                break
        if k == 0:
            break

    for item in l_completed:
        if not temp_set.get(item.get_sentence()):
            temp_set[item.get_sentence()] = item
    l_completed = []
    for word in temp_set.values():
        l_completed.append(word)
    return l_completed, k


def replace_index(word, index, old_score):
    """
    a generator to replace the character of a string at index, and calculates the score based of ,
    what index the misspelling occurred.
    :param word:
        users input
    :param index:
        what index to replace
    :param old_score:
        the old score before the misspelling
    :return:
        yields the new string after replacing the the character at index with another ,
         and the new score
    """
    list_count = [5, 4, 3, 2, 1]
    before_index = word[:index]
    after_index = word[index + 1:]
    letter = word[index]
    for i in range(ord('a'), ord('z') + 1):
        old_score = len(word)
        if chr(i) != letter:
            new_string = before_index + chr(i) + after_index
            old_score -= 1
            old_score *= 2
            if index <= 4:
                old_score -= list_count[index]
            else:
                old_score -= 1

            yield new_string, old_score


# if there is a deleted char from the word
def add_index(word, index, default_score):
    """
    a generator to add a character at index, and calculates the score based of ,
    what index the misspelling occurred.
    :param word:
        users input
    :param index:
        what index to replace
    :param default_score:
        the old score before the misspelling
    :return:
         yields the new string after replacing the the character at index with another ,
         and the new score
    """
    list_count = [10, 8, 6, 4]
    before_index = word[:index + 1]
    after_index = word[index + 1:]
    for i in range(ord('a'), ord('z') + 1):
        default_score = len(word)
        new_string = before_index + chr(i) + after_index
        default_score -= 1
        default_score *= 2
        if index <= 3:
            default_score -= list_count[index]
        else:
            default_score -= 2
        yield new_string, default_score


def delete_index(word, index, default_score):
    """
    a generator to delete extra character of a string at index, and calculates the score based of ,
    what index the misspelling occurred.
    :param word:
        users input
    :param index:
        what index to replace
    :param default_score:
        the old score before the misspelling
    :return:
         yields the new string after replacing the the character at index with another ,
         and the new score
    """
    list_count = [10, 8, 6, 4]
    before_index = word[:index]
    after_index = word[index + 1:]
    new_string = before_index + after_index
    default_score -= 1
    default_score *= 2
    if index <= 3:
        default_score -= list_count[index]
    else:
        default_score -= 2
    yield new_string, default_score


trie_db = TrieFactory()
trie_db.load_to_trie_from_pkl()
