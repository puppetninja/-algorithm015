class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.chars = {}
        self.end_of_word = '#'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_chars = self.chars
        for c in list(word):
            if c not in curr_chars:
                curr_chars[c] = {}
            curr_chars = curr_chars[c]

        curr_chars[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr_chars = self.chars
        for c in list(word):
            if c not in curr_chars:
                return False
            curr_chars = curr_chars[c]
        return self.end_of_word in curr_chars

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr_chars = self.chars
        for c in list(prefix):
            if c not in curr_chars:
                return False
            curr_chars = curr_chars[c]
        return True
