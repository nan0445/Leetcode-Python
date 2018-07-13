# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        res = []
        def helper(root,k):
            if not root: return
            if k==len(res) or res==[]: res.append([])
            res[k].append(root)
            helper(root.left,k+1)
            helper(root.right,k+1)
        helper(root,0)
        for i in range(len(res)):
            for j in range(len(res[i])):
                if j<len(res[i])-1:
                    res[i][j].next = res[i][j+1]
                else: res[i][j].next = None
        
        
