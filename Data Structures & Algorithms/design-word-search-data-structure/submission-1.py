class TrieNode():

    def __init__(self):
        self.neighbours = {}
        self.EOW = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch in curr.neighbours:
                curr = curr.neighbours[ch]
            else:
                curr.neighbours[ch] = TrieNode()
                curr = curr.neighbours[ch]
        curr.EOW = True

    def search(self, word: str) -> bool:
        # dfs on word, branching if .

        def dfs(node, i):
            if i == len(word):
                return node.EOW

            ch = word[i]
            if ch != '.': 
                if ch in node.neighbours:
                    return dfs(node.neighbours[ch], i+1)
                else:
                    return False
            else:
                for neigh in node.neighbours:
                    found = dfs(node.neighbours[neigh], i+1)
                    if found: 
                        return True
                return False
        
        return dfs(self.root, 0)

                    
            

        
        
                
                
