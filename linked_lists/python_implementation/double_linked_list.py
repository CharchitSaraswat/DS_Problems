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

    def add_first(self, new_node):
        new_node.next = self.head
        new_node.prev = None
        self.head.prev = new_node
        self.head = new_node

    def add_last(self, new_node):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
        new_node.prev = node
        new_node.next = None

    def remove_first(self):
        if not self.head:
            raise Exception("List is empty")
            return
        node = self.head
        self.head = node.next
        node.next = None
        self.head.prev = None

    def remove_last(self):
        if not self.head:
            raise Exception("List is empty")
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.prev.next = None
        node.prev = None

    def add_after(self, target_data, new_node):
        if not self.head:
            raise Exception("List is empty")
            return
        node = self.head
        while node is not None:
            if node.data == target_data:
                new_node.prev = node
                new_node.next = node.next
                node.next.prev = new_node
                node.next = new_node
                return
            node = node.next
        raise Exception("target data not found")

    def add_before(self, target_data, new_node):
        if not self.head:
            raise Exception("List is empty")
            return
        node = self.head
        if self.head.data == target_data:
            return self.add_first(new_node)
        while node is not None:
            if node.data == target_data:
                node.prev.next = new_node
                new_node.next = node
                new_node.prev = node.prev
                node.prev = new_node
                return
            node = node.next
        raise Exception("target data not found")

    def remove_node(self, target_data):
        if not self.head:
            raise Exception("List is empty")
            return
        if self.head.data == target_data:
            return self.remove_first()
        node = self.head
        while node is not None:
            if node.data == target_data:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = None
                node.prev = None
                return
            node = node.next
        raise Exception("target data not found")

    def reverse_list(self):
        if not self.head:
            raise Exception("List is empty")
        prev_node = None
        node = self.head
        while node is not None:
            next_node = node.next
            prev_node = node.prev
            node.next = prev_node
            node.prev = next_node
            node = next_node
        self.head = prev_node.prev

linked_list = LinkedList(["a", "b", "c"])
linked_list.add_first(Node("d"))
linked_list.add_last(Node("e"))
linked_list.remove_first()
linked_list.remove_last()
linked_list.add_after("b", Node("f"))
linked_list.add_before("a", Node("z"))
linked_list.remove_node("b")
linked_list.reverse_list()
print(linked_list)
