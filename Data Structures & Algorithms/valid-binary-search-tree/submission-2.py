# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.arr=[]
    def inorder(self, root: Optional[TreeNode]):
        if root is None:
            return None
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val1=True
        if root is None:
            return None
        self.inorder(root)
        for i in range(len(self.arr)-1):
            if self.arr[i+1]<=self.arr[i]:
                val1=False
            
        return val1
            