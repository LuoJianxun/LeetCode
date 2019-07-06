class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        if 'IV' in s:
            IV_num = s.count('IV')
            s = ''.join(s.split('IV'))
            result += IV_num * 4
        if 'IX' in s:
            IX_num = s.count('IX')
            s = ''.join(s.split('IX'))
            result += IX_num * 9
        if 'XL' in s:
            XL_num = s.count('XL')
            s = ''.join(s.split('XL'))
            result += XL_num * 40
        if 'XC' in s:
            XC_num = s.count('XC')
            s = ''.join(s.split('XC'))
            result += XC_num * 90
        if 'CD' in s:
            CD_num = s.count('CD')
            s = ''.join(s.split('CD'))
            result += CD_num * 400
        if 'CM' in s:
            CM_num = s.count('CM')
            s = ''.join(s.split('CM'))
            result += CM_num * 900
        if 'I' in s:
            I_num = s.count('I')
            s = ''.join(s.split('I'))
            result += I_num
        if 'V' in s:
            V_num = s.count('V')
            s = ''.join(s.split('V'))
            result += V_num * 5
        if 'X' in s:
            X_num = s.count('X')
            s = ''.join(s.split('X'))
            result += X_num * 10
        if 'L' in s:
            L_num = s.count('L')
            s = ''.join(s.split('L'))
            result += L_num * 50
        if 'C' in s:
            C_num = s.count('C')
            s = ''.join(s.split('C'))
            result += C_num * 100
        if 'D' in s:
            D_num = s.count('D')
            s = ''.join(s.split('D'))
            result += D_num * 500
        if 'M' in s:
            M_num = s.count('M')
            s = ''.join(s.split('M'))
            result += M_num * 1000
            
        return result
        