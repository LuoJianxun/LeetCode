class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = sum(nums[:3])
        temp = abs(target - result)
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                diff = abs(target - res)
                if diff < temp:
                    temp = diff
                    result = res
                if res == target:
                    break
                elif res < target:
                    left += 1
                else:
                    right -= 1

        return result

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    result = Solution().threeSumClosest(nums, target)
    print(result)

