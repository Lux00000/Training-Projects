class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, index, data):
        
        if index < 0:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        
        for i in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        
        if current is None:
            raise IndexError("Index out of range")
        new_node.prev = current
        new_node.next = current.next
        
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_first(self):
        
        if self.is_empty():
            raise IndexError("List is empty")
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        else:
            self.head = self.head.next
            self.head.prev = None

    def remove_last(self):
        
        if self.is_empty():
            raise IndexError("List is empty")
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def remove_at(self, index):
        
        if index < 0:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.remove_first()
            return
        current = self.head
        
        for i in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        
        if current is None:
            raise IndexError("Index out of range")
        
        if current == self.tail:
            self.remove_last()
        
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def display(self):
        current = self.head
        
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


dll = DoublyLinkedList()

dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.insert(2, 2.5)

dll.display()  

dll.remove_first()
dll.remove_last()
dll.remove_at(1)

dll.display()  