class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0
        self.array = capacity * [None]

    def get(self, i:int) -> int:
        return self.array[i]

    def set(self, i:int, n:int) -> None:
        self.array[i] = n

    def pushback(self, n:int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1
        
    def popback(self) -> int:
        self.size -= 1
        popped = self.array[self.size]
        self.array[self.size] = None
        return popped

    def resize(self) -> None:
        self.capacity *= 2
        self.array += [None] * self.capacity
    def getSize(self) -> int:
        return self.size
    def getCapacity(self) -> int:
        return self.capacity
