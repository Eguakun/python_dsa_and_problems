# have to find a value in the array that is larger than its the two adjacent values to its left and right
# find peaks and compare peaks need to be two different steps

# Time complexity: O(n) youll never visit more than n nodes while comparing and you have to iterate all the way through to ensure youve found all peaks
# O(1) if array is simply increasing or decreasing

# go through the array and find a peak, once you find a peak store the length of that peak in the
# largest peak variable, once that variable is created, go through find another peak and compare the length of that peak
# to the current. if greater, replace current longest peak if not keep finding other peaks and keep comparing

# Space complexity: O(1)

def longestPeak(array):
    longestPeakLength = 0
    i = 1  # not starting at 0 because in order for a peak to be a peak its tip has to have a strictly smaller value to the left and to the right of the value
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue
        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIdx
    return longestPeakLength
