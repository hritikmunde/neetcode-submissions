# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        def mergelists(curr_node, node1, node2):
            if node1 is None:
                curr_node.next = node2
                return None
            if node2 is None:
                curr_node.next = node1
                return None
            if node1.val <= node2.val:
                curr_node.next = node1
                mergelists(node1, node1.next, node2)
            else:
                curr_node.next = node2
                mergelists(node2, node1, node2.next)
        if list1.val <= list2.val:
            curr_node = list1
            mergelists(list1, list1.next, list2)
        else:
            curr_node = list2
            mergelists(list2, list1, list2.next)
        return curr_node