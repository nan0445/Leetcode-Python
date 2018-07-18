class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        l1,l2 = len(version1), len(version2)
        flag = False
        if l1>l2: 
            flag = True
            version1, version2 = version2, version1
        t = abs(l1-l2)
        version1 += ['0']*t
        for i in range(len(version1)):
            if int(version1[i])>int(version2[i]): return 1 if not flag else -1
            elif int(version1[i])<int(version2[i]): return -1 if not flag else 1
        return 0
