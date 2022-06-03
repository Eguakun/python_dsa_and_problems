# time complexity: O(n) - two n time operations, go through and create counts data structure, then we iterate back through to look at all frequencies
# Space complexity: O(1) - at most 26 unique characters, hash tables has finite number of keys

def firstNonRepeatingCharacter(string):
    characterFrequencies = {}
    for character in string:
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1

    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx
    return -1



