class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l<=1: return True
        if nums[0]==0: return False
        dp = [0 for _ in range(l)]
        for i in range(l):
            t = min(l-1,i+nums[i])
            if dp[l-1]!=0: return True
            for j in range(t,i,-1):
                if dp[j]==0 and nums[i]!=0: 
                    if i>0 and dp[i]==0: break
                    else:
                        dp[j] = dp[i]+1
                else:
                    break
        #print(dp)
        if dp[l-1]!=0: return True
        else: return False
################ a easier way ####################
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= last:
                last = i
        return not(last)
