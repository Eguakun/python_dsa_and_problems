# we pick a combo for the all digits up until the last digit, then on the last digit,
# we go all of the possible options with all of the leading digits staying the same
# once we go through all of those combinations, we go back to the digit before the last digit and change it, then iterate through all the options for that change and the options for the last digit. and we repeat this process going back one digit at a time
# 1905
# 1w0j --> 1w0k --> 1w0l --> 1x0j --> 1x0k --> 1x0l

# if we get a sstrign with all 1s and 0s we return the exact same string
# 1s and 0s cannot be changed

# the base case/ when our functions will stop is when we call the recursive function on an index that is greater than or equal to the length of our phone numbner

# Time complexity: O((4 ^n) *n)
# - 4^n comes from number of recursive calls that we will have at most to our recursive function
# - looking at our mapp we see that the most amount of characters that represent a digit is 4
# thats where we get this 4 from. we could have a phone number filled completely with 9s right
# 4 to the n because were trying to figure out the most number of recursive calls that we weill have
# for every level in our decision tree of 3 9s there will be 4 branches to come out at each level exponentionally

# when we hit the base case of our algorithm we need to create a string based on the current array
# turning that into a string and adding to list is O(n) operation
# base case takes n times and we hit base case at worst 4 ^ n times


# Space Complexity: O((4 ^n) *n)

def phoneNumberMnemonics(phoneNumber):
    currentMnemonic = ['0'] * len(phoneNumber)
    mnemonicsFound = []
    # call our recursive function starting at index zero
    phoneNumberMnemonicsHelper(0, phoneNumber, currentMnemonic, mnemonicsFound)
    return mnemonicsFound


def phoneNumberMnemonicsHelper(idx, phoneNumber, currentMnemonic, mnemonicsFound):
    # base case
    if idx == len(phoneNumber):
        mnemonic = ''.join(currentMnemonic) # O(n)
        mnemonicsFound.append(mnemonic)
        # recursive case
    else:
        digit = phoneNumber[idx]
        letters = DIGIT_LETTERS[digit]
        for letter in letters:
            currentMnemonic[idx] = letter
            phoneNumberMnemonicsHelper(idx + 1, phoneNumber, currentMnemonic, mnemonicsFound)







DIGIT_LETTERS = {
        "0": ["0"],
        "1": ["1"],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }



