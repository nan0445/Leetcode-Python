class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator*denominator<0: sign = '-'
        else: sign = ''
        numerator, denominator = abs(numerator), abs(denominator)
        n, m = divmod(numerator, denominator)
        ans = [sign, str(n)]
        if m==0: return ''.join(ans)
        ans.append('.')
        dic = {}
        while m!=0:
            if m in dic:
                ans.insert(dic[m],'(')
                ans.append(')')
                break
            dic[m] = len(ans)
            n, m = divmod(m*10, denominator)
            ans.append(str(n))
        return ''.join(ans)
