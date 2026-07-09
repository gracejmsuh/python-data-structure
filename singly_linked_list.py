'''
This file shows how to implement singly linked list using Python.
'''

'''
First, define the class Node to make instances of each node used in linked list 
'''
class Node:
    def __init__(self, key):
        # Value that node has
        self.key = key

        # Link to next node
        self.next = None
    
    def __str__(self):
        return str(self.key)
    
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.key))
            current = current.next
        nodes.append("None")
        return " -> ".join(nodes)

    '''
    Add node in front of the head of linked list 
    O (1) -> takes constant time, regardless of the linked list. No need to traverse elements in the linked list
    '''
    def add_node_front(self, key): 
        new_node = Node(key) # Create new node
        new_node.next = self.head # Link it to the head node
        self.head = new_node # Change the head node to be the new node
        self.size += 1 # Increase the size 

    '''
    Add node at the back of the linked list
    O(n) -> needs to traverse the list to find the end(tail) then link new node to be new tail
    '''
    def add_node_back(self, key):
        new_node = Node(key) # Create new node 
        if len(self) == 0: # If empty linked list
            self.head = new_node # New node becomes head and tail 
        else:
            tail = self.head # Need to follow from head to find tail
            while tail.next != None:
                tail = tail.next # Follow the link until it reaches the end
            tail.next = new_node # Link tail to new node -> now new node is tail
        self.size += 1 # Increase size

    '''
    Delete the front/head node in linked list
    O(1) -> No need to traverse the list, shift the head node and delete old one 
    '''
    def pop_front(self):
        if len(self) == 0: # If empty linked list, nothing to delete
            return None
        else:
            old_head = self.head # Head node 
            key = old_head.key # Save the key value of the head node
            self.head = old_head.next # Reset head node
            self.size -= 1 # Decrease size
            del old_head # Delete node
            return key # Return the value of deleted node
    
    '''
    Delete the node in the back of the linked list
    O(n) -> need to traverse the list to find the tail and delete it
    '''
    def pop_back(self):
        if len(self) == 0: # If empty linked list, nothing to delete
            return None
        else:
		    # Running technique
            prev, tail = None, self.head # Starting from the head
            while tail.next != None: # Keep following the link until it reaches the end
                prev = tail 
                tail = tail.next 
            if len(self) == 1: # When there is only one node in the linked list
                self.head = None
            else:
                prev.next = None # prev is now tail 
            
            key = tail.key
            del tail 
            self.size -= 1 # Decrease size 
            return key 

L = SinglyLinkedList()
L.add_node_front(-1)
L.add_node_front(9)
L.add_node_back(4)
L.add_node_front(3)
L.add_node_front(5)
L.add_node_back(7)
L.pop_back()
L.pop_front()
print(L)
