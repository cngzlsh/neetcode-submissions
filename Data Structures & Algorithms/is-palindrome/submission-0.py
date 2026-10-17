class Solution:
    def isPalindrome(self, s: str) -> bool:
        chs ='1234567890qwertyuiopasdfghjklzxcvbnm'
        news = ''
        for i in range(len(s)): 
            if s[i].lower() in chs:
                news += s[i].lower()
        
        l, r = 0, len(news) -1
        while l < r:
            if news[l] != news[r]: return False
            l += 1
            r -= 1
        
        return True