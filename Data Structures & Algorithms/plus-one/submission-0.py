class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits) - 1:
                carry = (digits[i] + 1) >= 10
                digits[i] = (digits[i] + 1) % 10
            else:
                if carry:
                    carry = (digits[i] + 1) >= 10
                    digits[i] = (digits[i] + 1) % 10
        if carry: return [1] + digits
        else:
            return digits