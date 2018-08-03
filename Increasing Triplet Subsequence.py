class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=2: return False
        t, b = None, None
        for i in range(1,len(nums)):
            if t == None:
                if nums[i] > nums[i-1]: 
                    t, b = nums[i], nums[i-1]
                    
            else:
                if nums[i] > t: return True
                else:
                    if b < nums[i] < t: t = nums[i]
                    if nums[i] < b: b = nums[i]
        return False
