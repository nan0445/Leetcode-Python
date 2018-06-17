class ExamRoom(object):
    s_n = 0
    stack = []
    def __init__(self, N):
        """
        :type N: int
        """
        self.s_n = N
        self.stack = []
        
    def seat(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            self.stack.append(0)
            return 0
        else:
            stack_whole = self.stack[:]
            stack_whole.insert(0,-self.stack[0])
            stack_whole.append(2*self.s_n-1-self.stack[-1])
            mm = 0
            l_ind = 0
            for x in range(1,len(stack_whole)):
                temp = (stack_whole[x]-stack_whole[x-1])//2
                if temp>mm:
                    l_ind = x-1
                    mm = temp
            self.stack.insert(l_ind,stack_whole[l_ind]+mm)
            return stack_whole[l_ind]+mm

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        if p in self.stack:
            self.stack.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
