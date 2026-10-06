class ListNode:
    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val
        self.prev = prev_node
        self.next = next_node

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1, prev_node=self.head)
        self.head.next = self.tail

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        cur = self.head.next
        for _ in range(index):
            if cur is self.tail:
                return -1
            cur = cur.next
        return -1 if cur is self.tail else cur.val
            

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val, prev_node=self.head, next_node=self.head.next)
        self.head.next = new_head
        new_head.next.prev = new_head
        

    def addAtTail(self, val: int) -> None:
        new_tail = ListNode(val, prev_node=self.tail.prev, next_node=self.tail)
        self.tail.prev = new_tail
        new_tail.prev.next = new_tail
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0: 
            return -1 

        cur = self.head.next
        for _ in range(index):
            if cur is self.tail:
                return -1
            cur = cur.next

        new_node = ListNode(val, cur.prev, cur)
        cur.prev.next = new_node
        cur.prev = new_node
            
    def deleteAtIndex(self, index: int) -> None:
        if index < 0: 
            return -1 

        cur = self.head.next
        for _ in range(index):
            if cur is self.tail:
                return -1
            cur = cur.next
        
        if cur is self.tail:
            return -1
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)