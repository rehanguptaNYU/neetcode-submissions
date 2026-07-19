# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        if list1==None and list2!=None:
            return list2
        if list1!=None and list2==None:
            return list1
        l1=list1
        l2=list2
        if list1.val<=list2.val:
            head=list1
            l1=list1.next
        else:
            head=list2
            l2=list2.next
        curr=head
        while(l1!=None and l2!=None):
            if(l1.val<=l2.val):
                curr.next=l1
                curr=l1
                l1=l1.next
            else:
                curr.next=l2
                curr=l2
                l2=l2.next
        if(l1!=None and l2==None):
            while(l1!=None):
                curr.next=l1
                curr=l1
                l1=l1.next
        elif(l2!=None and l1==None):
            curr.next=l2
            curr=l2
            l2=l2.next
        return head
        

        