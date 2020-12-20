class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            prev_node = None
            for elem in nodes:
                node.prev = prev_node
                node.next = Node(data=elem)
                prev_node = node
                node = node.next
            node.prev = prev_node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " <-> ".join(nodes)

linked_list = LinkedList(["a", "b", "c"])
print(linked_list)
