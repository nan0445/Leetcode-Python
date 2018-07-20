class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k==0 or not prices: return 0
        if k >= len(prices) / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        buy = [-2**31 for _ in range(k)]
        sold = [0 for _ in range(k)]
        for v in prices:
            for i in range(k)[::-1]:
                sold[i] = max(sold[i], buy[i]+v)
                buy[i] = max(buy[i], sold[i-1]-v if i>=1 else -v)
            
        return sold[-1]
