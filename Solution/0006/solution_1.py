class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        group = 0
        i = 0
        result_list = [''] * numRows
        result = ''
        if numRows < 2:
            return s
        while i < len(s):
            if group == 0:
                temp = 0
                reverse = 1
                group = 2 * numRows - 2
            if temp == numRows - 1:
                reverse = -1
            result_list[temp] = result_list[temp] + s[i]
            temp = temp + reverse
            group = group - 1
            i = i + 1
        for i in range(len(result_list)):
            result = result + result_list[i]
        return result

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    result = Solution().convert(s, numRows)
    print(result)