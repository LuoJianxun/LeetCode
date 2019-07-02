class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        i = 0
        while i < len(nums):
            x = nums[i]
            temp = nums[i+1:]
            left = 0
            right = len(temp) - 1
            while left < right:
                y = temp[left]
                z = temp[right]
                if x + y + z == 0:
                    tmp = [x, y, z]
                    if not tmp in result:
                        result.append(tmp)
                    left += 1
                elif x + y + z < 0:
                    left +=1
                elif x + y + z > 0:
                    right -= 1
            i += 1
        return result

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    result = Solution().threeSum(nums)
    print(result)