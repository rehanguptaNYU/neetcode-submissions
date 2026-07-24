# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValNode(self,root):
        curr=root
        while(curr is not None and curr.left is not None):
            curr=curr.left
        return curr
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if(key<root.val):
            root.left=self.deleteNode(root.left,key)
        elif(key>root.val):
            root.right=self.deleteNode(root.right,key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.right is None and root.left is not None:
                return root.left
            elif root.left is None and root.right is not None:
                return root.right
            elif root.left is not None and root.right is not None:
                sucessor_val=self.minValNode(root.right).val
                root.val=sucessor_val
                root.right=self.deleteNode(root.right,sucessor_val)

        return root