class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        flag = None
        n = 1
        ans = 0
        stack = []
        for i in range(1,len(ratings)):
            if ratings[i]<ratings[i-1]:
                if flag == None or flag == False: n += 1
                elif flag == True:
                    ans += sum(range(2,n+1))
                    stack.append(n)
                    n = 1
                flag = False
            elif ratings[i]>ratings[i-1]:
                if flag == None:
                    n += 1
                    ans += 1
                elif flag == True: n += 1
                elif flag == False:
                    ans += sum(range(n+1))
                    if stack:
                        t = stack.pop()
                        if n>=t: ans += n+1-t
                    n = 2
                flag = True
            else:
                if flag == True: ans += sum(range(2,n+1))
                elif flag == False: 
                    ans += sum(range(n+1))
                    if stack:
                        t = stack.pop()
                        if n>=t: ans += n+1-t
                else: ans += 1
                n = 1
                flag = None
        if flag == True: ans += sum(range(2,n+1))
        elif flag == False: 
            ans += sum(range(n+1))
            if stack:
                t = stack.pop()
                if n>=t: ans += n+1-t
        else: ans += 1
        return ans
        
################## OR #########################

class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        count = [1 for _ in range(len(ratings))]
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]: count[i] = count[i-1] + 1
        for i in range(0,len(ratings)-1)[::-1]:
            if ratings[i]>ratings[i+1]: count[i] = max(count[i], count[i+1]+1)
        return sum(count)
