class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        num += 1 
        bit_counts = [0] * num
        for i in range(1, num):
            bit_counts[i] = bit_counts[i>>1] + (i&1)
        return bit_counts
