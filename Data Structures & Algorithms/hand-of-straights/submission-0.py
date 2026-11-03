class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        counter = Counter(hand)
        while counter:
            m = min(counter.keys())
            for i in range(groupSize):
                if m + i not in counter:
                    return False
                else:
                    counter[m+i] -= 1
                    if not counter[m+i]:
                        del counter[m+i]
        
        return True