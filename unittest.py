class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
    
root = Node(21)
root.left = Node(324)
root.right = Node(214)