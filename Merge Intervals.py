# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)==0: return []
        intervals.sort(key = lambda x: x.start)
        res = []
        temp = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i].start>temp.end:
                res.append(temp)
                temp = intervals[i]
            else:
                temp.end = max(intervals[i].end, temp.end)
        res.append(temp)
        return res
