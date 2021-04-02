import sys

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = 0 # 1-->red and 0--> black

class RedBlackTree():
    def __init__(self):
        self.null_node = Node(0)
        self.null_node.color = 0
        self.null_node.left = None
        self.null_node.right = None
        self.root = self.null_node

    def __print_helper(self, node, indent, last):
        # print a tree on the screen
        if node != self.null_node:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            color = "RED" if node.color == 1 else "BLACK"
            print(str(node.data) + "(" + color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def print_bst_rnb(self):
        self.__print_helper(self.root, "", True)

    def left_rotate(self, node):
        y = node.right
        node.right = y.left
        if y.left != self.null_node:
            y.left.parent = node
        y.parent = node.parent
        if node.parent == None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def right_rotate(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.null_node:
            y.right.parent = node
        y.parent = node.parent
        if node.parent == None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.right = node
        node.parent = y

    def fix_tree_insert(self, node):
        while node.parent.color == 1:
            # if parent is the right-side child of the grandparent
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == 1:
                    #set node.parent.parent to red. Set uncle and parent to black
                    node.parent.parent.color = 1
                    uncle.color = 0
                    node.parent.color = 0
                    node = node.parent.parent
                else:
                    # if uncle is set to black
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.color == 1:
                    node.parent.parent.color = 1
                    uncle.color = 0
                    node.parent.color = 0
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 0

    def insert(self, key):
        # init node
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.null_node
        node.right = self.null_node
        node.color = 1

        # traverse tree to find node parent
        y = None
        x = self.root

        while x != self.null_node:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y

        #set node on the correct side of the parent
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        # if new node is root node
        if node.parent == None:
            node.color = 0
            return

        #if node is the second element (grandparent is None)
        if node.parent.parent == None:
            return

        # else fix the tree

        self.fix_tree_insert(node)

if __name__ == "__main__":
    bst = RedBlackTree()
    bst.insert(8)
    bst.insert(18)
    bst.insert(5)
    bst.insert(15)
    bst.insert(17)
    bst.insert(25)
    bst.insert(40)
    bst.insert(80)
    bst.print_bst_rnb()
