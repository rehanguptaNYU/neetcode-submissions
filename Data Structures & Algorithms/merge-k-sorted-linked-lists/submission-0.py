# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        list1=list(enumerate(lists))
        for (list_index,node) in list1:
            if node is not None:
                heap.append((node.val,list_index,node))
        heapq.heapify(heap)
        head=None
        curr=None
        while (len(heap)!=0):
            (value,list_index,smallest_node)=heapq.heappop(heap)
            if head is None:
                head=smallest_node
                current=smallest_node
            else:
                current.next=smallest_node
                current=current.next
            if(smallest_node.next is not None):
                next_node=smallest_node.next
                heapq.heappush(heap,(next_node.val,list_index,next_node))
        return head
            
        



