# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.getNum(l1)
        num2 = self.getNum(l2)
        res = num1 + num2
        numStr = str(res)
        prev = None
        for i in range(len(numStr)):
            node = ListNode(int(numStr[i]))
            node.next = prev
            prev = node
        return prev

    def getNum(self, node):
        stack = []
        curr = node
        numStr = ""
        while curr:
            stack.append(curr.val)
            curr = curr.next
        while stack:
            numStr += str(stack.pop())
        return int(numStr)