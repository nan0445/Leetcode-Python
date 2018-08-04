class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def helper(x):
            count = 0
            for c in x:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0: return False
            return count == 0
        
        hold = {s}
        
        while True:
            res = list(filter(helper, hold))
            if res: return res
            hold = {s[:i] + s[i+1:] for s in hold for i in range(len(s))}
 
        
