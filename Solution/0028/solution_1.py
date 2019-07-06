class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if needle in haystack:
            group = haystack.split(needle)
            return len(group[0])
        else:
            return -1

if __name__ == '__main__':
    haystack = 'aaaaa'
    needle = 'bba'
    result = Solution().strStr(haystack, needle)
    print(result)