# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None:
            return None
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        prev=slow
        curr=slow.next
        slow.next=None
        while curr is not None:
            ahead=curr.next
            curr.next=prev
            prev=curr
            curr=ahead
        p1=head
        p2=prev
        while p2.next is not None:
            ahead1=p1.next
            ahead2=p2.next
            p1.next=p2
            p2.next=ahead1
            p1=ahead1
            p2=ahead2
        return 
        
        