def maxSumIncreasingSubSequence(array):
    # were gonna wanna buid two arrays
# one to store greatest sums that we can generate from an icnreasing subsequence at each index
# other to sotre our sequences or indices to generate our final increasing subsequnce

# start with sequence array
    sequences = [None for x in array]
    sums = array[:] # at each index the potential best sum that we can generate is at the very least teh numnber stored at that index
    maxSumIdx = 0
    # once we have that we can start iterationg
    for i in range(len(array)):
        #declare our current num

        currentNum = array[i]

        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sum[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
    if sums[i] >= sums[maxSumIdx]:
        maxSumIdx = i
    return [sums[maxSumIdx], buildSequence()]

def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))


