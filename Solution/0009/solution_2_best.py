class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        if s[0] == '-':
            return False
        if s == s[::-1]:
            return True
        else:
            return False