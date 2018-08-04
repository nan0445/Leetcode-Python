class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack, count = [], []
        s = preorder.split(',')
        if s[0] == '#' and len(s) > 1: return False
        if s[0] == '#' and len(s) == 1: return True
        stack.append(s[0])
        count.append(0)
        for i in s[1:]:
            if not stack: return False
            if i != '#':
                stack.append(i)
                count.append(0)
                count[-2] += 1
            else:
                count[-1] += 1
            while count and count[-1] == 2:
                stack.pop()
                count.pop()
        if not stack: return True
        else: return False
###################################################
######## This is very smart!! #####################
class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        exp = 1
        preorder = preorder.split(',')
        for p in preorder:
            exp -= 1
            if(exp < 0):
                return False
            if(p != '#'):
                exp += 2
        return exp == 0
