class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for char in s:
            if char.isalpha():
                result += char
            elif char == '*' and result:
                result = result[:-1]
            elif char == '#':
                result = result + result
            elif char == '%':
                result = result[::-1]
        return result
