class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if min(nums) >= 0:
            return sum(nums)
        temp, result = 0, nums[0]
        for num in nums:
            temp = max(temp + num, num)
            result = max(result, temp)
            print('temp:%s, result:%s' % (temp, result))
        return result
        
        
if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = Solution().maxSubArray(nums)
    print(result)