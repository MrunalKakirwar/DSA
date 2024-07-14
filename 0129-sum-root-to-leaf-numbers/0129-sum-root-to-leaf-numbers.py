# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
       
        def helper(root,currnum ):
            if root == None:
                return 0
            currnum = currnum * 10 + root.val
            left = helper(root.left, currnum)
            
            right = helper(root.right, currnum)
            if root.left == None and root.right == None:
                print(currnum)
                self.sum += currnum
            return self.sum
        return helper(root, 0)

        