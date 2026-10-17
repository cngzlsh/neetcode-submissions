class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sh, th = {}, {}
        for n in s:
            if n not in sh:
                sh[n] = 1
            else:
                sh[n] += 1
        for n in t:
            if n not in th:
                th[n] = 1
            else:
                th[n] += 1
        
        return True if sh == th else False