class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '?'}
                    if i<len(s) and j+1<len(p) and p[j] == '*':
                        ans = dp(i, j+1) or dp(i+1, j)
                    elif j==len(p)-1 and p[j]=='*': ans = True
                    elif p[j]=='*' and i==len(s): ans = dp(i,j+1)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
