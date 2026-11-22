class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for ch in s:
            if ch not in counter:
                counter[ch] = 1
            else:
                counter[ch] += 1
                
        
        for ch in t:
            if ch in counter:
                if counter[ch] > 1:
                    counter[ch] -= 1
                
                elif counter[ch] == 1:
                    del counter[ch]
                
            else:
                return False
        
        return True if counter == {} else False