class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num
        while l<r:
            mid = (l+r)//2
            if mid ** 2 == num : return True
            elif mid ** 2 < num: l = mid + 1
            else: r = mid
        if l ** 2 == num or (l-1) ** 2 == num: return True
        else: return False
