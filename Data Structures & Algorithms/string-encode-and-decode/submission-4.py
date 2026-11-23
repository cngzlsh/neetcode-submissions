class Solution:

    def encode(self, strs: List[str]) -> str:
        lens = []
        for s in strs:
            lens.append(str(len(s)) + '#')
        
        return "".join(lens) + "$" + "".join(strs)

    def decode(self, s: str) -> List[str]:

        lens, strs = s.split("$", 1)  

        lens = lens.split("#")[:-1]
        res = []

        c = 0
        for l in lens:
            res.append(strs[c:c + int(l)])
            c += int(l)
        
        return res
        

        
