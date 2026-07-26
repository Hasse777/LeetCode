class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) > len(word2):
            word1, word2 = word2, word1
        n, m = len(word1), len(word2)
        result = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        for x in range(n + 1):
            result[x][0] = x
        for y in range(m + 1):
            result[0][y] = y

        for x in range(1, n + 1):
            for y in range(1, m + 1):
                f1 = result[x - 1][y] + 1
                f2 = result[x][y - 1] + 1
                f3 = result[x - 1][y - 1] + (0 if word1[x - 1] == word2[y - 1] else 1)
                result[x][y] = min(f1, f2, f3)
        return result[n][m]
