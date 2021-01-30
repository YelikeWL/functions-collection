'''Write a Python function to implement the quick sort algorithm over a singly linked list.
The input of your function should be a reference pointing to the first node of a linked list,
and the output of your function should also be a reference to the first node of a linked
list, in which the data have been sorted into the ascending order.'''

class Node:
    
    def __init__(self, element):
        self.element = element
        self.pointer = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, e):
        new_node = Node(e)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.pointer != None:
                current = current.pointer
            current.pointer = new_node
        self.size += 1

    # Move node to a new linked list
    def move(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.pointer = self.head
            self.head = node
        self.size += 1

    def delete_head(self):
        answer = self.head
        self.head = self.head.pointer
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return answer

    # Delete current_node
    def delete(self, previous, current):
        previous.pointer = current.pointer
        current.pointer = None
        if current == self.tail:
            self.tail = previous
        self.size -= 1
        return current

    # "Glue" together a list with myList
    def append(self, myList):
        self.tail.pointer = myList.head
        self.tail = myList.tail
        self.size += myList.size

    def __str__(self):
        myList = []
        node = self.head
        while node != None:
            myList.append(node.element)
            node = node.pointer
        return str(myList)

def quick_sort(myList):    
    if myList.size == 0 or myList.size == 1:
        return myList

    previous = myList.head
    pivot = previous.element
    current = previous.pointer
    leftSide = LinkedList()  

    # Partition between left side and right side w.r.t. pivot
    while current != None:
        if current.element <= pivot:
            current = myList.delete(previous, current)
            leftSide.move(current)
        else:
            previous = current
        current = previous.pointer
    removed = myList.delete_head()
    leftSide = quick_sort(leftSide)
    rightSide = quick_sort(myList)
    rightSide.move(removed)
    
    # Return sorted list
    if leftSide.is_empty():         # in case if the pivot is the smallest number
        return rightSide
    else:
        leftSide.append(rightSide)
        return leftSide

def main():
    myList = LinkedList()
    while True:
        n = input("Please enter a number (or press any letter to stop):")
        try:
            n = float(n)
            myList.add(n)
        except ValueError:
            print("Before sorting:", myList.__str__())
            myList = quick_sort(myList)
            print("After sorting:", myList.__str__())
            try:
                print("The first node of the list:", myList.head.element)
            except AttributeError:
                print("The list is empty.")
            break

main()
