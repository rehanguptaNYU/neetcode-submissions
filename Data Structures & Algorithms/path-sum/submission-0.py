# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val==targetSum
        remaining=targetSum-root.val
        val1=self.hasPathSum(root.left,remaining)
        val2=self.hasPathSum(root.right,remaining)
        return val1 or val2
