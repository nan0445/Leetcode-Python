class LRUCache(object):
    dic = {}
    stack = []
    c = 0
    count = 0
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.dic = {}
        self.stack = []
        self.count = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic: 
            self.stack.remove(key)
            self.stack.insert(0,key)
            return self.dic[key]
        else: return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.count<self.c:
            if key not in self.dic:
                self.count+=1
            else: 
                self.stack.remove(key)
                del self.dic[key]
            
        else:
            if key in self.dic:
                self.stack.remove(key)
                del self.dic[key]
            else:
                del self.dic[self.stack.pop()]
        
        self.stack.insert(0,key)
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
