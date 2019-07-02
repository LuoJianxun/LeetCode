class Solution:
    def removeElement(self, nums, val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    result = Solution().removeElement(nums, val)
    print(result)