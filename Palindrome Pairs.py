class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dic = {word: i for i, word in enumerate(words)}
        res = []
        for j, word in enumerate(words):
            
            for i in range(len(word)+1):
                if word[:i] == word[:i][::-1]:
                    w = word[i:][::-1] 
                    if w != word and w in dic: res.append([dic[w],j])
                if i>0 and word[-i:] == word[-i:][::-1]:
                    w = word[:-i][::-1] 
                    if w != word and w in dic: res.append([j, dic[w]])
        return res
