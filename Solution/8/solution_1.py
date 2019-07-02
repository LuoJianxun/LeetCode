class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        new_str = str.lstrip()
        sub_str = new_str.split(' ')[0]
        try:
            result = int(sub_str)
        except:
            if len(sub_str) <= 1:
                return 0
            else:
                if sub_str[0] == '-' and sub_str[1].isdigit():
                    result = 0 - self.get_num(sub_str[1:])
                elif sub_str[0] == '+' and sub_str[1].isdigit():
                    result = self.get_num(sub_str[1:])
                elif sub_str[0].isdigit():
                    result = self.get_num(sub_str)
                else:
                    return 0
        
        if result < pow(-2, 31):
            result = pow(-2, 31)
        elif result > (pow(2, 31) - 1):
            result = (pow(2, 31) - 1)

        return result
                
    def get_num(self, str):
        for i in range(len(str)):
            if str[i].isdigit():
                pass
            else:
                break
        return int(str[:i])