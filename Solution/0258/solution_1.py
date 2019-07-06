class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        while len(num_str) > 1:
            num_list = [int(x) for x in num_str]
            num_str = str(sum(num_list))
        return int(num_str)

if __name__ == '__main__':
    num = 38
    result = Solution().addDigits(num)
    print(result)