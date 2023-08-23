class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # fetching the min value
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


def main():
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)

    param_1 = obj.getMin()
    print(param_1)

    print("popped : ", obj.pop())

    param_2 = obj.top()
    print(param_2)

    param_3 = obj.getMin()
    print(param_3)


if __name__ == "__main__":
    main()
