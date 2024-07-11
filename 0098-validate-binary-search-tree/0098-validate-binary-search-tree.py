# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        self.prev = None
        self.flag = True
        def findIfBST(root):
            if root == None:
                return
            findIfBST(root.left)
            if self.prev is not None and self.prev.val >= root.val:
                self.flag = False
            self.prev = root
            findIfBST(root.right)
            
        findIfBST(root)
        return self.flag