class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        if re.fullmatch(p,s):
            return True
        else:
            return False
        