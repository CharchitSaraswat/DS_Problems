class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def in_order(self):
        if self.left is not None:
            self.left.in_order()
        print(self.data)
        if self.right is not None:
            self.right.in_order()

    def insert_node(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert_node(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert_node(data)

    def min_value_node(self, current):
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, root_ptr, data):
        parent = None
        curr = root_ptr
        while curr and curr.data != data:
            parent = curr
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        if curr is None:
            return root_ptr
        if curr.left is None and curr.right is None:
            if curr != root_ptr:
                if parent.left == curr:
                    parent.left = None
                elif parent.right == curr:
                    parent.right = None
            else:
                root_ptr = None
        elif curr.right and curr.left:
            in_ord_succ = self.min_value_node(curr)
            value = in_ord_succ.data
            self.delete_node(root_ptr, value)
            curr.data = value
        else:
            if curr.left:
                child = curr.left
            elif curr.right:
                child = curr.right
            if curr != root_ptr:
                if curr == parent.left:
                    parent.left = child
                if curr == parent.right:
                    parent.right = child
            else:
                root_ptr = child
        return root_ptr



root = Node(50)
root_ptr = root
root.insert_node(30)
root.insert_node(20)
root.insert_node(40)
root.insert_node(70)
root.insert_node(60)
root.insert_node(80)
root.in_order()
print("*********")
root.delete_node(root_ptr, 20)
root.in_order()
print("*********")
root.delete_node(root_ptr, 30)
root.in_order()
print("*********")
root.delete_node(root_ptr, 50)
root.in_order()
print("*********")
