class MinStack:

    def __init__(self):
        self.stack = []
        self.prevMin = []
        self.min = math.inf
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.prevMin.append(self.min)
        self.min = min(self.min, val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min = self.prevMin.pop()        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()