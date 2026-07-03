# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        result = list()
        if n == 0:
            return result
        return self.recursive(1, n)

    def recursive(self, l, r):
        if l > r:
            return [None]
        result = list()
        for root in range(l, r + 1):
            l_trees = self.recursive(l, root - 1)
            r_trees = self.recursive(root + 1, r)
            for l_tree in l_trees:
                for r_tree in r_trees:
                    root_node = TreeNode(root)
                    root_node.left = l_tree
                    root_node.right = r_tree
                    result.append(root_node)
        return result
