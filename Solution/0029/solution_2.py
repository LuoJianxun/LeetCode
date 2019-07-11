class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        symbol = self.get_symbol(dividend, divisor)
        rest = abs(dividend)
        div = abs(divisor)
        res = ''
        begin = False
        if rest == div:
            return symbol
        if rest < div:
            return 0
        while rest > div:
            temp, rest, flag = self.get_rest(rest, div)
            digit, diff = self.cal(temp, div)
            if flag and begin:
                res = res + '0' + str(digit)
            else:
                res = res + str(digit)
            if diff == 0:
                begin = True
            else:
                begin = False
            if rest == -1:
                break
            rest = int(str(diff) + str(rest))
            if rest < div:
                res = res + '0'

        if symbol == 1:
            return int(res) if int(res) < 2147483648 else 2147483647
        else:
            return -int(res) if -int(res) >= -2147483648 else 2147483647

    def get_symbol(self, dividend, divisor):
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return 1
        elif (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            return -1

    def get_rest(self, dividend, divisor):
        str1 = str(dividend)
        length = len(str(divisor))
        temp = int(str1[:length])
        if temp < divisor:
            temp = int(str1[:length + 1])
            rest = int(str1[length + 1:]) if str1[length + 1:] else -1
            flag = True
        else:
            rest = int(str1[length:]) if str1[length:] else -1
            flag = False

        return temp, rest, flag

    def cal(self, temp, divisor):
        i = 0
        while True:
            diff = temp - divisor
            # print('diff:', diff)
            i += 1
            if diff < divisor:
                break
            else:
                temp = diff

        return i, diff


if __name__ == '__main__':
    a = -1730782680
    b = -159474903
    c = Solution().divide(a, b)
    print(c)
