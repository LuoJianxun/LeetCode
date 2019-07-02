class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = [i for i in range(len(nums)) if (target - nums[i]) in (nums[:i] + nums[i+1:])]
        return index
