class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        temp = []
        res = []
        dic = {}
        def helper(s,start):
            if len(temp)==4 and len(''.join(temp))==len(s):
                t = '.'.join(temp[:])
                if t in dic: return
                else: 
                    dic[t] = 1
                    res.append('.'.join(temp[:]))
                
                return
            if len(temp)>=4: return
            if start>=len(s): return
            temp.append(s[start])
            helper(s,start+1)
            temp.pop()
            if s[start]!="0":
                temp.append(s[start:start+2])
                helper(s,start+2)
                temp.pop()
                if int(s[start:start+3])<=255:
                    temp.append(s[start:start+3])
                    helper(s,start+3)
                    temp.pop()
        helper(s,0)
        return res
            
