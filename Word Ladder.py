class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dic = set(wordList)
        if endWord not in dic: return 0
        
        cur_w = {beginWord}
        next_w = {endWord}
        ans = 1
        
        while cur_w and next_w:
            ans += 1
            t = set()
            if len(cur_w)>len(next_w): cur_w,next_w = next_w,cur_w
            for c in cur_w:
                c_1 = [c[:i]+x+c[i+1:] for x in string.ascii_lowercase for i in range(len(c))]
                for n in c_1:
                    if n in next_w: return ans
                    if n not in dic: continue
                    dic.remove(n)
                    t.add(n)
            cur_w = t
            
        return 0
        
