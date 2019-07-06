class Solution:
    def isHappy(self, n: int) -> bool:
        num_pow = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        l = []
        while n > 0:
            num = [num_pow[int(i)] for i in str(n)]
            n = sum(num)
            if n in l:
                break
            else:
                l.append(n)
        return n == 1

if __name__ == '__main__':
    n = 19
    result = Solution().isHappy(n)
    print(result)

# 注：
# 不是快乐数的数称为不快乐数（unhappy number）
# 所有不快乐数的数位平方和计算
# 最後都会进入 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 的循环中