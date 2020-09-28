# implement stack with push pop and min in o(1)
class StackNode:
    def __init__(self, data: int):
        self.data = data
        self.below = None

class Stack:
    def __init__(self, item: int):
        self.top = StackNode(item)

    def push(self, item: int):
        node = StackNode(item)
        node.below = self.top
        self.top = node

    def pop(self):
        self.top = self.top.below

    # def min(self):

if __name__ == "__main__":
    stack = Stack(8)
    node = stack.top
    stack.push(2)
    stack.push(6)
    stack.pop()
    print("hello")


