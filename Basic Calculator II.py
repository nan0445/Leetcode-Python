class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [(0, '+')]
        sign = 1
        num = 0
        for i in s:
            if i == ' ': continue
            elif i == '+' or i == '-' or i == '*' or i == '/':
                if stack[-1][1] == '*' or stack[-1][1] == '/':
                    t = stack.pop()
                    if t[1] == '*': stack.append((t[0] * num, i))
                    else: stack.append((t[0] // num if t[0] >= 0 else -(-t[0] // num), i))
                else:
                    stack.append((num * sign, i))
                sign = -1 if i == '-' else 1
                num = 0
            else: num = num * 10 + int(i)
        if stack[-1][1] == '*' or stack[-1][1] == '/':
            t = stack.pop()
            if t[1] == '*': stack.append((t[0] * num, i))
            else: stack.append((t[0] // num if t[0] >= 0 else -(-t[0] // num), i))
        else:
            stack.append((num * sign, i))
        return sum([x[0] for x in stack])
            
                
        
