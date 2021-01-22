from trie import Trie
import pickle as pkl


class TrieFactory:
    def __init__(self):
        self.trie = Trie()

    def load_to_trie_from_pkl(self):
        with open('trie_db.pkl', 'rb') as f:
            self.trie = pkl.load(f)