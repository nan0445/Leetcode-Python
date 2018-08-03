# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.l = []
        def helper(temp):
            if temp.isInteger():
                self.l.append(temp.getInteger())
                return
            else:
                x = temp.getList()
                for j in range(len(x)):
                    helper(x[j])
                    
        for i in range(len(nestedList)):
            helper(nestedList[i])
        self.index = 0

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.l[self.index - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index == len(self.l): return False
        else: return True
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
