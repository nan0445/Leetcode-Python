class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1: return 0
        b,s = prices[0],prices[0]
        ans = 0
        for i in range(1,len(prices)):
            if prices[i]>b:
                s = prices[i]
                ans = max(ans,s-b)
            elif prices[i]<b:
                b = prices[i]
                
        return ans
