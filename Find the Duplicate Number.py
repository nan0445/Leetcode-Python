class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        res = nums[0]
        slow = nums[slow]
        #print(slow, fast)
        while res != slow:
            res = nums[res]
            slow = nums[slow]
        return res
