# Iterative with a queue

# FIFO

# Used for: Check if a path exists between nodes, finding hops or distance out or levels away

# Goes wide

# level order traversal of a tree

# Breadth first search on an undirected graph

# Classes:
# - Vertex
    # - Instance variables:
        # - name, neighbors[], distance, color
# - Graph
    # Instance variables:
        # vertices{}
# - Functions
 # add_neighbor(v)
 # add_vertex(vert)
 # add_edge(u, v)
 # print_graph()
 # bfs()


class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

        self.distance = 9999
        self.color = 'black'

    def add_neighbors(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
                return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + " " + str(self.vertices[key].distance))

    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.color = "red"

        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)

        while len(q) >0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = "red"
