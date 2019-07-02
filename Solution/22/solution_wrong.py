class Solution:
    def generateParenthesis(self, n: int):
        str_1 = '(' * n + ')' * n
        result = [str_1]
        for i in range(1, n):
            for j in range(n, n*2-1):
                for k in range(int(n/2)):
                    if i+k >= n:
                       break
                    print('i+k:', i+k, 'k:', k)
                    temp = str_1[0:i+k] + ')'*(k+1) + str_1[i+k+k+1:j] + '('*(k+1) + str_1[j+k+1:]
                    print('temp:', temp)
                    if temp not in result and len(temp) == n*2:
                        result.append(temp)
        print(len(result))
        return result

if __name__ == '__main__':
    n = 4
    result = Solution().generateParenthesis(n)
    print(result)