class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic={}
        dic["1"]=""
        dic["2"]="abc"
        dic["3"]="def"
        dic["4"]="ghi"
        dic["5"]="jkl"
        dic["6"]="mno"
        dic["7"]="pqrs"
        dic["8"]="tuv"
        dic["9"]="wxyz"
        dic["0"]=""
        if len(digits)==0:
            return []
        if len(digits)==1:
            return list(dic[digits[0]])
        pre = self.letterCombinations(digits[:-1])
        more = dic[digits[-1]]
        return [a+b for a in pre for b in more]
