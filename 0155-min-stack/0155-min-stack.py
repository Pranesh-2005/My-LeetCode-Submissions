class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, value: int) -> None:
        curmin = min(value,self.stk[-1][1] if self.stk else value)
        self.stk.append((value,curmin))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()