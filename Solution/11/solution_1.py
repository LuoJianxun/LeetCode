class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        l = 0
        r = len(height) - 1
        result = 0
        while l < r:
            h = min(height[l], height[r])
            maxArea = h * (r - l)
            result = max(result, maxArea)
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return result