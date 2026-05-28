# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Space O(1)
# time O(n+m)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = merged = ListNode(0)

        while list1 and list2:
            if list1.val<list2.val:
                merged.next=list1
                list1=list1.next
            else:
                merged.next=list2
                list2=list2.next
            merged=merged.next
        
        merged.next=list1 or list2
        return res.next
