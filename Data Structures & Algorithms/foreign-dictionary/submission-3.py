class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        from collections import defaultdict
        adjL = {c: set() for w in words for c in w}

        for w1, w2 in zip(words, words[1:]):     # adjacent pairs suffice
            m = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:m] == w2[:m]:
                return ""                        # e.g. "abc" before "ab"
            for k in range(m):
                if w1[k] != w2[k]:
                    adjL[w2[k]].add(w1[k])
                    break

        visited, visiting, res = set(), set(), []

        def dfs(ch):
            if ch in visited: return True
            if ch in visiting: return False
            visiting.add(ch)
            for child in adjL[ch]:
                if not dfs(child):
                    return False
            visiting.remove(ch)
            visited.add(ch)
            res.append(ch)
            return True

        for ch in adjL:
            if not dfs(ch):
                return ""
        return ''.join(res)