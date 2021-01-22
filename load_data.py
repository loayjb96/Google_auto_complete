from trie import Trie
import json


class TrieFactory:
    def __init__(self):
        self.trie = Trie()

    def load_to_trie(self):
        with open("C:/Users/loay-/PycharmProjects/play_ground/Compined_Suffixes.json") as file:
            data = json.load(file)
            for item in data:
                name = list(item.keys())[0]
                with open(f"C:/Users/loay-/Desktop/Google_Progect/small/{name}", encoding="utf8") as f:
                    for line in item[name]:
                        index = list(line.keys())[0]
                        try:
                            l = f.readlines()[int(index)]
                        except IndexError:
                            index = 0
                            break

                        for suffix in line[index]:
                            self.trie.insert(suffix, l)


b = TrieFactory()
b.load_to_trie()