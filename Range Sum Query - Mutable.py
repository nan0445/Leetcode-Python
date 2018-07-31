class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums: return
        self.__n = nums
        l = math.sqrt(len(nums))
        self.lens = math.ceil(len(nums)/l)
        self.b = [0 for _ in range(self.lens)]
        for i in range(len(nums)):
            self.b[i // self.lens] += nums[i]
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        b_l = i // self.lens
        self.b[b_l] = self.b[b_l] - self.__n[i] + val
        self.__n[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        s = 0
        startBlock = i // self.lens
        endBlock = j // self.lens
        if startBlock == endBlock: 
            for k in range(i, j+1):
                s += self.__n[k]
        else:
            for k in range(i, (startBlock + 1) * self.lens): 
                s += self.__n[k]
            for k in range(startBlock + 1, endBlock):
                s += self.b[k]
            for k in range(endBlock * self.lens, j+1):
                s += self.__n[k]
    
        return s

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
