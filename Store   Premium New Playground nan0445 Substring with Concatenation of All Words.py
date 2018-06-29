class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words: return []
        n_s, n_w, n_ws = len(s), len(words), len(words[0])
        c = collections.Counter(words)
        ans = []
        for i in range(n_s+1-n_w*n_ws):
            current = dict(c)
            j = i
            for _ in range(n_w):
                temp = s[j:j+n_ws]
                if temp in current:
                    if current[temp]==1: current.pop(temp)
                    else: current[temp]-=1
                else: break
                j+=n_ws
            if not current: ans.append(i)
        return ans
