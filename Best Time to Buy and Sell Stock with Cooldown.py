class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1: return 0
        keep = -prices[0]
        sell = 0
        relax = 0
        buy = -prices[0]
        for i in prices:
            keep = max(buy, keep)
            buy = -i + relax
            relax = max(relax, sell)
            sell = i + keep
        return max(sell, relax)
        
