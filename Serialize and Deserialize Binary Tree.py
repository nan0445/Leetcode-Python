# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return 'null'
        return str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        s = data.split(',')
        if s[0] == 'null': return None
        def helper(s):
            if not s: return
            temp = s.pop(0)
            if temp == "null": return
            root = TreeNode(int(temp))
            root.left = helper(s)
            root.right = helper(s)
            return root
        return helper(s)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
