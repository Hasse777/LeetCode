class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = dict()

        for word in strs:
            key = ''.join(sorted(word))
            groups.setdefault(key, []).append(word)

        return list(groups.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
