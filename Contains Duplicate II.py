class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):
            if v not in dic:
                dic[v] = [i]
            else:
                t = dic[v].pop()
                if i-t<=k: return True
                dic[v].append(i-t)
                dic[v].append(i)
        return False
