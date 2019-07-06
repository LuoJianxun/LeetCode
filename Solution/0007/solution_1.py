class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            sign = 1
        else:
            sign = -1
        x = sign * x
        s = str(x)
        s = s[::-1]
        result = sign * int(s)
        if pow(-2, 31) < result < (pow(2, 31) - 1):
            return result
        else:
            return 0