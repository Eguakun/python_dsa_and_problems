'''
Algoritithm steps:

1. We created a graph, put everything in a graph. Then,
2. we grabbed all the airports that were unreachable using depth first search
    - traverse through all the airports starting at the starting airport using dfs
    - all the ones we didnt visit, we say those are unreachable.
3. then for every unreachable airport, we iterated through them and all of their connections and all of their connections' connections using dfs to assign them a score
    - go through all connections, and count importance based on number of connections.

4. Sort the unreachable airports in descending order starting with the ones that have the most unreacahble nodes
that you can connect to(highest value score),

5. create a connection to them

6. for each connection made, iterate thropugh all of its unreachable connections and mark them as now reachable

7. once we finish that process, were left with our final connections that enable us to visit all airports.


Time complexity: O(a * (a + r) + a + r + alog(a) ) nlog n for the sort, dfs for grabbing nodes and assigning scores V + E
Space complexity: O(a + r)
'''


def airportConnections(airports, routes, startingAirport):
    airportGraph = createAirportGraph(airports, routes)
    unreachableAirportNodes = getUnreachableAirportNodes(airportGraph, airports, startingAirport)
    markUnreachableConnections(airportGraph, unreachableAirportNodes)
    return getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes)


# O(a + r) time complexity
def createAirportGraph(airports, routes):
    airportGraph = {}
    for airport in airports:
        airportGraph[airport] = AirportNode(airport)
    # fill up airport connections based on routes
    for route in routes:
        airport, connection = route
        airportGraph[airport].connections.append(connection)
    return airportGraph


class AirportNode:
    def __init__(self, airport):
        self.airport = airport
        self.connections = []
        self.isReachable = True
        self.unreachableConnections = []


# O(a + r) time complexity
# O(a) space complexity
def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
    # dfs through the graph and grab all airports that we havent visited, add them to list, set their boolean to False
    visitedAirports = {}
    depthFirstTraverseAirports(airportGraph, startingAirport, visitedAirports)

    unreachableAirportNodes = []
    for airport in airports:
        if airport in visitedAirports:
            continue
        airportNode = airportGraph[airport]
        airportNode.isReachable = False
        unreachableAirportNodes.append(airport)
    return unreachableAirportNodes

def depthFirstTraverseAirports(airportGraph, airport, visitedAirports):
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    connections = airportGraph[airport].connections
    for connection in connections:
        depthFirstTraverseAirports(airportGraph, connection, visitedAirports)

# O(a * (a + r)) time complexity | space complexity: O(a) adding up to a unreachable connections
def markUnreachableConnections(airportGraph, unreachableAirportNodes):
    # how many nodes do you unlock for me?
    for airportNode in unreachableAirportNodes:
        airport = airportNode.airport
        unreachableConnections = []
        depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, {})
        airportNode.unreachableConnections = unreachableConnections

def depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, visitedAirports):
    if airportGraph[airport].isReachable:
        return
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    unreachableConnections.append(airport)
    connections = airportGraph[airport].connections
    for connection in connections:
        depthFirstAddUnreachableConnections(airportGraph, connection, unreachableConnections, visitedAirports)


# O(a log (a) + a + r) sorting
def getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes):
    unreachableAirportNodes.sort(key=lambda airport: len(airport.unreachableConnections), reverse=True)

    numberOfNewConnections = 0
    for airportNode in unreachableAirportNodes:
        if airportNode.isReachable:
            continue
        numberOfNewConnections += 1
        for connection in airportNode.unreachableConnections:
            airportGraph[connection].isReachable = True
    return numberOfNewConnections