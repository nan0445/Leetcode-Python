class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {} # set memory as the dictionary for pointers
        def dp(i, j): # this is two pointer dp. i is the pointer of string and j is the pointer of pattern
            if (i, j) not in memo: # set the memory
                if j == len(p): # if the pointer for pattern ends, then check if the pointer of string ends
                    ans = i == len(s)
                else: # if the pointer for pattern not end...
                    first_match = i < len(s) and p[j] in {s[i], '.'} # if the pointer for string not end and pattern == string or '.'
                    if j+1 < len(p) and p[j+1] == '*': # if the next pattern character is '*'
                        ans = dp(i, j+2) or first_match and dp(i+1, j) # then string[i]==pattern[j+2](skip this pattern character), or string[i+1]==pattern[j](repeat this pattern character); above make so far true
                    else: # if the next pattern character is not '*'
                        ans = first_match and dp(i+1, j+1) # then pattern has to equal as string

                memo[i, j] = ans # finally set the memory
            return memo[i, j] #save it for the dp

        return dp(0, 0) #Let's go from the beginning of both string and pattern
