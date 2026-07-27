# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        val1=None
        val2=None
        if p.val>root.val and q.val>root.val:
            val1=self.lowestCommonAncestor(root.right,p,q)
        if p.val<root.val and q.val<root.val:
            val2=self.lowestCommonAncestor(root.left,p,q)
        if val1 is None and val2 is not None:
            return val2
        if val2 is None and val1 is not None:
            return val1
        if val1 is None and val2 is None:
            return root
        