class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = s.split()[-1]
        last = len(result)
        return last
        