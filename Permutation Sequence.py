class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        temp = []
        c = 1
        p = 1
        while k>=c:
            temp.append(c)
            p += 1
            c *= p
        if k==temp[-1] and len(temp)==n:
            return ''.join([str(x) for x in range(n,0,-1)])
        l = n - len(temp) - 1
        ans = ""
        num = [i for i in range(1,n+1)]
        for i in range(l):
            ans += str(i+1)
            num.remove(i+1)
        for i in temp[::-1]:
            t = num[math.ceil(k/i)-1]
            num.remove(t)
            ans += str(t)
            k %= i
            if k==0:
                ans += ''.join([str(x) for x in num[::-1]])
                num = []
                break
        if len(num)>0: ans += str(num[0])
        return ans
