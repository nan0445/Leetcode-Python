class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        res_l = 1
        res = s[0]
        for start in range(n):
            l = start
            r = n - start - 1
            bd = min(l,r)
            res_l_temp = 1
            if (bd+1)*2<=res_l:
                continue
            for end in range(start-bd,start+1):
                p = s[end:start+1]
                p = p[::-1]
                if (start-end+1)*2<=res_l:
                    break
                if p==s[start+1:start-end+start+1+1]:
                    res_l_temp = (start-end+1)*2
                    break
                if p==s[start:start-end+start+1]:
                    res_l_temp = (start-end)*2+1
                    break
            if res_l_temp>res_l:
                res_l = res_l_temp
                res = s[start-(res_l_temp-1)//2:start+res_l_temp//2+1]
        return res
        
        
        
 ##### Or save the length ########
 class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in range(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]
