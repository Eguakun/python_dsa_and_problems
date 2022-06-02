# Time complexity:
# - Searching: O(M) where M is the length of whatever string we are searching for in the suffix trie

# - Building the Trie: O(n ^ 2), where n is the length of the input string that were looking for,bc were
#   iterating through all the suffixes and all their characters
# Could use eukonins algorithsm to build in O(n) time but it would take a lot more time to build here.

# Space Complexity:
# Searching: O(1), because were not storing any extra space, and we already have our suffix trie construction.

# Building the Trie: O(n ^ 2), if there arent too many repeating characters we will have to store every character in the suffix trie
# O(n) if we had a string that had the same character - would be a straight line trie w/ a bunch of asterisks.

# useful for finding, strings, searching for strings, matching strings. you might could use a trie

class SuffixTrie:
    def __init__(self, string):
        self.root = {}  # root node, empty node points to empty python dictionary
        self.endSymbol = "*"  # denotes the end of a suffix
        self.populateSuffixTrieFrom(string)  # takes in a string, checks if each letter is there, and stores if not

# O(n ^ 2) time | O(n ^ 2) space
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    def insertSubstringStartingAt(self, i, string):
        node = self.root  # declaring our node to be root of tree
        for j in range(i, len(string) - 1):  # start iterating through all letters in string
            letter = string[j]
            if letter not in node: # if the letter not in node.
                node[letter] = {}  # create a new node for that letter
            node = node[letter]  # continue traversing the tree by updating our current node to point to the node of the current letter that were at, which is either an existing node or the one we just created
# once were done after weve added or visited existing nodes, add an asterisk at the end
        node[self.endSymbol] = True

# O(m) time complexity --> where m is length of input string that you're looking for
# O(1) space complexity --> because you're not using any additional space
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node  # return assertion that asterisk is in our current node which represents the final letter in our string.


