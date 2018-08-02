class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = {'a','e','i','o','u','A','E','I','O','U'}
        s = list(s)
        temp = []
        for i in s:
            if i in vowel: temp.append(i)
        for i in range(len(s)):
            if s[i] in vowel: s[i] = temp.pop()
        return ''.join(s)
