class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        triangle = [[1]]
        for i in range(1, numRows):
            prev_row = triangle[-1]
            new_row = [1]  # Indented: Starts each new row
            for j in range(1, i):  # Indented: Builds middles for this row
                new_row.append(prev_row[j-1] + prev_row[j])
            new_row.append(1)  # Indented: Ends each new row
            triangle.append(new_row)  # Indented: Adds this row to triangle
        return triangle

