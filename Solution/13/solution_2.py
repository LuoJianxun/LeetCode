# close to solution1

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        IV_num, s = self.num_count(s, 'IV')
        IX_num, s = self.num_count(s, 'IX')
        XL_num, s = self.num_count(s, 'XL')
        XC_num, s = self.num_count(s, 'XC')
        CD_num, s = self.num_count(s, 'CD')
        CM_num, s = self.num_count(s, 'CM')
        I_num, s = self.num_count(s, 'I')
        V_num, s = self.num_count(s, 'V')
        X_num, s = self.num_count(s, 'X')
        L_num, s = self.num_count(s, 'L')
        C_num, s = self.num_count(s, 'C')
        D_num, s = self.num_count(s, 'D')
        M_num, s = self.num_count(s, 'M')
        
        result = 4 * IV_num + 9 * IX_num + 40 * XL_num + 90 * XC_num + 400 * CD_num + 900 * CM_num + I_num + 5 * V_num + 10 * X_num + 50 * L_num + 100 * C_num + 500 * D_num + 1000 * M_num
        return result

       
    def num_count(self, s, num):
        cnt = 0
        if num in s:
            cnt = s.count(num)
            s = ''.join(s.split(num))
        return cnt, s
        