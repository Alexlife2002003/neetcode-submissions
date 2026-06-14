# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #half
        #reverse the second half
        #merge the halfs
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                break
        second=slow.next
        slow.next=None
        prev=None

        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt
        
        second=prev
        first=head

        while second:
            tmp1, tmp2=first.next, second.next
            first.next=second
            second.next=tmp1
            first, second=tmp1, tmp2
        
        