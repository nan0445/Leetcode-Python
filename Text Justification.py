class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        count_line = 0
        temp = []
        res = []
        for word in words:
            if not temp:
                temp.append(word)
                count_line += len(word)
            else:
                t = ' ' + word
                if count_line+len(t)<=maxWidth:
                    temp.append(t)
                    count_line += len(t)
                else:
                    n = maxWidth - count_line
                    m = len(temp) - 1
                    if m==0: res.append(''.join(temp)+' '*n)
                    else:
                        n_space = n//m
                        n_extra = n%m
                        for i in range(1,len(temp)):
                            if i<=n_extra:
                                temp[i] = ' '*(n_space+1) + temp[i]
                            else: temp[i] = ' '*n_space + temp[i]
                        res.append(''.join(temp))
                    temp = [word]
                    count_line = len(word)
        if temp:
            n = maxWidth - count_line
            res.append(''.join(temp)+' '*n)
        return res
        
