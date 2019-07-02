class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        result = strs[0]
        for i in range(len(strs) - 1):
            result = self.compare(result, strs[i + 1])
            if result == '':
                break
        return result
        
        
    def compare(self, s1, s2):
        s = ''
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                s = s + s1[i]
            else:
                break
        return s