class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        best = [0, 0, 0]
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:   # usable
                best = [max(best[0], a), max(best[1], b), max(best[2], c)]
        return best == target