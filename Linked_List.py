class LinkedList:
    head = None
    lenght = 0

    class Node:

        def __init__(self, element, next_node = None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            self.lenght += 1 
            return element
        
        node = self.head
        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)
        self.lenght += 1
        return element
    
    def __str__(self):
        node = self.head
        line = "["
        while node.next_node:
            line += str(node.element) + ", "
            node = node.next_node
        line += str(node.element) + "]"
        
        return line
    
    def getitem(self,key):
        i = 0
        node = self.head

        while i < key:
            node = node.next_node
            i += 1
        return node.element
    
    def insert(self, key, value):
        i = 0
        node = self.head
        prev_node = self.head

        if key == 0:
            old_head = self.head
            self.head = self.Node(value, next_node= old_head)
            self.lenght += 1
            return value
        
        while i < key:
            prev_node = node
            node = node.next_node
            i += 1
        
        prev_node.next_node = self.Node(value, next_node= node)
        self.lenght += 1
        return value
    
    def delitem(self, key):
        i = 0 
        node = self.head
        prev_node = node

        if key == 0:
            old_head = self.head
            element = self.head.element
            self.head = self.head.next_node
            self.lenght -= 1

            del old_head
            return element
        
        while i < key:
            prev_node = node
            node = node.next_node
            i += 1

            prev_node.next_node = node.next_node
            element = node.element
            self.lenght -= 1

            del node
            return element


        
