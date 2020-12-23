class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data

class CircularLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
            node.next = self.head

    def __contains__(self, target_data):
        current_node = self.head.next
        while current_node != self.head:
            if current_node.data == target_data:
                return True
            current_node = current_node.next
        return False

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = list()
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print("->".join(nodes))

linked_list = CircularLinkedList(["a", "b", "c"])
linked_list.print_list()
