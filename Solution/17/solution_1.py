class Solution:
    def letterCombinations(self, digits: str):
        num_dict = {'2': ['a', 'b', 'c'], 
                    '3': ['d', 'e', 'f'], 
                    '4': ['g', 'h', 'i'], 
                    '5': ['j', 'k', 'l'], 
                    '6': ['m', 'n', 'o'], 
                    '7': ['p', 'q', 'r', 's'], 
                    '8': ['t', 'u', 'v'], 
                    '9': ['w', 'x', 'y', 'z']}
        if len(digits) == 1:
            result = num_dict.get(digits)
        else:
            result = []
        for i in range(len(digits)-1):
            if len(result) == 0:
                result = [x + y for x in num_dict[digits[i]] for y in num_dict[digits[i+1]]]
            else:
                result = [x + y for x in result for y in num_dict[digits[i+1]]]
        return result

if __name__ == '__main__':
    digits = '23'
    result = Solution().letterCombinations(digits)
    print(result)