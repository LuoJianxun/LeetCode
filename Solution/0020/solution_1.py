class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        left = []
        for e in s:
            if e in ('(', '[', '{'):
                left.append(e)
            elif e in (')', ']', '}'):
                try:
                    tmp = left.pop()
                    temp = tmp + e
                    if temp not in ('()', '[]', '{}'):
                        return False
                except:
                    return False
        if len(left) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    s = "["
    result = Solution().isValid(s)
    print(result)
