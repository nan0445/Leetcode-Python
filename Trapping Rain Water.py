class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<3: return 0
        l,r = 0, 0
        ans = 0
        temp = []
        r_ind = []
        
        def SumHeight(p,q,x,height):
            res = 0
            for m in range(p,q):
                if x>=height[m]:
                    res += height[m]
                else: res += x
            return res
        
        for i in range(1,len(height)):
            if height[i]>=height[l]:
                if i-l>=2:
                    ans += height[l]*(i-l-1)-sum(height[l+1:i])
                    temp = []
                    r_ind = []
                l = r = i
            else:
                if height[i]>height[r]:
                    r = i
                    if r - l >= 2:
                        if r_ind: 
                            while r_ind and height[i]>height[r_ind[-1]]:
                                r_ind.pop()
                                temp.pop()
                            if r_ind: t = r_ind[-1]
                            else: t = l
                            r_ind.append(i)
                            temp.append(height[i]*(i-t-1)-SumHeight(t+1,i,height[i],height))
                        else:
                            r_ind.append(i)
                            temp.append(height[i]*(i-l-1)-SumHeight(l+1,i,height[i],height))
                        
                else:
                    r = i
        ans += sum(temp)
        return ans
                
                
  ###############Below is a very smart solution############################
  class Solution:
    '''Complexity O(n)'''

    def trap(self, height):
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0

        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1

            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1

            minHeight = min(height[l], height[r])

        return water
