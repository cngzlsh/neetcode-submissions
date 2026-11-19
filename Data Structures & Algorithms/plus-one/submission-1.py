class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for d in reversed(digits):
            carry, digit = divmod(d + carry, 10)
            res.append(digit)
        if carry:
            res.append(1)
        return res[::-1]