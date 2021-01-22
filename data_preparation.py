import os
import re
import pickle as pkl
from trie import Trie
from config import Path

suffix_trie = Trie()


def fill_trie():
    global suffix_trie
    regex = re.compile("[^a-zA-Z\s]")
    for data, file_name in read_files():

        filter_set = set(data.split('\n'))
        for line in filter_set:
            if line == '' or line == ' ':
                continue
            unfiltered_line = line
            line = regex.sub("", line).strip(' ').lower()

            suffix_line = all_complete_suffixes(line)
            for sentence in suffix_line:
                suffix_trie.insert(sentence, unfiltered_line)


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


fill_trie()

print(suffix_trie.query('HoW'))
