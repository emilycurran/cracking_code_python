from collections import deque

class Graph:
    nodes = []

    def route_between_nodes(root1, root2):
        #need to design a breadth first search between two
        #nodes and check if there is collision on each iteration
        #of the search
        
        queue1 = deque()
        queue2 = deque()

        root1.visited1 = True
        root2.visited2 = True

        queue1.append(root1)
        queue2.append(root2)

        while(len(queue1) != 0 or len(queue2) != 0):

            if len(queue1) != 0:
                node1 = queue1.popleft()

                if node1.visited2 == True:
                    return True

                for n in node1.children:
                    if n.visited1 == False:
                        n.vistited1 = True
                        queue1.append(n)

            if len(queue2) != 0:
                node2 = queue2.popleft()

                if node2.visited1 == True:
                    return True

                for n in node2.children:
                    if n.visited2 == False:
                        n.visited2 = True
                        queue2.append(n)

        return False

class Node:

    def __init__(self, name):
        self.name = name
        self.children = []
        self.visited1 = False
        self.visited2 = False

    def print_children(self):
        string = f"{self.name} is connected to:"
        for i in self.children:
            string += f" {i.name}," 

my_graph = Graph

connections = [[1,4,5], [3,4], [1], [2,4], [], []]

for i in range(len(connections)):
    node = Node(i)
    Graph.nodes.append(node)

for i in range(len(Graph.nodes)):
    parent = my_graph.nodes[i]
    for j in connections[i]:
        child = my_graph.nodes[j]
        parent.children.append(child)

root1 = my_graph.nodes[3]
root2 = my_graph.nodes[0]

