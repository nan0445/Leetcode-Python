class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        M = collections.Counter(nums)
        rev = {}
        for i in M:
            if M[i] not in rev:
                rev[M[i]] = [i]
            else: rev[M[i]].append(i)
        res = []
        for i in range(1, len(nums)+1)[::-1]:
            if i in rev:
                res += rev[i]
            if len(res) >= k:
                break
        print(M,rev)
        return res[:k]
