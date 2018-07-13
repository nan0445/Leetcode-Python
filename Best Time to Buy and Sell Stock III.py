class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1,buy2,sold1,sold2 = -2**31,-2**31,0,0
        for v in prices:
            sold2 = max(sold2,buy2+v)
            buy2 = max(buy2,sold1-v)
            sold1 = max(sold1,buy1+v)
            buy1 = max(buy1,-v)
        return sold2
