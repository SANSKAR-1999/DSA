class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return 0
        r = len(digits)
        for i in range(r - 1, -1, -1):
            if digits[i] < 9:
            # If the current digit is less than 9, increment it and return
                digits[i] += 1
                return digits
            else:
            # If the digit is 9, set it to 0 and continue to the next digit
                digits[i] = 0
    
    # If we reach here, all digits were 9, so we need to add a leading 1
        return [1] + [0] * r    