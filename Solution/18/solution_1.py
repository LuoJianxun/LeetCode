class Solution:
    def fourSum(self, nums, target: int):
        result = []
        if len(nums) < 4:
            return result
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    for l in range(k+1, length):
                        if nums[i] + nums[j] +nums[k] + nums[l] == target:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            if temp not in result:
                                result.append(temp)
        return result

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = Solution().fourSum(nums, target)
    print(result)

# 超时