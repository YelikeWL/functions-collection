'''Write a Python function to implement a recursive algorithm which counts the number of
nodes in a singly linked list. The input of the function should be a reference pointing to
the first node of the linked list. The output of the function should be the number of nodes
in that linked list. '''

class Node:
    
    def __init__(self, element):
        self.element = element
        self.pointer = None

    def set_pointer(self, pointer):
        self.pointer = pointer
    
    def get_pointer(self):
        return self.pointer

def count(node):        # made to be recursive
    if node == None:
        return 0
    else:
        return 1 + count(node.get_pointer())

list_is_empty = True
current = None

while True:
    prompt = input("Do you want to add a new element (y/n)?: ")
    if prompt == 'y':
        value = input("Enter element value: ")  # inappropiate input not defined
        new_node = Node(value)
        if list_is_empty:
            list_is_empty = False
        else:
            new_node.set_pointer(current)   # set new node to point the first node
        current = new_node
    elif prompt == 'n':
        break
print("The number of nodes:", count(current))
