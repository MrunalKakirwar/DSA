# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root == None:
            return res
        
        def dfs(root, level):
            if root == None:
                return 
            if len(res) == level:
                res.append(root.val)
            
            res[level] = max( res[level], root.val)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        return res