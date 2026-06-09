class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        size = len(matrix)
        for i in range(size):
            for j in range(i, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(size):
            for j in range(size // 2):
                matrix[i][j], matrix[i][size - 1 - j] = matrix[i][size - 1 - j], matrix[i][j]
        return matrix
