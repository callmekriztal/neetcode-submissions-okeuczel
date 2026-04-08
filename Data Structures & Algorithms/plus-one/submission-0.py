class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        new_digit = []
        for i in digits:
            num = num*10 + i

        num = str(num + 1)

        for i in num:
            new_digit.append(int(i))

        return new_digit