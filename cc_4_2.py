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

def create_tree_sorted(array):
    my_tree = BinarySearchTree()

    root_value = array[int(len(array)/2)]
    my_tree.add(root_value)

    add_center(my_tree.root, array, 0)
    print(f"max_depth: {my_tree.max_depth}")
    my_tree.max_depth = 3

    my_tree.print_tree()

def add_center(parent, array, depth):
    depth += 1
    if len(array) == 1:
        return
    left_array = array[0: int(len(array)/2)]
    left_node = Node(left_array[int(len(left_array)/2)], depth)
    print(left_array)
    print(f"left_node: {left_node}")
    parent.left = left_node

    if len(array) >= 3:
        right_array = array[int(len(array)/2) + 1:]
        right_node = Node(right_array[int(len(right_array)/2)], depth)
        print(right_array)
        print(f"right_node: {right_node}")
        print(f"connected {parent.value} to {left_node.value} and {right_node.value}")
        parent.right = right_node
    else:
        right_array = [0]



    add_center(parent.left, left_array, depth)
    add_center(parent.right, right_array, depth)



    return



my_tree = BinarySearchTree()

arr = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44] 

for i in arr:
    my_tree.add(i)

my_tree.print_tree()

sorted = sorted(arr)

create_tree_sorted(sorted)



