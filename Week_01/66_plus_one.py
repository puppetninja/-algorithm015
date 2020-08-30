class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Set overflow boolean, last digit add 1 as if there is overflow
        of = True

        # Iterate over reversed digit list
        for i in reversed(range(len(digits))):
            if of:
                if digits[i] + 1 == 10:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    of = False

            if i == 0 and of:
                digits = [1] + digits

        return digits
