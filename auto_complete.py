from dataclasses import dataclass
import re
from config import pure_dilemeters
from load_data import TrieFactory

from command_line_view import print_suggestions, print_start_system, print_enter_text


@dataclass
class AutoCompleteData:
    completed_sentence: str
    offset: int
    score: int

    def get_sentence(self):
        return self.completed_sentence

    def get_score(self):
        return self.score


def get_list_from_trie(prefix, k, l_completed, default_score):
    completed = trie_db.trie.query(prefix)
    for sentence in completed:
        if k == 0:
            break
        sentence_s = sentence.lower()
        offset = sentence_s.index(prefix)
        l_completed.append(AutoCompleteData(sentence, offset, default_score))
        k -= 1
    return k


def get_best_k_completions(prefix: str, k=5):
    global trie_db
    regex = re.compile(pure_dilemeters)
    prefix = regex.sub("", prefix)
    prefix = prefix.lower()
    default_score = len(prefix)
    l_completed = []
    k = get_list_from_trie(prefix, k, l_completed, default_score * 2)
    temp_set = dict()
    l_completed, k = get_deleted_replaced_added_character(prefix, k, l_completed, replace_index, temp_set)

    l_completed, k = get_deleted_replaced_added_character(prefix, k, l_completed, add_index, temp_set)

    l_completed, k = get_deleted_replaced_added_character(prefix, k, l_completed, delete_index, temp_set)

    return sorted(l_completed, key=lambda x: x.score, reverse=True)


def get_deleted_replaced_added_character(val, k, l_completed, func, temp_set):
    default_score = len(val)

    for i in range(len(val) - 1, -1, -1):
        for new_val, default_score in func(val, i, default_score):
            if k != 0:
                k = get_list_from_trie(new_val, k, l_completed, default_score)
                default_score = len(val)
            if k == 0:
                break
        if k == 0:
            break

    for item in l_completed:
        if not temp_set.get(item.get_sentence()):
            temp_set[item.get_sentence()] = item
    l_completed = []
    for val in temp_set.values():
        l_completed.append(val)
    return l_completed , k


def replace_index(string, index, old_score):
    list_count = [5, 4, 3, 2, 1]
    before_index = string[:index]
    after_index = string[index + 1:]
    letter = string[index]
    for i in range(ord('a'), ord('z') + 1):
        old_score = len(string)
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
def add_index(string, index, default_score):
    list_count = [10, 8, 6, 4]
    before_index = string[:index + 1]
    after_index = string[index + 1:]
    for i in range(ord('a'), ord('z') + 1):
        default_score = len(string)
        new_string = before_index + chr(i) + after_index
        default_score -= 1
        default_score *= 2
        if index <= 3:
            default_score -= list_count[index]
        else:
            default_score -= 2
        yield new_string, default_score


def delete_index(string, index, default_score):
    list_count = [10, 8, 6, 4]
    before_index = string[:index]
    after_index = string[index + 1:]
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
