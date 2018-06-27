class Solution:
    digit = {str(i):i for i in range(10)}
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0": return "0"
        res = "0"
        count = 0
        for s in num2[::-1]:
            temp = self.multi_by_single_digit(num1,s)
            res = self.addtwo(res,temp+"0"*count)
            count+=1
        return res
        
    def multi_by_single_digit(self,num1,figure):
        temp = []
        for s in num1[::-1]:
            carry,single = divmod(self.digit[s]*self.digit[figure],10)
            if len(temp)>0:
                single += self.digit[temp[-1]]
                carry += single//10
                single %= 10
                temp[-1] = str(single)
            else:
                temp.append(str(single))
            temp.append(str(carry))
        if temp[-1]=="0": temp.pop()
        return ''.join(temp[::-1])
        
    def addtwo(self,s1,s2):
        temp = []
        if len(s1)>len(s2): s1,s2 = s2,s1
        s1 = s1[::-1]
        s2 = s2[::-1]
        carry = 0
        for i in range(len(s2)):
            if i<len(s1):
                single = self.digit[s1[i]] + self.digit[s2[i]] + carry
            else:
                single = self.digit[s2[i]] + carry
            carry = single//10
            single %= 10
            temp.append(str(single))
        if carry>0: temp.append(str(carry))
        return ''.join(temp[::-1])
