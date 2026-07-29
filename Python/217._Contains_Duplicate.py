class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        result = dict()
        for char in s:
            result[char] = result.get(char, 0) + 1
        for char in t:
            result[char] = result.get(char, 0) - 1
            if result[char] < 0:
                return False
        return True
