class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                sub_str = s[j:j+i]
                if sub_str == sub_str[::-1]:
                    return sub_str