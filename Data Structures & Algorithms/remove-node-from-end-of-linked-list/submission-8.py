# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        second = head
        for _ in range(n):
            second = second.next
        if second is None:
            return head.next
        first = head
        while second.next:
            first = first.next
            second = second.next
        curr = first.next
        first.next = curr.next
        return head