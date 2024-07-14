# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, min, max):
            # base
            if root == None:
                return True
            # main cond
            if (min != None and root.val <= min):
                return False
            if (max != None and root.val >= max):
                return False

            left = helper(root.left, min, root.val)
            if left:
                right = helper(root.right, root.val, max)
            return left and right
        return helper(root, None, None)

            