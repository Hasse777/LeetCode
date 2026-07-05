class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        self.mem = dict()
        return self.recursive(1, n)

    def recursive(self, l, r):
        if l > r:
            return 1

        if (l, r) in self.mem:
            return self.mem[(l, r)]

        result = 0
        for root in range(l, r + 1):
            l_trees = self.recursive(l, root - 1)
            r_trees = self.recursive(root + 1, r)
            result += l_trees * r_trees
        self.mem[(l, r)] = result
        return result
