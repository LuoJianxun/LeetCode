class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = set(s)
        word_len = len(word)
        s_len = len(s)
        if word_len == s_len:
            return s_len
        else:
            for i in range(word_len):
                for j in range(s_len - word_len):
                    substr = s[j:j+i]
                    temp = set(substr)
                    if len(temp) == len(substr):
                        return len(substr)
                
        