# implement stack with push pop and min in o(1)
class StackNode:
    def __init__(self, data: int):
        self.data = data
        self.below = None
class MiniStack:
    def __init__(self):
        self.top = None

    def push(self, item: StackNode):
        if self.top == None or item.data <= self.top.data:
            item.below = self.top
            self.top = item

    def pop(self, top: StackNode):
        if self.top == top:
            self.top = self.top.below

    def isEmpty(self) -> bool:
        return self.top == None

    def peek(self) -> int:
        if self.isEmpty():
            raise RuntimeError("The stack is empty")
        return self.top.data


class Stack(MiniStack):
    def __init__(self, item: StackNode):
        self.top = item
        self.mini = MiniStack()

    def push(self, item: int):
        self.mini.push(item)
        item.below = self.top
        self.top = item

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("The stack is empty")
        self.mini.pop(self.pop)
        self.top = self.top.below

    def min(self) -> int:
        if self.mini.top is None:
            raise RuntimeError("The stack is empty")
        return self.mini.peek()

if __name__ == "__main__":
    stack = Stack(StackNode(8))
    node = stack.top
    stack.push(StackNode(2))
    stack.push(StackNode(6))
    stack.push(StackNode(1))
    stack.push(StackNode(3))
    minimum = stack.min()
    print("hello")


