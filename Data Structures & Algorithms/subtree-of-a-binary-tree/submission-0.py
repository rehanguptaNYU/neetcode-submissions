# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            if p is None and q is not None:
                return False
            if p is not None and q is None:
                return False
            if p.val!=q.val:
                return False
            val1=self.isSameTree(p.left,q.left)
            val2=self.isSameTree(p.right,q.right)
            return val1 and val2
        def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if self.isSameTree(root,subRoot)==True:
                return True
            else:
                if root is None:
                    return False
                val1=self.isSubtree(root.left,subRoot)
                val2=self.isSubtree(root.right,subRoot)
            return val1 or val2


        
        