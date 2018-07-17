class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in {"+","-","*","/"}:
                stack.append(i)
            else:
                t2 = int(stack.pop())
                t1 = int(stack.pop())
                if i=="+":
                    t = t1 + t2
                elif i=="-":
                    t = t1 - t2
                elif i=="*":
                    t = t1 * t2
                elif i=="/":
                    t = t1/t2
                stack.append(t)
                print(t)
        return int(stack[-1])
                
