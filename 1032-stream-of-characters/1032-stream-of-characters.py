from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.stream = []

        # Insert every word in reverse
        for word in words:
            node = self.root

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.is_word = True

        # Longest word length
        self.max_len = max(len(word) for word in words)

    def query(self, letter: str) -> bool:
        self.stream.append(letter)

        node = self.root

        # Check from newest character backwards
        for i in range(len(self.stream) - 1, 
                       max(-1, len(self.stream) - self.max_len - 1), 
                       -1):

            ch = self.stream[i]

            if ch not in node.children:
                return False

            node = node.children[ch]

            if node.is_word:
                return True

        return False