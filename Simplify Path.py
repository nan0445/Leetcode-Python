class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = path.strip('/').split('/')
        stack = []
        for v in s:
            if v=='.' or v=='': continue
            elif v=='..':
                if stack: stack.pop()
            else: 
                stack.append(v)
        return '/'+'/'.join(stack)
