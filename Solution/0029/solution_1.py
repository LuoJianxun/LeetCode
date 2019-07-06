class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if abs(dividend) == abs(divisor):
            return -1 if dividend + divisor == 0 else 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            symbol = '-'
        else:
            symbol = '+'
        result = 0
        tmp = int(symbol + '1')
        while True:
            temp = dividend
            if symbol == '-':
                dividend += divisor
            elif symbol == '+':
                dividend -= divisor
            if (temp > 0 and dividend < 0) or (temp < 0 and dividend > 0):
                break
            result += tmp
        return result

if __name__ == '__main__':
    dividend = -2147483648
    divisor = 1
    result = Solution().divide(dividend, divisor)
    print(result)

# 超时