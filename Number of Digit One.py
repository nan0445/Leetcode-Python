class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        f, pre, cur, base = 1, 0, 0, 1
        res = 0
        num_normal = 0
        while n>0:
            n, cur = divmod(n, 10)
            if cur > 1:
                res += cur * num_normal + f
            elif cur == 1:
                res += cur * num_normal + pre + 1
            
            pre = cur * base + pre
            base *= 10
            num_normal = num_normal * 10 + f
            f *= 10
        return res
            
