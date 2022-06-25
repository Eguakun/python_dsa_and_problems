# FINDING MINIMUM NUUMBER OF CONNECTIONS TO REACH ALL CONNECTIONS/NODES

# we need to assign a value to each node based upon how many other connections we can access by adding a connection to that node. 

# so the problem would be to find out how many connections we can reach for every node in the graph 

# 1.  Find all airports that are unreachable from the starting node. 
    # so we have to come up with a way to tell if a node is reachable or not 
    # what is reachable? 
        # - no outbound connection 

# 2. Give a value score to all nodes/connections based on how many other nodes/connection we can access

# 3. Go to the node with the highest score and draw a connection to that node from the starting node. 

# 4. When we go down the node with the highest score to visit its neighbors using DFS, we need to keep track of which other nodes we have new access to so we dont revisit the same nodes. 

# 5. Go to the next highest score node and continue the same process. 

# 6. Keep track of how many new connections that we are making. 

# 7. Once weve visited all of the nodes we can return the number of connections that we made. 

# 8. Also return a list of the nodes that we drew connections to. 

# Time complexity: O(n + c + n log(n)) where n is the number of nodes and c is the connections

# because we sort our nodes based on the score, and we do DFS on the nodes which give us the nodes plus connection time complexity

# O ( (a) * (a + r) + (a + r) + (a log(a)) ) 
def nodeConnections(nodes, connections, startingNode):
    # we need a way to represent our nodes and connections, so that will be via a directed graph
    nodeGraph = createNodeGraph(nodes, connections)

    # STEP #1 we need to gather all of the unreachable nodes from the starting node. 
        # we know a node is unreachable if there is no connection from the startingNode,node[i] 
    
    unreachableNodes = getUnreachableNodes(nodeGraph, nodes, startingNode)
    markConnectionsThatCanBeUnlockedByConnecting(nodeGraph, unreachableNodes)
    return getMinNumberOfNewConnections(nodeGraph, unreachableNodes)


# Time Complexity: O(n + c) where n is the number of nodes and c is the number of connections
# Space Complexity: O(n + c) where n is the number of nodes and c is the number of connections
def createNodeGraph(nodes, connections):

    nodeGraph = {}
    for node in nodes:
        # for each node in our list of nodes, we want to create a place in our dicitonary with the node identifier/name as the key
        # the value here will be another custom object that we create call CustomNode
        nodeGraph[node] = CustomNode(node)

    for connection in connections:
        startConnectingNode, endConnectingNode = connection
        nodeGraph[startConnectingNode].connections.append(endConnectingNode)

    return nodeGraph



def getUnreachableNodes(nodeGraph, nodes, startingNode):
    visitedNodes = {}
    depthFirstTraverseNodes(nodeGraph, startingNode, visitedNodes)
    unreachableNodes = []

    for node in nodes:
        if node in visitedNodes:
            continue 
        customNode = nodeGraph[node]
        customNode.isReachable = False
        unreachableNodes.append(customNode)
    return unreachableNodes


# Time Complexity: O(n + c) where n is the number of nodes and c is the number of connections
# Space Complexity: O(n) where n is the number of nodes


def depthFirstTraverseNodes(nodeGraph, node, visitedNodes):
    if node in visitedNodes:
        return 
    visitedNodes[node]= True
    connections = nodeGraph[node].connections
    for connection in connections:
        depthFirstTraverseNodes(nodeGraph, connection, visitedNodes)


# Time complexity: O(a * (a + r))
# Space complexity: O(a) 
def markConnectionsThatCanBeUnlockedByConnecting(nodeGraph, unreachableNodes):
    for unreachableNode in unreachableNodes:
        node = unreachableNode.nodeName
        connectionsThatCanBeUnlockedByConnecting = []
        depthFirstAddConnectionsThatCanBeUnlockedByConnecting(nodeGraph, node, connectionsThatCanBeUnlockedByConnecting, {})
        unreachableNode.connectionsThatCanBeUnlockedByConnecting = connectionsThatCanBeUnlockedByConnecting


def depthFirstAddConnectionsThatCanBeUnlockedByConnecting(nodeGraph, node, connectionsThatCanBeUnlockedByConnecting, visitedNodes):
    if nodeGraph[node].isReachable:
        return
    if node in visitedNodes:
        return
    visitedNodes[node] = True
    connectionsThatCanBeUnlockedByConnecting.append(node)
    connections = nodeGraph[node].connections
    for connection in connections:
        depthFirstAddConnectionsThatCanBeUnlockedByConnecting(nodeGraph, connection, connectionsThatCanBeUnlockedByConnecting, visitedNodes)
    





# Time complexity: O(a log(a))
# Space complexity: O(1)
def getMinNumberOfNewConnections(nodeGraph, unreachableNodes):
    unreachableNodes.sort(key= lambda node: len(node.connectionsThatCanBeUnlockedByConnecting), reverse=True)

    numberOfNewConnections = 0
    for unreachableNode in unreachableNodes:
        if unreachableNode.isReachable:
            continue
        numberOfNewConnections += 1
        for connection in unreachableNode.connectionsThatCanBeUnlockedByConnecting:
            nodeGraph[connection].isReachable = True
    return numberOfNewConnections


class CustomNode:
    def __init__(self, nodeName):
        self.nodeName = nodeName
        self.connections = []
        self.visited = False
        self.isReachable = True
        self.connectionsThatCanBeUnlockedByConnecting = []



c = [["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"]]

n = [
    "BGI",
    "CDG",
    "DEL",
    "DOH",
    "DSM",
    "EWR",
    "EYW",
    "HND",
    "ICN",
    "JFK",
    "LGA",
    "LHR",
    "ORD",
    "SAN",
    "SFO",
    "SIN",
    "TLV",
    "BUD",
]

s = "LGA"


# n = nodeConnections(n,c,s)
# print("Node connections answer :", n)


a = createNodeGraph(n, c)
for  k, v in a.items():
    print("key: ", k, "value: ",v)



