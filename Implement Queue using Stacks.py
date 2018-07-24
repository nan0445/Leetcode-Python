class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        p = []
        q = self._queue
        while q:
            p.append(q.pop())
        p.append(x)    
        while p:
            q.append(p.pop())
        
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self._queue.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self._queue[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self._queue)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
