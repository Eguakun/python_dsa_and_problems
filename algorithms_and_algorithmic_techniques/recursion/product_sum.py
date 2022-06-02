# time complexity: O(n) --> total number of elements in the original array including all of the elements in each subarray aneach of their subarrays afterwards
# space complexity: --> using up space on the call stack. whatever maximum depth of subarrays is. where m is the  max value of multiplier at any time
# O(d) where d is the depth of the subarrays

def productSum(array, multiplier):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier
