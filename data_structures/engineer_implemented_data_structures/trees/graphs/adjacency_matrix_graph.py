# Relationships are two-way
# Used to model social or computer networks

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


# This Implementation is of an undirected graph with weighted or unweighted edges implementing using an adjacency matrix

# Implementation Details:

# - Vertex Class
    # - A vertex object only needs to store its name

class Vertex:
    def __init__(self, n):
        self.name = n

# - Graph Class
    # - A graph object has three attributes:
        # - vertices: a dictionary with vertex_name:vertex_object
        # - edges: a 2-dimensional list (i.e. matrix) of edges.
            # - For an unweighted graph it will contain 0 for no edges and 1 for an edge
        # edge_indices: a dictionary with vertex_name:list_index (eg: A:0) to access edges.
        # add_vertex: updates all three of these attributes
        # add_edge: only needs to update the edges matrix

class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            # for loop appends a column of zeroes to the edges matrix
            for row in self.edges:
                row.append(0)
            # append a row of zeroes to the bottom of the edges matrix.
            self.edges.append( [0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end=" ")
            for j in range(len(self.edges)):
                print(self.edges[i][j], end=" ")
            print(" ")


# Graph test code:


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








