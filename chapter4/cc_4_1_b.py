from collections import deque

class Graph:
    nodes = []

class Node:
    def __init__(self,name):
        self.name = name
        self.children = []

my_graph = Graph()

connections = [[1,4,5], [3,4], [1], [2,4], [], []]

for i in range(len(connections)):
    node = Node(i)
    Graph.nodes.append(node)

for i in range(len(Graph.nodes)):
    parent = my_graph.nodes[i]
    for j in connections[i]:
        child = my_graph.nodes[j]
        parent.children.append(child)

def Search(graph, start, end):
    if (start == end):
        return True
    
    q = deque()

    for i in graph.nodes:
        i.state = "unvisited"

    start.state = "visiting"
    q.append(start)
    n = None

    while(len(q) != 0):    
        n = q.popleft()
        for child in n.children:
            if child.state == "unvisited":
                if child == end:
                    return True
                else:
                    child.state = "visiting"
                    q.append(child)
        n.state = "visited"

    return False


start = my_graph.nodes[5]
end = my_graph.nodes[0]
print(Search(my_graph, start, end))