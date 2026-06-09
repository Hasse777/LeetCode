class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        cur_min = min(nums[0], nums[1])
        cur_max = max(nums[0], nums[1])
        result = (cur_max - cur_min) * k
        for i in range(2, len(nums)):
            if nums[i] < cur_min:
                cur_min = nums[i]
            elif nums[i] > cur_max:
                cur_max = nums[i]
            result = max(result, (cur_max - cur_min) * k)

        return result
