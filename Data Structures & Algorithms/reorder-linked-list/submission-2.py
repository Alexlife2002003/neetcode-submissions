# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #half list
        #reverse second half
        #merge
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        
        second=slow.next
        prev=None
        slow.next=None

        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt
        
        second=prev
        first=head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2
        