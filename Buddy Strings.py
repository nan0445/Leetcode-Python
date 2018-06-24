class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        #if A==B: return True
        if len(A)!=len(B): return False
        temp = 0
        t = []
        flag = False
        dic = {}
        for i in range(len(A)):
            if A[i]!=B[i]:
                temp+=1
                t.append(i)
            if temp>2: return False
            if A[i] in dic.keys(): flag = True
            dic[A[i]]=1
        if temp==1: return False
        if flag and temp==0: return True
        if temp==2:
            if A[t[0]]==B[t[1]] and A[t[1]]==B[t[0]] : return True
        return False
