class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        # bfs from source
        switch = 1
        stack = [beginWord]
        visited = set(beginWord)
        while stack:
            new_stack = []
            switch += 1
            for _ in range(len(stack)):
                w = stack.pop()
                for c in wordList:
                    if sum([w[i] == c[i] for i in range(len(w))]) == len(w) -1 and c not in visited:
                        if c == endWord: 
                            return switch
                        new_stack.append(c)
                        visited.add(c)
            stack = new_stack

        return 0