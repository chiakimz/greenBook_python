
class Node:
    def __init__(self, data: int):
        self.next = None
        self.data = data

    def Node(self, d: int):
        self.data = d

    def removeDuplicates(self, head: Node) -> Node:
        n = head
        seen_data = {n.data: 1}
        
        while (n.next != None):
            if (n.next.data not in seen_data):
                seen_data[n.next.data] = 1
                n = n.next
            else:
                if n.next.next != None:
                    n.next = n.next.next
                else:
                    n.next = None
        return head

if __name__ == "__main__":
    node = Node(8)
    node.next = Node(4)
    node.next.next = Node(8)
    node.next.next.next = Node(3)
    node.next.next.next.next = Node(4)
    node.next.next.next.next.next = Node(1)
    node.removeDuplicates(node)      