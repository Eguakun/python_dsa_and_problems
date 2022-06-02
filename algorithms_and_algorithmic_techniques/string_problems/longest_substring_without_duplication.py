# Time complexity: O(n) , where n is the length of the string, because were iterating through the string and at each point
# all we are doing is accessing/inputting values in hash tables, comparing length, all constant time operations

# Space complexity: O(min(n, a)) where n is the length of our string
# a represents the length of the alphabet that is represented in our string

# during the entire problem, we are storing letters in an dict and were storing a substring of a certain length
# how many letters can we stor in the hashtable at most?
# as many letters that are in the alphabet, so in the worse case we would have to store them all.

def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    longest = [0, 1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i + 1]
        lastSeen[char] = i
    return string[longest[0]:longest[1]]
