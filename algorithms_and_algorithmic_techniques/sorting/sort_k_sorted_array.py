from data_structures.engineer_implemented_data_structures.trees.heaps.min_heap import MinHeap
# first step initialize two variables
# 1. minheap
# 2. keep track of next position to insert an element into

# Time complexity is O(n(log(k)))
# Space Complexity O(k)

def sortKSortedArray(array, k):
    minHeapWithKElements = MinHeap(array[:min(k + 1, len(array))])

    nextIndexToInsertElement = 0
    for idx in range(k + 1, len(array)):
        minElement = minHeapWithKElements.remove()
        array[nextIndexToInsertElement] = minElement
        nextIndexToInsertElement += 1
        currentElement = array[idx]
        minHeapWithKElements.insert(currentElement)
    while not minHeapWithKElements.isEmpty():
        minElement = minHeapWithKElements.remove()
        array[nextIndexToInsertElement] = minElement
        nextIndexToInsertElement += 1
    return array




