# Learn Class, object, constructror and how values are referenced in Python(pass yb value or pass by reference).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert(self, data):
    new_node = Node()
    # first node
    if new_node.next == None:
        new_node.data = data
        new_node.next = None
