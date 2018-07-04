class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        while count<len(nums):
            if nums[i]==0:
                del nums[i]
                nums.insert(0,0)
                i += 1
            elif nums[i]==2:
                del nums[i]
                nums.insert(len(nums),2)
            else: i+= 1
            count += 1
