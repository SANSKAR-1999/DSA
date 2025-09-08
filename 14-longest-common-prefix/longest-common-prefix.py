class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Handle edge cases
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        # Sort the array of strings
        strs.sort()
        
        # Compare the first and last strings after sorting
        first = strs[0]
        last = strs[-1]
        prefix = ""
        
        # Find common prefix between first and last strings
        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                prefix += first[i]
            else:
                break
        
        return prefix