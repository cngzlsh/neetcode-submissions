class Node:

    def __init__(self):
        self.children = {}
        self.eow = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        head = self.root
        for ch in word:
            if ch in head.children:
                head = head.children[ch]
            else:
                head.children[ch] = Node()
                head = head.children[ch]
        head.eow = True

    def search(self, word: str) -> bool:
        head = self.root
        for ch in word:
            if ch in head.children:
                head = head.children[ch]
            else:
                return False
        return True if head.eow else False
        

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for ch in prefix:
            if ch in head.children:
                head = head.children[ch]
            else:
                return False
        return True
        