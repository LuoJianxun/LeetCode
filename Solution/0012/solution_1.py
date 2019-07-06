class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict_0 = {}
        dict_1 = {'0':'', '1':'I', '2':'II', '3':'III', '4':'IV', '5':'V', '6':'VI', '7':'VII', '8':'VIII', '9':'IX'}
        dict_10 = {'0':'', '1':'X', '2':'XX', '3':'XXX', '4':'XL', '5':'L', '6':'LX', '7':'LXX', '8':'LXXX', '9':'XC'}
        dict_100 = {'0':'', '1':'C', '2':'CC', '3':'CCC', '4':'CD', '5':'D', '6':'DC', '7':'DCC', '8':'DCCC', '9':'CM'}
        dict_1000 = {'0':'', '1':'M', '2':'MM', '3':'MMM'}
        tuple_num = (dict_0, dict_1, dict_10, dict_100, dict_1000)
        s = str(num)
        l = len(s)
        result = ''
        for i in range(l):
            result += tuple_num[l-i][s[i]]
        return result