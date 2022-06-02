# What is a trie?
# - A data structure for storing items based off of prefixes the items share in common.
# - Imagine if we want to store the words "wait", "waiter", "shop", "shopper"

# Time complexity to scheck if word shopper is in each data structure

# List -> O(NM) where N is the number of words in list and M is length of shopper.
# For each word in the list you have to iterate through every word which is O(n) and you have to do a comparison
# operation which is O(m) so it would be O(nm)

# Trie -> O(M) where M is the length of shopper because you dont have to do extra comparisons
# Tries are optimal when you have prefixed based words
# Adding a word to a trie takes O(M) time where M is the length of the word to be added.

# Types of questions that could be good for Tries:
# - Given a list of words, find if a given word is in that list of words, instead of using a list, make a trie.
# - Given a list of words, finding the longest prefix that is shared by the most amount of words, use a trie.


# Implementation #1:

# class Trie:
#     def __init__(self):
#         self.root = {'*':'*'}
#
#     def add_word(self, word):
#         curr_node = self.root
#         for letter in word:
#             if letter not in curr_node:
#                 curr_node[letter] = {}
#             curr_node = curr_node[letter]
#         curr_node["*"] = "*"
#
#     def does_word_exist(self, word):
#         curr_node = self.root
#         for letter in word:
#             if letter not in curr_node:
#                 return False
#             curr_node = curr_node[letter]
#         return "*" in curr_node

# Implementation #2:

class TrieNode:
    def __init__(self, letter,):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode(letter)
            curr_node = curr_node.children[letter]
        curr_node.is_end_of_word = True

    def does_word_exist(self, word):
        if word == "":
            return True
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.is_end_of_word


# Test code

trie = Trie()
words = ["wait", "waiter", "shop", "shopper"]

for word in words:
    trie.add_word(word)

print(trie.does_word_exist("wait"))
print(trie.does_word_exist(""))
print(trie.does_word_exist("waite"))
print(trie.does_word_exist("shop"))
print(trie.does_word_exist("shoppp"))

