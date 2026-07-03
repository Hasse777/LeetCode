class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                if nums[j] == target:
                    count += 1
                if count > (j - i + 1) / 2:
                    result += 1
        return result
