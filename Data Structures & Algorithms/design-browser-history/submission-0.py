class ListNode:
    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val
        self.prev = prev_node
        self.next = next_node

class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, prev_node=self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.prev:
                self.cur = self.cur.prev
            else:
                break
        return self.cur.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.next:
                self.cur = self.cur.next
            else:
                break
        return self.cur.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)