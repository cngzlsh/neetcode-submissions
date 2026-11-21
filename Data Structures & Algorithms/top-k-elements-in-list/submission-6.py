class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]   # buckets[c] = numbers with count c
        for num, cnt in counter.items():
            buckets[cnt].append(num)

        res = []
        for cnt in range(len(nums), 0, -1):
            for num in buckets[cnt]:
                res.append(num)
                if len(res) == k:
                    return res
        return res