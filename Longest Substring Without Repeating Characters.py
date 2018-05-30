class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = start
        l = len(s)
        dic = {}
        count = 0
        max_count = count
        for i in range(0,l):
            if s[i] not in dic or dic[s[i]]==None:
                dic[s[i]] = i
                end = i
                count += 1
            else:
                new_start = dic[s[i]]+1
                for j in range(start,new_start):
                    dic[s[j]] = None
                dic[s[i]] = i
                start = new_start
                end = i
                count = end - start + 1
            max_count = count if count>max_count else max_count
        return max_count
        
 #OR
 class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
            
        return max_length
