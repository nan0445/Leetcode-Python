class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        pre = 0
        res = 0
        for i,h in enumerate(heights):
            if h>pre: stack.append((pre,h,i))
            elif h<pre:
                while stack:
                    h0,h2,ind = stack.pop()
                    res = max(res,h2*(i-ind))
                    if h0<=h: break
                stack.append((h0,h,ind))
            pre = h
        while stack:
            h0,h2,ind = stack.pop()
            res = max(res,h2*(len(heights)-ind))
        return res
