# Relationships are one-way
# Used to model airplane flights or bus routes


# Two possible ways to implement a graph is an adjacency list and an adjacency matrix

# Each piece of data in a graph is a node.

# Adjacency List
# - Each node contains a list of the places(edges) in memory(other nodes) that it is connected to
# - To model a directed graph with an adjacency list,
#   you would just put the outbound nodes that are connected in the node's list.


# Adjacency Matrix
# you have an x and y-axis. The x-axis is the "to" nodes and the y-axis is the "from" nodes
# if there is a connection between two nodes, there is a 1 in their(the two nodes) meeting spot in the matrix
# if there is not a connection between two nodes, there is a 0 in their(the two nodes) meeting spot in the matrix
# - To model a directed graph with an adjacency matrix,
#   you would just put the number in the meeting places of the outbound nodes that are connected.


# - Weighted Edges are used to represent distance or time between nodes.
    # - If you have weighted edges, this is much easier to implement with an adjacency matrix. Why?
    # - Because instead of putting a 1 in the meeting place of two nodes in the matrix,
    #   you can put the number that indicates the weight e.g. 9 or 10

# - Adjacency matrix takes up (number of vertices)^2 space, regardless of how dense or sparse the graph is



# Types of Graphs:
# - Dense Graph
    # - Each node could be connected to every other node in the graph.
    # - There are a lot of edges in proportion to the number of vertices.
    # - The number of edges = (number of vertices)^2

# - Sparse Graph
    # - Relatively few edges
    # - The number of edges are relatively equal to the number of vertices.


# Trade-offs:

# - Adjacency List --> [Use in case of sparse graph]
    # - Pro: Faster and uses less space for sparse graphs
    # - Con: Slower for dense graphs

# - Adjacency Matrix --> [Use in case of dense graph, unless we are very tight on space and dont mind the program being slower.]
    # - Pro: Faster for dense graphs
    # - Pro: Simpler for Weighted Edges
    # - Con: Uses more space


# Implementation Details:
# - Two Classes:
    # - Vertex Class
        # - The vertex class has a constructor that sets the name of the vertex and creates a new empty set to store neighbors
        # - The add_neighbor method adds the name of a neighboring vertex to the neighbors se. This set automatically eliminates duplicates.

# This implementation is an undirected graph implemented using an adjacency list:

class Vertex:
    def __init__(self, n):
        self.name =  n
        self.neighbors = set()

    def add_neighbor(self, v):
        self.neighbors.add(v)

    # Graph Class
        # - The graph class uses a dictionary to store vertices in the format, vertex_name:vertex_object
        # - Adding a new vertex to the graph, we first check if the object passed in is a vertex object,
        # - then we check if it already exists in the graph. If both checks passed, then we add the vertex to the graph's vertices dictionary
        # - When adding an edge, we recieve two vertex names, we first check if both vertex names are valid,
        # - then we add each to the other's neighbors set.

        # to print the graph, we iterate through the vertices, and print each vertex name(the key), followed by its sorted neighbors list.


class Graph:
    vertices = dict()

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, sorted(list(self.vertices[key].neighbors)))


# Graph Test code

g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))


# An Edge consists of two vertex names. Here we iterate through a list of edges and add each to the graph.
# This print_graph method doesn't give a very good visualiztion of the graph, but it does show the neighbors for each vertex.

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ']

for edge in edges:
    g.add_edge(edge[0], edge[1])

g.print_graph()



