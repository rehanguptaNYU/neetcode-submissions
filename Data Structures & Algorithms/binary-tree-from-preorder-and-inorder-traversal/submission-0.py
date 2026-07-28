# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0 and len(inorder)==0:
            return None
        root=TreeNode(preorder[0])
        root_index=inorder.index(preorder[0])
        left_arr1=inorder[0:root_index]
        left_size=len(left_arr1)
        right_arr=inorder[root_index+1:]
        root.left=self.buildTree(preorder[1:left_size+1],left_arr1)
        root.right=self.buildTree(preorder[left_size+1:],right_arr)
        return root


            
        
        