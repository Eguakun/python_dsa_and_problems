# time complexity - O(n * l) loop through all words and then loop throuigh all characters and count them
# O(c) number of keys in hash map

def minimumCharactersForWords(words):

    maximumCharacterFrequencies = {}
    for word in words:
        characterFrequencies = countCharacterFrequencies(word)
        updateMaximumFrequencies(characterFrequencies, maximumCharacterFrequencies)

    return makeArrayFromCharacterFrequencies(maximumCharacterFrequencies)

def countCharacterFrequencies(string):
    characterFrequencies = {}
    for character in string:
        # if character not in dict add in empty key that hads value of 0
        if character not in characterFrequencies:
            characterFrequencies[character] = 0
            # everytime here we will add 1 to whatever that value is
        characterFrequencies[character] += 1
    return characterFrequencies

def updateMaximumFrequencies(frequencies, maximumFrequencies):
    for character in frequencies:
        frequency = frequencies[character]

        if character in maximumFrequencies:
            maximumFrequencies[character] = max(frequency, maximumFrequencies[character])
        else:
            maximumFrequencies[character] = frequency


def makeArrayFromCharacterFrequencies(characterFrequencies):
    characters = []
    # looping through all the keys in character frequencies dictionary, getting the value associated with that key
    for character in characterFrequencies:
        frequency = characterFrequencies[character]

        
        for _ in range(frequency):
            characters.append(character)

    return characters








