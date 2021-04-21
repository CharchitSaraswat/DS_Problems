# Build a Graph G and check if node A of the graph is connected to node b of the Graph
from collections import defaultdict

class Graph:
    def __init__(self, vertices_count):
        self.vertices_count = vertices_count
        self.graph = dict()
        for num in range(vertices_count):
            self.graph[num] = list()

    def print_graph(self):
        print(self.graph)

class BFS(Graph):

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)
        return self.graph

    def BFS(self, a, b):
        queue = list()
        nodes_visited = [False]*(self.vertices_count)
        queue.append(a)
        nodes_visited[a] = True
        while queue:
            a = queue.pop(0)
            if b == a:
                return True
            for neighbour in self.graph[a]:
                if not nodes_visited[neighbour]:
                    queue.append(neighbour)
                    nodes_visited[neighbour] = True
        return False

# plan a city with 10 points of interests
cp = BFS(10)
# simulate roads
cp.add_edge(0, 1)
cp.add_edge(0, 2)
cp.add_edge(1, 2)
cp.add_edge(2, 4)
cp.add_edge(3, 5)
cp.add_edge(5, 6)
cp.add_edge(4, 6)

cp.print_graph()
# check if a path exists
result = cp.BFS(0,5)
print(result)
result = cp.BFS(1,6)
print(result)
