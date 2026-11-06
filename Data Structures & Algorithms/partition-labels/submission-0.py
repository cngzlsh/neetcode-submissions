class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # count when each label appeared first and last in string
        counter = {}
        for i, n in enumerate(s):
                counter[n] = i
        
        res = []
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, counter[ch])               # farthest this piece must extend
            if i == end:                           # nothing in the piece appears later
                res.append(end - start + 1)
                start = i + 1
        return res
