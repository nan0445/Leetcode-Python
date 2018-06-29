class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        stack, temp, k = [], [], []
        ans = 0
        flag = False
        for i in range(len(s)):
            if s[i]=="(": 
                temp.append(s[i])
                if i>0 and s[i-1]=="(": k[-1] += 1
                else: k.append(1)
                if i>0 and s[i-1]==")": 
                    stack.append(count)
                    count = 0
            else:
                if not temp:
                    stack.append(count)
                    ans = max(max(stack),ans)
                    stack = []
                    count = 0
                else:
                    temp.pop()
                    count += 2
                    k[-1] -= 1
                    if k[-1]==0:
                        k.pop()
                        if stack: 
                            count += stack[-1]
                            stack.pop()
                        
                    
        stack.append(count)
        
        ans = max(max(stack),ans)
        return ans
        
        
        
 ###############  OR #################
 ## directly record the last'(' position!!####
 class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        res = 0
        for i, chr in enumerate(s):
            if chr == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) != 0:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res
