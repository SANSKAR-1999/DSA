class Solution(object):
    def romanToInt(self, s): 
        # Dictionary mapping Roman numerals to integers
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        prev_value = 0
        
        # Iterate from right to left
        for char in reversed(s):
            current_value = roman_values[char]
            # If current value is greater than or equal to previous, add it
            if current_value >= prev_value:
                result += current_value
            # If current value is less than previous, subtract it
            else:
                result -= current_value
            prev_value = current_value
        
        return result