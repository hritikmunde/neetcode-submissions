# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        result = []
        while head:
            result.append(head.val)
            head = head.next
        
        newhead = None
        for val in result:
            newhead = ListNode(val, newhead)
        return newhead