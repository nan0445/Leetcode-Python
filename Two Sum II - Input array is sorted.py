class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for ind, n1 in enumerate(numbers):
            n2 = target - n1
            if n2 in dic:
                return [dic[n2]+1,ind+1]
            else:
                dic[n1] = ind
        return []
