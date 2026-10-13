class MyCircularQueue:

    def __init__(self, k: int):
        self._data = [None] * k
        self._k = k
        self._front = 0
        self._count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        spot = (self._front + self._count) % self._k
        self._data[spot] = value
        self._count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._front = (self._front + 1) % self._k
        self._count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._data[self._front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self._data[(self._front + self._count - 1) % self._k]

    def isEmpty(self) -> bool:
        return self._count == 0

    def isFull(self) -> bool:
        return self._count == self._k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()