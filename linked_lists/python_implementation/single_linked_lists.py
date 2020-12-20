class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_data, node):
        if not self.head:
            raise Exception("List is empty")
        for current_node in self:
            if current_node.data == target_data:
                node.next = current_node.next
                current_node.next = node
                return
        raise Exception("Target data not found in the list")

    def add_before(self, target_data, node):
        if not self.head:
            raise Exception("List is empty")
        if self.head.data == target_data:
            return self.add_first(node)
        prev_node =  self.head
        for current_node in self:
            if current_node.data == target_data:
                prev_node.next = node
                node.next = current_node
                return
            prev_node = current_node
        raise Exception("Target data not found")

    def remove_node(self, target_data):
        if not self.head:
            raise Exception("List is empty")
        if self.head.data == target_data:
            self.head = self.head.next
            return
        prev_node =  self.head
        for current_node in self:
            if current_node.data == target_data:
                prev_node.next = current_node.next
                current_node.next = None
                return
            prev_node = current_node
        raise Exception("target data not found")

    def remove_first(self):
        if not self.head:
            raise Exception("List is empty")
        self.head = self.head.next

    def remove_last(self):
        if not self.head:
            raise Exception("List is empty")
        prev_node = self.head
        for current_node in self:
            if current_node.next is not None:
                prev_node = current_node
        prev_node.next = None

    def reverse_list(self):
        if not self.head:
            raise Exception("List is Empty")
        prev_node = None
        node = self.head
        while node is not None:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
        self.head = prev_node
# Create a linked list
linked_list = LinkedList(["a", "b", "c"])
linked_list.add_first(Node("d"))
linked_list.add_last(Node("e"))
linked_list.add_after("b", Node("f"))
linked_list.add_before("b", Node("z"))
print(linked_list)
linked_list.remove_node("z")
linked_list.remove_first()
print(linked_list)
linked_list.remove_last()
# linked_list.add_after("z", Node("f")) ### raise Exception
print(linked_list)
linked_list.reverse_list()
print(linked_list)
# for node in linked_list:
#     print(node)

