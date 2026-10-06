# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative 

        # prev, curr = None, head
        # while curr is not None:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr 
        #     curr = temp
        # return prev

        # Recursive
        if not head:
            return 
        if not head.next:
            return head

        rev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rev


