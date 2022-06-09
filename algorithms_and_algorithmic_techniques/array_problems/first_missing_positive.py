class Solution:
    def firstMissingPositive(self, A):
        # scan through the array and turn every negative value to 0
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = 0
         # now we will start marking values as having appeared in the array
        # we want to mark that the number 3 exists in our array
        # so were going to go to index = 3 - 1 which is 2, so we go to index 2 and we will change this value
        # to a negative value to indicate that the number 3 exists in our array
        # effectively using the input array as memory and keeping the constant memory constraint
        for i in range(len(A)):
            val = abs(A[i])
            if 1 <= val <= len(A):
                if A[val - 1] > 0:
                    A[val - 1] *= -1
                elif A[val - 1] == 0:
                    A[val - 1] = -1 * (len(A) + 1)
        # iterate through from 1 to len of input array, and return the first missing number
        for i in range(1, len(A) + 1):
            if A[i - 1] >= 0:
                return i
        # return the number above the range if not found

        return len(A) + 1