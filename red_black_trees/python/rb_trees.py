class Node():
    def __init__(self, data, left=None, right=None, parent=None, color=0):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color # 1-->red and 0--> black

class RedBlackTree():
    def __init__(self):
        self.root = Node(0)
        self.root.color = 0
        self.root.left = None
        self.root.right = None
