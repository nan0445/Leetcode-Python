class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = len(s)
        if l==0: return ""
        dic_all = {}
        for v in t:
            if v not in dic_all:
                dic_all[v] = 1
            else: dic_all[v] += 1
        dic_c = {item:0 for item in dic_all}
        start = 0
        count = 0
        count_c = len(dic_all)
        res = []
        for i in range(len(s)):
            if s[i] in dic_all:
                dic_c[s[i]] += 1
                if dic_c[s[i]]==dic_all[s[i]]: 
                    count+=1
                
                if count==count_c:
                    while count==count_c:
                        if s[start] in dic_c:
                            dic_c[s[start]] -= 1
                            if dic_c[s[start]]<dic_all[s[start]]:
                                count -= 1
                        start += 1
                    if i-start+2<=l:
                        l = i-start+2
                        res = [start-1,i+1]
        print(res)            
        if not res: return ""
        return s[res[0]:res[1]]
                
