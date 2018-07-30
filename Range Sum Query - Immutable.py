class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__s = []
        for i in range(len(nums)):
            if not self.__s:
                self.__s.append(nums[i])
            else:
                self.__s.append(self.__s[-1] + nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.__s[j] - self.__s[i-1] if i>0 else self.__s[j]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
