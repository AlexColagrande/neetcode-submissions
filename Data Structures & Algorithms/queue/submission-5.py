class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next 
class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next is self.tail

    def append(self, value: int) -> None:
        new_node = Node(value, self.tail.prev, self.tail)
        new_node.prev.next = new_node
        new_node.next.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value, self.head, self.head.next)
        new_node.prev.next = new_node
        new_node.next.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        popped = self.tail.prev 
        self.tail.prev = self.tail.prev.prev
        popped.prev.next = self.tail
        return popped.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        popped = self.head.next
        self.head.next = self.head.next.next
        popped.next.prev = self.head
        return popped.val
