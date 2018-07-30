class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def dfs(remain, curr_str, curr, prev):
            if not remain and curr == target:
                res.append(curr_str)
                
            for i in range(1, len(remain) + 1):
                if len(curr_str) == 0:   #avoid generate str begin with +-*
                    if not (i > 1 and remain[0] == '0'):   # avoid '0X' case be counted
                        dfs(remain[i:], remain[:i], int(remain[:i]), int(remain[:i]))
                else:
                    if not (i > 1 and remain[0] == '0'):
                        dfs(remain[i:], curr_str + '+' + remain[:i], curr + int(remain[:i]), int(remain[:i]))
                        dfs(remain[i:], curr_str + '-' + remain[:i], curr - int(remain[:i]), -int(remain[:i]))
                        # need take extra care for '*' case, a+b*c = a+b-b+b*c
                        dfs(remain[i:], curr_str + '*' + remain[:i], curr - prev + prev * int(remain[:i]), prev * int(remain[:i]))
            
        res = []
        dfs(num, '', 0, 0)
        return res
