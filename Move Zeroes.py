class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        while count<len(nums):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
            else:
                i += 1
            count += 1
