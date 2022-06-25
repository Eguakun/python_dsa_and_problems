# 1. We choose the node with the smallest value as the "current node" and visit all of its neighboring nodes. As we visit each neighbor, we update their tentative distance from the starting node. 
# 2. Once we visit al of the current node's neighbors and update their distances, we mark the current node as 'visited'. Marking a node as "visited" means that we've arrived at its final cost. 
# 3. We go back to step one. The algorithm loops until it visits all the nodes in the graph. 
from collections import deque

class City:
    def __init__(self, cityName):
        self.cityName = cityName
        self.connectedCities = []
        self.visited = False
        self.distance = 0
    
    def addConnectedCity(self, city):
        self.connectedCities.append(city)

class Graph:
    def __init__(self):
        passx

    def buildGraph(self, cities, connectedCities):
        cityGraph = {}

        for city in cities:
            c = City(city)
            cityGraph[city] = City(city)
        i = 0
        for i in range(len(connectedCities)):
            startCity = connectedCities[i][0]
            endCity = connectedCities[i][1][0]
            distance = connectedCities[i][1][1]
            i += 1
            cityGraph[startCity].connectedCities.append((endCity,distance))
            cityGraph[startCity].distance = distance
        return cityGraph
    
    def addCity(self, cityGraph, cityToAdd):
        cityGraph[cityToAdd] = City(cityToAdd)

    def addConnectedCities(self, cityGraph, connectedCities):
        i = 0
        for i in range(len(connectedCities)):
            startCity = connectedCities[i][0]
            endCity = connectedCities[i][1][0]
            distance = connectedCities[i][1][1]
            i += 1
            cityGraph[startCity].connectedCities.append((endCity,distance))
            cityGraph[startCity].distance = distance

    
    def accessConnectedCities(self, graph, city):
        i = 0
        return graph[city].connectedCities

    

    def computeShortestPathToAllNodesUsingDjisktras(self, graph, startCity):
        # Step 1: Create a list of ditsnaces initialized to infinity. 
        
        
        # Step 2: Initialize the distance of the start city to 0
        
        distances = dict()

        # Step 3: Create a list of visited noddes, all initialized to false, since we havent visited any of them. 
        visited = [False for _ in range(len(graph))]

        # Step 4a: First loop through the nodes and pick the next nodes to visit based on distance. If we loo through all of the avaialble nodes and haven't found a valid one, we break out of the inner loop. 
        temp_distances_list = []

        temp_distances_dict = {}

        for i in graph[startCity].connectedCities:
            temp_distances_dict[startCity]= (i[0],i[1])
        print(temp_distances_dict)
        
        
        

        for i in graph[startCity].connectedCities:
            temp_distances_list.append((i[0],i[1]))
        # sorted_distances_list = sorted(temp_distances_list, key=temp_distances_list[0][1])
        
        # print(temp_distances_list)

        minimumDistance = float('inf')
        for i in range(len(temp_distances_list)):
            if temp_distances_list[i][1] < minimumDistance:
                minimumDistance = temp_distances_list[i][1]
                minimumDistanceCity = temp_distances_list[i][0]
        

        


        
        # distances[startCity] = 0
        
        

        
        
        
        # Step 4b: Add the closest node to the list of visited nodes. 
        # Step 4c: Set the distance of the visited node to the  shortest distance availble. 

    def computeShortestPathToAllNodesUsingJohnsons(self, connectedCities, startCity):
        pass

    def computeShortestPathToAllNodesUsingBellmanFord(self, connectedCities, startCity):
        pass

    def computeShortestPathToAllNodesUsingFloydWarshall(self, connectedCities, startCity):
        pass

    def computeShortestPathBetweenNodesUsingFloydWarshall(self, connectedCities, startCity, endCity):
        pass

    def computeShortestPathBetweenNodesUsingDjisktras(self, connectedCities, startCity, endCity):
        pass


    def depthFirstSearch(self, graph, city, visited=set()):
        
        if city not in visited:
            # print(graph[city].connectedCities)
            visited.add(city)
            print("City ",city, " has now been visited. ")
            for connectedCity, distance in graph[city].connectedCities:
                self.depthFirstSearch(graph, connectedCity, visited)
    
          


    def breadthFirstSearch(self, graph, city, visited=set()):
        visited = set()
        queue = deque()
        if city not in visited:
            visited.add(city)
            queue.append(city)
            print("City ",city, " has now been visited. ")
          

            while queue:
                cityFirstInLine = queue.popleft()

                for connectedCity, distance in graph[cityFirstInLine].connectedCities:
                    if connectedCity not in visited:
                        visited.add(connectedCity)
                        queue.append(connectedCity)
                        print("City ",connectedCity, " has now been visited. ")

    def getDistancesList(self,connectedCities):
        distances = []
        for i in range(len(connectedCities)):
            distances.append(connectedCities[i][1][1])
        return distances



    def topologicalSort(self, graph):
        pass

    def convertAdjListToAdjMatrix(self, connectedCities, cities):
        pass


    def convertAdjMatrixToAdjList(self, adjMatrix):
        pass

    def doesPathExist(self, connectedCities, startCity, endCity):
        pass

    def removeConnection(self, graph, connectedCities):
        pass

    def removeCity(self, graph, connectedCities):
        pass

    def __str__(self):
        pass



CONNECTED_CITIES = [

    ["DSM", ["ORD", 25] ],
    ["ORD", ["BGI", 92] ],
    ["BGI", ["LGA", 99] ],
    ["SIN", ["CDG", 344] ],
    ["CDG", ["SIN", 2] ],
    ["CDG", ["BUD", 66] ],
    ["DEL", ["DOH", 57] ],
    ["DEL", ["CDG", 445] ],
    ["TLV", ["DEL", 11] ],
    ["EWR", ["HND", 435] ],
    ["HND", ["ICN", 244] ],
    ["HND", ["JFK", 535] ],
    ["ICN", ["JFK", 3] ],
    ["JFK", ["LGA", 55] ],
    ["EYW", ["LHR", 66] ],
    ["LHR", ["SFO", 643] ],
    ["SFO", ["SAN", 102] ],
    ["SFO", ["DSM", 94] ],
    ["SAN", ["EYW", 95] ]
    ]

CITIES = [
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


STARTING_CITY = "LGA"






    


g = Graph()
a = g.buildGraph(CITIES, CONNECTED_CITIES)
g.computeShortestPathToAllNodesUsingDjisktras(a,"DEL")


# print(a)

# # print(g.accessConnectedCities(a,"DEL"))
# # for  k, v in a.items():
# #     print("key: ", k, "value: ",v.connectedCities)

# d = g.breadthFirstSearch(a, "LHR")



    


        

    
    
        