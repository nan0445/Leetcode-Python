class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        temp = []
        
        def helper(start,s):
            if start==len(s):
                res.append(temp[:])
                return
            for i in range(start,len(s)):
                t = s[start:i+1]
                if t == t[::-1]:
                    temp.append(t)
                    helper(i+1,s)
                    temp.pop()
                    
        helper(0,s)
        return res
