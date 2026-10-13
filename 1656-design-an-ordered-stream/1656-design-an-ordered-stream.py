class OrderedStream:

    def __init__(self, n: int):
        self.n = [None] * n # list starts from index 0
        self.i = 0 # set pointer at slot 1 which is index 0 of n
        
    def insert(self, idKey: int, value: str) -> list[str]:
        output = []
        self.n[idKey-1] = value 
        # idKey of 1 goes into the first slot of list n which is 0
        while self.i < len(self.n) and self.n[self.i] != None:
            # while the pointer isnt out of index and the ith slot in n isnt empty
            output.append(self.n[self.i]) 
            self.i += 1
        return output




# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)