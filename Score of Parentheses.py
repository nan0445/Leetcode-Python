class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        temp = ""
        flag = False
        for i in range(len(S)):
            if flag: 
                flag = False
                continue
            if i<=len(S)-2 and S[i]=="(" and S[i+1]==")":
                if i==len(S)-2 or S[i+2]==")":
                    temp += "1"
                else:
                    temp += "1+"
                flag = True
            elif S[i]==")":
                if i<len(S)-1 and S[i+1]=="(":
                    temp += ")+"
                else:
                    temp += ")"
                flag = False
            elif S[i]=="(":
                temp += "2*("
                flag = False
        return eval(temp)
