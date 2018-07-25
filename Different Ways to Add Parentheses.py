class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit(): return [int(input)]
        res = []
        
        def helper(n1, n2, op):
            if op == '+': return n1 + n2
            elif op == '-': return n1 - n2
            elif op == '*': return n1 * n2
        
        for i in range(len(input)):
            if input[i] in "+-*":
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                res.extend([helper(ln, rn, input[i]) for ln in l for rn in r])
        return res
