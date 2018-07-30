class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        l, r = 0, len(self.__nums)-1
        while l<r:
            mid = (l+r)//2
            if self.__nums[mid]<num:
                l = mid + 1
            elif self.__nums[mid]>num:
                r = mid
            else:
                l = mid
                break
        if not self.__nums: self.__nums.append(num)
        else:
            if self.__nums[l] >= num: self.__nums.insert(l, num)
            else: self.__nums.insert(l+1, num)

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.__nums)
        if n % 2 == 0: return (self.__nums[n//2] + self.__nums[n//2-1]) / 2.0
        else: return self.__nums[(n-1)//2] * 1.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
