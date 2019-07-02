class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        while True:
            n = nums[i]
            if nums.count(n) > 1:
                nums.remove(n)
            else:
                i += 1
            if n == max(nums) and nums.count(n) == 1:
                break
        return len(nums)

if __name__ == '__main__':
    nums = []
    result = Solution().removeDuplicates(nums)
    print(result)