import pprint 
from collections import defaultdict

class Graph(object):

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self.directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)
        
    
    def add(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)
    
    def remove(self, node):
        for key, value in self._graph.items():
            try:
                value.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass
    
    def is_connected(self, node1, node2):
        return node1 in self._graph and node2 in self._graph[node1]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph))

connections = [('A','B')]