class BinarySearchTree:
    root = None
    max_depth = 0
    my_array = []

    def add(self, value):
        if self.root == None:
            self.root = Node(value, 0)
        else: 

            current = self.root
            depth = 0
            while current != None:
                depth += 1
                if value <= current.value:
                    if current.left == None:
                        current.left = Node(value, depth)
                        if depth > self.max_depth:
                            self.max_depth = depth
                        return
                    else:
                        current = current.left

                else:
                    if current.right == None:
                        current.right = Node(value, depth)
                        if depth > self.max_depth:
                            self.max_depth = depth
                        return
                    else:
                        current = current.right

    def print_tree(self):
        self.my_array = []
        for i in range( (self.max_depth + 1) ):
            row = []
            for j in range(2**(self.max_depth+1)):
                row.append('_')
            row.append(0)
            self.my_array.append(row)
        

        self.print_array()

        self.in_order(self.root)

        self.print_array()

    def print_array(self):
        for i in self.my_array:
            print(i)
        print("\n")

        
    def in_order(self, node):
        if node != None:
            print(node.value)
            print(f"{node.value}: {node.depth}")
            nodes_at_depth = self.my_array[node.depth][-1]
            spacing = 2**(self.max_depth-node.depth + 1)
            row_index = int(spacing/2) + (spacing*nodes_at_depth)
            self.my_array[node.depth][row_index] = node.value
            self.my_array[node.depth][-1] += 1
            self.print_array()

            self.in_order(node.left)
            self.in_order(node.right)

class Node:
    left = None
    right = None
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth

my_tree = BinarySearchTree()

arr = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]

for i in arr:
    my_tree.add(i)

my_tree.print_tree()