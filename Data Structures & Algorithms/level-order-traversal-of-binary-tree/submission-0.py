# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.queue=deque()
        if root is None:
            return []
        self.queue.append(root)
        self.big_arr=[]
        while len(self.queue)>0:
            self.arr=[]
            for i in range(len(self.queue)):
                self.curr=self.queue.popleft()
                if self.curr.left is not None:
                    self.queue.append(self.curr.left)
                if self.curr.right is not None:
                    self.queue.append(self.curr.right)
                self.arr.append(self.curr.val)
            self.big_arr.append(self.arr)
        return self.big_arr
            

        