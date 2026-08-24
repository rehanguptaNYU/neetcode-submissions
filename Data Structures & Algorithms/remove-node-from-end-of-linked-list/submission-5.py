# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(head==None):
            return None
        p1=head
        p2=head
        counter=head
        i=0
        if(head.next==None and n==1):
            return None
        while(counter!=None):
            counter=counter.next
            i=i+1

        if(n==i):
            head=head.next
            return head
        for i in range(n+1):
            if(p2!=None):
                p2=p2.next
        while(p2!=None):
            p1=p1.next
            p2=p2.next
        p1.next=p1.next.next
        return head
        