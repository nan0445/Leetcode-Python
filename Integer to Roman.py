class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = {}
        s[0]=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        s[1]=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        s[2]=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        s[3]=["","M","MM","MMM"]
        count = 0
        res = []
        while num>0:
            ind = num % 10
            res.insert(0,s[count][ind])
            num = num//10
            count+=1
            
        return ''.join(res)
            
        
