class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic: dic[nums[i]] = 1
            else: dic[nums[i]] += 1
            if dic[nums[i]]>len(nums)/2: return nums[i]
