class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        # Dictionary mapping digits to letters
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        # Initialize result with an empty string
        result = [""]
        
        # Process each digit
        for digit in digits:
            # Get letters for the current digit
            letters = phone_map[digit]
            # Create new combinations by appending each letter to existing combinations
            new_result = []
            for prefix in result:
                for letter in letters:
                    new_result.append(prefix + letter)
            # Update result with new combinations
            result = new_result
        
        return result