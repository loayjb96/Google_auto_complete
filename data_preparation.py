import os
import re
import pickle as pkl
from trie import Trie
from config import Path, pure_dilemeters


def fill_trie():
    """
    this function creates the trie suffix tree and ,calls the function that creates all the
    suffixes
    :return:
    the function returns the trie tree.
    """
    suf_trie = Trie()
    regex = re.compile(pure_dilemeters)
    for data, file_name in read_files():  # calls the generator function to minimize memory use
        filter_set = set(data.split('\n'))
        for line in filter_set:
            if line == '' or line == ' ':
                continue
            unfiltered_line = line
            line = regex.sub("", line).strip(' ').lower()
            suffix_line = all_complete_suffixes(line)
            for sentence in suffix_line:
                suf_trie.insert(sentence, unfiltered_line)
    return suf_trie


def insert_trie_to_pkl():
    """
    this function saves the trie tree to the disk in a pickle file format.
    :return:
    None
    """
    with open('trie_db.pkl', 'wb') as f:
        pkl.dump(fill_trie(), f)


def read_files():
    """
    A generator method reads from file and yields its output to the caller method
    :return:
    yields the data and the file name
    """
    for subdir, dirs, files in os.walk(Path):
        for file_name in files:
            with open(os.path.join(subdir, file_name), encoding="utf8") as f:
                data = f.read()

                yield data, file_name


def all_complete_suffixes(s):
    """
    this function returns the suffixes of a given string.
    :param s:
    s is the string
    :return:
    returns a list of suffixes of a given string
    """
    list_suffix = []
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            list_suffix.append(s[i + 1:])

    list_suffix.append(s)
    return list_suffix


insert_trie_to_pkl()
