from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, val):
        queue = list()
        visited = [False]*(max(self.graph) + 1)
        queue.append(val)
        visited[val] = True
        while queue:
            val = queue.pop(0)
            print(val, end = " ")
            for neighbour in self.graph[val]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True

g = Graph()
g.add_edge(9, 3)
g.add_edge(4, 2)
g.add_edge(25, 5)
g.add_edge(3, 9)
g.add_edge(9, 4)
g.add_edge(3, 5)
g.add_edge(4, 25)
g.BFS(3)
