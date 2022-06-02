# Find three largest numbers
# Write a function that takes in an array of at least three integers
# and without sorting the input array, returns a sorted array of the three largest integers in the input array
from algorithms_and_algorithmic_techniques.helpers import get_a_list as g

# we initialize an array of length three. array[0] is the third largest number, array[1] is the second largest number
# array[2] is the first largest number.
# we iterate through the array and check to see if each number is greater than our largest, second, or third largest number.
# if it is larger, we insert it into our 3 length array in its proper position and keep iterating and keep checking.


# Time complexity: O(n) where n is the length of our input array
# We have to traverse the entire array because it is unsorted and we have no other information about the numbers
# that prevent us from having to check every number to be sure.


def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, number):
    if threeLargest[2] is None or number > threeLargest[2]:
        shiftAndUpdate(threeLargest, number, 2)
    elif threeLargest[1] is None or number > threeLargest[1]:
        shiftAndUpdate(threeLargest, number, 1)
    elif threeLargest[0] is None or number > threeLargest[0]:
        shiftAndUpdate(threeLargest, number, 0)

def shiftAndUpdate(array, number, index):
    for i in range(index + 1):
        if i == index:
            array[i] = number
        else:
            array[i] = array[i + 1]