class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if abs(dividend) == abs(divisor):
            return -1 if dividend + divisor == 0 else 1
        d1 = str(dividend)
        d2 = str(divisor)
        result = 0
        return result

if __name__ == '__main__':
    dividend = -2147483648
    divisor = 1
    result = Solution().divide(dividend, divisor)
    print(result)

# 模拟手写除法的步骤