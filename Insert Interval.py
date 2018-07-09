# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        flag = False
        i = 0
        if len(intervals)==0:
            intervals.append(newInterval)
            return intervals
        
        while i<(len(intervals)):
            
            if ((newInterval.start<=intervals[i].end and newInterval.end>=intervals[i].start) or (newInterval.start<=intervals[i].start and newInterval.end>=intervals[i].start)) and not flag:
                intervals[i].end = max(newInterval.end,intervals[i].end)
                intervals[i].start = min(newInterval.start, intervals[i].start)
                flag = True
                ind = i
                t = intervals[i].end
                i+=1
            elif i<len(intervals)-1 and newInterval.start>intervals[i].end and newInterval.end<intervals[i+1].start and not flag:
                intervals.insert(i+1,newInterval)
                flag = True
                break
            elif flag and t>=intervals[i].start:
                if t>=intervals[i].end: del intervals[i]
                else:
                    intervals[ind].end = intervals[i].end
                    del intervals[i]
            else: i+=1
        if not flag: 
            if newInterval.end<intervals[0].start: intervals.insert(0,newInterval)
            else: intervals.append(newInterval)       
        return intervals
