class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = []
        for i in range(0,len(s)):
            if s[i]=="[":
                temp.append("[")
            if s[i]=="(":
                temp.append("(")
            if s[i]=="{":
                temp.append("{")
            if s[i]=="]":
                if len(temp)==0 or temp.pop()!="[":
                    return False
            if s[i]=="}":
                if len(temp)==0 or temp.pop()!="{":
                    return False
            if s[i]==")":
                if len(temp)==0 or temp.pop()!="(":
                    return False
        if len(temp)!=0: return False
        return True
 #OR
 class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            else:
                if not stack or stack.pop() != dic[s[i]]:
                    return False
        return stack == []
