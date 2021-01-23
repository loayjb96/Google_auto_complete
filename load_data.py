from trie import Trie
import pickle as pkl


class TrieFactory:
    """
    class the constructs the trie tree (abstract factory method)
    """
    def __init__(self):
        self.trie = Trie()

    def load_to_trie_from_pkl(self):
        """
        this function loads the saved trie from the pkl file
        :return:
        """
        with open('trie_db.pkl', 'rb') as f:
            self.trie = pkl.load(f)