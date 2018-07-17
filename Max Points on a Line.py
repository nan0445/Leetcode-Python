# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points)<=2: return len(points)
        res = 0
        for i in range(len(points)-1): 
            dic = {}
            overlap = 0
            m = 0
            if (len(points)-i)<res: return res
            for j in range(i+1,len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y: 
                    overlap += 1
                    continue
                elif points[i].x == points[j].x: t = "x"
                elif points[i].y == points[j].y: t = "y"
                else: t = (points[i].x - points[j].x) / (points[i].y - points[j].y) * 1.0
                if t not in dic:
                    dic[t] = 1
                    m = max(m,dic[t])
                else:
                    dic[t] += 1
                    m = max(m,dic[t])
            res = max(res, m+overlap+1)
        return res
