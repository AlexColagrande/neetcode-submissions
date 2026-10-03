# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        if head is None:
            return head
        while head is not None:
            stack.append(head.val)
            head = head.next
        rev_head = ListNode(stack.pop())
        rev_ll = rev_head
        
        while stack:
            rev_ll.next = ListNode(val=stack.pop())
            rev_ll = rev_ll.next
        return rev_head
