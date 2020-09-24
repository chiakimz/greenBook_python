class Node:
    def __init__(self, data: int):
        self.next = None
        self.data = data

    def Node(self, d: int):
        self.data = d

    def kthToTheLast(self, head: Node, k: int) -> Node:
        n = head
        nodelist = []
        i = 0
        while (n != None):
            nodelist.append(n)
            if (n.next == None):
                if(k > i + 1):
                    raise ValueError("k cannot be bigger than the length of the linked list.") 
                return nodelist[i - k + 1]
            n = n.next
            i += 1


if __name__ == "__main__":
    node = Node(8)
    node.next = Node(4)
    node.next.next = Node(8)
    node.next.next.next = Node(3)
    node.next.next.next.next = Node(4)
    node.next.next.next.next.next = Node(1)
    n = node.kthToTheLast(node, 1)
    print("hello")