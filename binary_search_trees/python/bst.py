class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def level_order_traversal(self, root_ptr):
        queue = list()
        queue.append(root_ptr)
        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                print(node.data)
                queue.append(node.left)
                queue.append(node.right)

    def in_order(self):
        if self.left is not None:
            self.left.in_order()
        print(self.data)
        if self.right is not None:
            self.right.in_order()

    def max_height(self, node):
        if node == None:
            return 0
        l_height = self.max_height(node.left)
        r_height = self.max_height(node.right)
        if l_height > r_height:
            l_height += 1
            return l_height
        else:
            r_height += 1
            return r_height

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
print(root.max_height(root_ptr))
root.in_order()
print("*********")
root.level_order_traversal(root_ptr)
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
