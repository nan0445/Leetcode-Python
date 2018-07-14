class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        dic = set(wordList)
        if endWord not in dic: return []
        if beginWord in dic: dic.remove(beginWord)
        ans = []
        cur = {beginWord:[[]]}
        flag = False
        
        temp = set()
        
        while cur:
            temp.clear()
            nex = {}
            for c in cur:
                c_words = [c[:i]+x+c[i+1:] for x in string.ascii_lowercase for i in range(len(c))]
                added_line = [m+[c] for m in cur[c]]
                #print(cur[c])
                for n in c_words:
                    if n not in dic: continue
                    else: 
                        temp.add(n)
                        if n not in nex:
                            nex[n] = added_line[:]
                        else: nex[n] += added_line[:]
                        if n==endWord: 
                            flag = True
                            break
            if flag:
                ans = [' '.join(p+[endWord]) for p in nex[endWord]]
                break
            cur = copy.copy(nex)
            for v in temp: dic.remove(v)
        ans = list(set(ans))
        return [m.split(' ') for m in ans]
                
