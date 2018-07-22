class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        i,j = 0,0
        total = nums[0]
        ans = len(nums)+1
        while j<len(nums):
            if total < s:
                if j<len(nums)-1:
                    j+=1
                    total += nums[j]
                else: j+=1
            else:
                ans = min(ans,j-i+1)
                total -= nums[i]
                i+=1
            
        return ans if ans<len(nums)+1 else 0
