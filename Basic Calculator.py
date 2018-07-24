class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        sign = 1
        temp = ''
        while i<len(s):
            if s[i]==' ': 
                if temp:
                    res += sign * int(temp)
                    temp = ''
                i += 1
                continue
            elif s[i]=='(':
                m = self.calculate(s[i+1:])
                res += sign * m[0]
                i += m[1] + 1
            elif s[i]==')':
                if temp:
                    res += sign * int(temp)
                    temp = ''
                return [res, i]
            elif s[i]=='+': 
                if temp:
                    res += sign * int(temp)
                    temp = ''
                sign = 1
            elif s[i]=='-': 
                if temp:
                    res += sign * int(temp)
                    temp = ''
                sign = -1
            else:
                temp += s[i]
            i += 1
        if temp:
            res += sign * int(temp)
        return res
