class Solution:
    def generateParenthesis(self, n: int):
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                    ans.append(S)
                    return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)
        ans = []
        backtrack()
        return ans

if __name__ == '__main__':
    n = 3
    result = Solution().generateParenthesis(n)
    print(result)
    a = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    print(len(a))

# 大佬的代码，递归实现