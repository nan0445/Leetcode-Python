class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        temp = "1"
        for i in range(n-1):
            count = 1
            t = ""
            for j in range(1,len(temp)):
                if temp[j]!=temp[j-1]:
                    t += str(count) + temp[j-1]
                    count = 1
                else: count += 1
            t += str(count) + temp[-1]
            temp = t
        return temp
