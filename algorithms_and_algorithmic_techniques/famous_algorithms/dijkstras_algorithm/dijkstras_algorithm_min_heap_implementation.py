# time complexity: O((v + e) * log(v))
# space complexity: O(v) space
def dijkstras_algorithm(start, edges):
    # defined a variable to hold the number of vertices which  is equal to the number of edges
    numberOfVertices = len(edges)
    # list that stores min distances for all vertices
    minDistances = [float("inf") for _ in range(numberOfVertices)]
    # the distance to get to the start vertex is always zero
    minDistances[start] = 0

    minDistancesHeap = MinHeap([(idx, float('inf')) for idx in range(numberOfVertices)])
    minDistancesHeap.update(start, 0)


    # we terminate when the length of what is visited is equal to the number of vertices
    while not minDistancesHeap.isEmpty():
        # grabs vertex from our list with the min value that has not yet been visited
        vertex, currentMinDistance = minDistancesHeap.remove()
    # if the distance to this vertex equals infinity, we can go ahead and stop the algorithm bc we know that there is no way to get to that vertex
    # we would already have reached it if we could have


        if currentMinDistance == float('inf'):
            break
            # add the vertex to the visited set

        for edge in edges[vertex]:
            destination, distanceToDestination = edge

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance
                minDistancesHeap.update(destination, newPathDistance)


    # look at our min distances list and replace any inf with -1 denoting we couldnt reacvh that vertex
    return list(map(lambda x: -1 if x == float('inf') else x, minDistances))


def getVertexWithMinDistance(distances, visited):
    currentMinDistance = float('inf')
    vertex = None

    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue
        if distance <= currentMinDistance:
            vertex = vertexIdx
            currentMinDistance = distance
    return vertex, currentMinDistance



class MinHeap:
    def __init__(self, array):
        # mapping that stores vertex value and what position in the internal array that rep this heap that that vertex is in
        # reason why is we need to be able to find very quckly where each vertex is in the heap so i can potenitally upadate its distance or iupdate its value
        # otherwise theres no way in non linear time, to update the value of a vertex
        self.vertexMap = {idx:idx for idx in range(len(array))}
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    def buildHeap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for currentIdx in reversed(range(first_parent_idx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array


    def siftDown(self, currentIdx, endIdx, heap):
        child_one_idx = currentIdx * 2 + 1
        while child_one_idx <= endIdx:
            child_two_idx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if child_two_idx != -1 and heap[child_two_idx][1] < heap[child_one_idx][1]:
                idxToSwap = child_two_idx
            else:
                idxToSwap = child_one_idx
            if heap[idxToSwap][1] < heap[currentIdx][1]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                child_one_idx = currentIdx *2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx][1] < heap[parentIdx][1]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        vertex, distance = self.heap.pop()
        self.vertexMap.pop(vertex)
        self.siftDown(0, len(self.heap) -1,  self.heap)
        return vertex, distance

    def swap(self, i, j, heap):
        self.vertexMap[heap[i][0]] = j
        self.vertexMap[heap[j][0]] = i
        heap[i], heap[j] = heap[j], heap[i]

    def update(self, vertex, value):
        self.heap[self.vertexMap[vertex]] = (vertex, value)
        self.siftUp(self.vertexMap[vertex], self.heap)




