from dataclasses import dataclass
import re
import json
from load_data import b

@dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int

with open("C:/Users/loay-/PycharmProjects/play_ground/files_name.json") as f:
    files_names = json.load(f)
def get_best_k_completions(prefix: str):
    saved_pre = prefix[:]
    regex = re.compile('[^a-zA-Z\n\s]')
    prefix = regex.sub("", prefix)
    prefix = prefix.lower()
    l_completed = []
    completed = b.trie.query(prefix)
    i = 0
    for sentence in completed:
        if i == 5:
            break

        sentence_s = sentence[:]
        sentence_s = sentence_s.lower()
        try:
            index = sentence_s.index(saved_pre)
        except ValueError:
            break

        for file in files_names:
            if file.get(sentence.strip("\n")):
                l_completed.append(AutoCompleteData(sentence.strip("\n"), file[sentence.strip("\n")], index, len(prefix)))
                break
        i += 1
    return l_completed