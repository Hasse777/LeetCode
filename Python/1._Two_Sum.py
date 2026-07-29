class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = dict()
        for i, num in enumerate(nums):
            j = target - num
            if j in result:
                return [result[j], i]
            result[num] = i
        return []
