class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else (num - 1) % 9 + 1

if __name__ == '__main__':
    num = 0
    result = Solution().addDigits(num)
    print(result)