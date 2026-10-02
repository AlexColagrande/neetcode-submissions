class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        node = self.head.next # the first is dummy
        for i in range(index):
            if node is None:
                return -1 
            node = node.next
        return node.val if node is not None else -1

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val=val, next_node=self.head.next)
        self.head.next = new_head
        if self.tail == self.head:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val)
        self.tail.next = new_tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        prec = self.head
        for i in range(index):
            prec = prec.next
        if prec is None or prec.next is None:
            return False
        if prec.next == self.tail:
            self.tail = prec
        prec.next = prec.next.next
        return True

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head.next
        while curr != None:
            vals.append(curr.val)
            curr = curr.next
        return vals
        
