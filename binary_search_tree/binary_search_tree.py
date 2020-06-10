"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):  
        if value < self.value:
            # go left
            # first check if a left value exists
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

        else:
            # go right
            # first check if right value exists
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target < self.value:
            # go left
            # first check if a left value contains a value
            if self.left:
                if self.left.value == target:
                    return True
                # if not, check the next node
                else:
                    self.left.contains(target)

            else:
                return False

        else:
            # go right
            # first check if a right value contains a value
            if self.right:
                if self.right.value == target:
                    return True
                # if not, check the next node
                else:
                    self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.value:          # if theres a value for the node, call the function
            fn(self.value)
            if self.left:       # then, if theres another value to the left, repeat the function
                self.left.for_each(fn)
            if self.right:
                self.right.for_each(fn)
        
        #return fn

            

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        arr = []
        fn = lambda x: arr.append(x)
        self.for_each(fn)
        
        #values = sorted(values)
        for x in sorted(arr):
            print(x)



        # #values = []
        # if not self.left:
        #     print(self.value)
        #     if self.right:
        #         return self.right.in_order_print()
        #     else:
        #         #move up the tree


        # return self.left.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BSTNode(5)
bst.insert(30)
bst.insert(4)



print(bst.in_order_print())