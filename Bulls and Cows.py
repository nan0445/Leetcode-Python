class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A, B = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
        M = collections.Counter(secret) & collections.Counter(guess)
        B = sum([M[x] for x in M]) - A 
        return str(A) + 'A' + str(B) + 'B'
            
