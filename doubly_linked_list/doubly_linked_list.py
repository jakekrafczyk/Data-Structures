"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)     # if this is the tail, currentnext should be none
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev    # currentprev = stores the original prev set in the node instantiation
        self.prev = ListNode(value, current_prev, self)     # sets self.prev to a new object with the new value,
        if current_prev:                                    # current prev as its prev, and the current node as
            current_prev.next = self.prev                   # its next value, effectively inserting the new value
                                                            # If statement sets the prev value's next to the current node
    """Rearranges this ListNode's previous and next pointers 
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        old_head = self.head
        if old_head != None:
            old_head.insert_before(value)       # inserts new value as old_head.prev
            self.head = old_head.prev
        else:
            self.head = ListNode(value)
            if self.length == 0:
                self.tail = ListNode(value)

        self.length += 1                    # update length

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        old_head = self.head
        self.head.delete()
        if self.length == 1:
            self.tail.delete()
            self.tail = None

        self.length -= 1
        self.head = old_head.next
        return old_head.value
        
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        old_tail = self.tail
        if old_tail != None:
            old_tail.insert_after(value)        # this returns the node with a node added onto .next
            # self.tail = ListNode(value,prev=old_tail,next=None)
            self.tail = old_tail.next
            
        else:
            self.tail = ListNode(value)
            if self.length == 0:
                self.head = ListNode(value)

        self.length += 1  
            
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        old_tail = self.tail
        self.tail.delete()
        if self.length == 1:
            self.head.delete()
            self.head = None

        self.length -= 1
        self.tail = old_tail.prev
        # self.tail = ListNode(s)
        # self.tail.next = None
        #self.tail.prev = the same as before
        return old_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        node_val = node.value
        node.delete()
        self.length -= 1
        self.add_to_head(node_val)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        node_val = node.value
        node.delete()
        self.length -= 1
        self.add_to_tail(node_val)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass


dll = DoublyLinkedList()
dll.add_to_head(40)

print(dll.head.value, dll.tail.value)

dll.move_to_end(dll.head)

print(dll.head.value, dll.tail.value)

dll.add_to_tail(4)

print(dll.head.value, dll.tail.value)

dll.move_to_end(dll.head.next)      # apparently this is a Nonetype and has no .value

print(dll.head.value,dll.tail.value)
# assertEqual(dll.tail.value, 40)
# assertEqual(dll.tail.prev.value, 4)
# assertEqual(len(dll), 3)