class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        ans = 1
        nums_s = set(nums)
        for v in nums_s:
            if v-1 not in nums_s:
                cur = v
                n = 1
                while cur+1 in nums_s:
                    cur += 1
                    n += 1
                ans = max(ans,n)
        return ans
