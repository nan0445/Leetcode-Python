class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost): return -1
        temp = []
        for i in range(len(gas)):
            temp.append(gas[i]-cost[i])
        
        i=0
        while i<len(temp):
            t = temp[i:]+temp[:i]
            s = 0
            for j in range(len(t)):
                s += t[j]
                if s<0: break
            else: return i
            #print(j)
            i += j + 1
        return -1
