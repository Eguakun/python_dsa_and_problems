# we need to find all of the palindrome subsequences in our sequence and return that number minus one?


# time complexity: O(n ^ 3)
# space complexity: O( n ^ 2)

def palindromePartitioningMinCuts(string):
    # build up palindromes array
    palindromes =[[False for i in string] for j in string]
    for i in range(len(string)):
        for j in range(i, len(string)):
            palindromes[i][j] = isPalindrome(string[i: j + 1]) # calling this n ^2 times and it takes O(n) time to run = O(n ^ 3)

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

def isPalindrome(string):
    # if string[:] == string[::-1]:
    #     return True

    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True





