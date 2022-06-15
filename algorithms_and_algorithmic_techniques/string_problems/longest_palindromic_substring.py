# Apalindrome has to have a center. We can check from the center and expand from there
# we keep track as we expand and once we cant expand anymore we have the length of the palindrome

# 1. check palindromicity
# 2. check palindromes length from above algorithm
# 3. return palindome with the longest length.

# O(n ^ 2) time complexity
# O (n) space since we have to slice and store the palindromic string

# we iterate through the array and use every letter as a potential center letter.
# then we check the letters adjacent to the potential center letter
# if they are equal then we expand our pointers out and check again

# define current longest palindromic substring
# we will update this throughout the algorithm

def longestPalindromicSubstring(string):
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1) # centered at the given letter
        even = getLongestPalindromeFrom(string, i - 1, i) # were saying our current letter is the starting letter because the center of our palindrome is in between those two letters
        longest = max(odd, even, key = lambda x: x[1] - x[0]) # take a look at odd and even and check which one is longer by taking the difference of the value at index 1 in them and 0 at them
        currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]] # slice current longest out of the current longest

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string): # if were still in our string
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1

    return [leftIdx + 1, rightIdx]
# once we break out of this while loop, we are past the length of the string or were at a left index that is not equal to the right index
# so we hit the if condition and break out of the while loop
#
