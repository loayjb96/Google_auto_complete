import os
import re
import pickle as pkl
from trie import Trie
from config import Path,pure_dilemeters


def fill_trie():
    suf_trie = Trie()
    regex = re.compile(pure_dilemeters)
    for data, file_name in read_files():
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
    with open('trie_db.pkl', 'wb') as f:
        pkl.dump(fill_trie(), f)


def read_files():
    for subdir, dirs, files in os.walk(Path):
        for file_name in files:
            with open(os.path.join(subdir, file_name), encoding="utf8") as f:
                data = f.read()

                yield data, file_name


def all_suffixes(s):
    return [s[-i:] for i in range(1, len(s) + 1)]


def all_complete_suffixes(s):
    list_suffix = []
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            list_suffix.append(s[i + 1:])

    list_suffix.append(s)
    return list_suffix


insert_trie_to_pkl()


