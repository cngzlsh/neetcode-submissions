class Node:
    def __init__(self, EoW=False):
        self.neighbours = {}
        self.EoW = EoW

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        head = self.root
        for ch in word:
            if ch in head.neighbours:
                head = head.neighbours[ch]
            else:
                head.neighbours[ch] = Node()
                head = head.neighbours[ch]
        
        head.EoW = True

    def search(self, word: str) -> bool:
        head = self.root
        for ch in word:
            if ch in head.neighbours:
                head = head.neighbours[ch]
            else:
                return False
        return True if head.EoW else False

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for ch in prefix:
            if ch in head.neighbours:
                head = head.neighbours[ch]
            else:
                return False
        return True
        