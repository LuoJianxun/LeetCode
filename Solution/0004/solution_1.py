class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        mid = l // 2
        re = l % 2
        if re == 0:
            result = (nums[mid - 1] + nums[mid]) / 2
        else:
            result = float(nums[mid])
        return result