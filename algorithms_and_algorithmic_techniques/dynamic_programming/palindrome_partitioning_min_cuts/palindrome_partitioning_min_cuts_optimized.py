# Time complexity: O(n ^ 2)
# Space complexity: O(n ^ 2)


def palindromePartitioningMinCuts(string):
    # build up palindromes array
    palindromes = [[False for i in string] for j in string]
    for i in range(len(string)):
        palindromes[i][i] = True
    # looping through length, looking at substrings of length 2 all the way to the length of the string

    for length in range(2, len(string) + 1):
        # for all these lengths we want to have a bunch of starting indices to go from 0 to this len because if they go beyond that number we not longer have substrings of length 2
        for i in range(0, len(string) - length + 1):
            j = i + length - 1 # why the minus 1? --> if length is 2 and i is index 0, then to get  substring of length 2 we want a suibstring that starts at 0 end ends at 1 inclusive
            if length == 2:
                palindromes[i][j] = string[i] == string[j]
            else:
                palindromes[i][j] = string[i] == string[j] and palindromes[i + 1][j - 1]


    cuts = [float('inf') for i in string]
    for i in range(len(string)):
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i - 1] + 1
            # iterating through all the other substrings that start at index j and end at index i where j is between 1 and i exclusive
            for j in range(1, i):
                # if that string is a palindrome, lets check the minimum number of cuts for the substring right before, add 1 cut to that to seperate and if that value is less than
                # what we had at cuts of i then we update.
                if palindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
                    cuts[i] = cuts[j - 1] + 1
    return cuts[-1]








