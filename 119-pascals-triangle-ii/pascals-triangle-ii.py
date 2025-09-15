class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] * (rowIndex + 1)
        if rowIndex <= 1:
            return row
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        return row