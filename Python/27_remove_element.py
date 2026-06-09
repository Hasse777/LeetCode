class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                if nums[right] != val:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        return left
