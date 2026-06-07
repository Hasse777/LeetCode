# 34. Find First and Last Position of Element in Sorted Array
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]
        if not nums:
            return result

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            right_num = mid
            left_num = mid
            if nums[mid] == target:
                while left_num > 0 and nums[left_num - 1] == target:
                    left_num -= 1
                while right_num < len(nums) - 1 and nums[right_num + 1] == target:
                    right_num += 1
                result = [left_num, right_num]
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
