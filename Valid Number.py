class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s)==0: return False
        if s and s[0]=='e': return False
        if s and s[-1]=='e': return False
        if s=='.': return False
        flag_num = False
        dic = {'0':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1,'.':0,'e':0}
        ind_e,ind_dot = len(s)-1,0
        for i in range(len(s)):
            if i==0 and (s[i]=='-' or s[i]=='+'): continue
            if (s[i]=='+' or s[i]=='-') and i>0 and s[i-1]=='e' and i<len(s)-1: continue 
            if s[i] not in dic: return False
            if s[i]=='e': ind_e = i
            if s[i]=='.': ind_dot = i
            if ind_dot>ind_e: return False
            if s[i]=='.' or s[i]=='e': del dic[s[i]]
            if s[i]=='e' and i==1 and (s[i-1]=='-' or s[i-1]=='.'): return False
            if s[i]=='e' and i<len(s)-1 and s[i+1]=='.': return False
            
            if s[i] in dic and dic[s[i]]==1: flag_num = True
        if not flag_num: return False
        return True
        
                
