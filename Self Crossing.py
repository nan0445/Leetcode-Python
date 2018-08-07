class Solution:
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x)<=3: return False
        flag = True if x[2] > x[0] else False
        for i in range(3,len(x)):
            if flag == False:
                if x[i]>=x[i-2]: return True
            else:
                if x[i]<=x[i-2]:
                    flag = False
                    if i>=4 and x[i-2]-x[i-4]<=x[i]:
                        x[i-1] -= x[i-3]
                    elif i==3 and x[i-2]<=x[i]:
                        x[i-1] -= x[i-3]
        return False
