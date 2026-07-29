import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = dict()
        for num in nums:
            d[num] = d.get(num, 0) + 1

        heap = heapq.nlargest(k, d.items(), key=lambda x: x[1])
        return [item[0] for item in heap]
