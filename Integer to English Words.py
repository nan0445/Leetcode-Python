class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return 'Zero'
        single = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        double = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy','Eighty', 'Ninety']
        unit = ['Thousand', 'Million','Billion']
        ten = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        i, x = 0, 0
        temp = []
        res = []
        while num>0:
            num, p = divmod(num, 10)
            if i == 0 and p > 0:
                temp = [single[p-1]] + temp
            elif i == 1 and p > 0:
                if p != 1:
                    temp = [double[p-1]] + temp
                else:
                    if not temp: temp = ['Ten']
                    else:
                        ind = single.index(temp[0])
                        temp = [ten[ind]]
            elif i == 2:
                if p>0:
                    temp = [single[p-1], 'Hundred'] + temp
                if temp:
                    if x > 0: res = temp + [unit[x-1]] + res
                    else: res = temp + res
                temp = []
                i = -1
                x += 1
            i += 1
        if temp:
            if x>0: res = temp + [unit[x-1]] + res
            else: res = temp + res
        return ' '.join(res).strip()
