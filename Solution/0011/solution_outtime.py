class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                temp = min(height[i], height[j]) * (j - i)
                if temp > result:
                    result = temp
        return result