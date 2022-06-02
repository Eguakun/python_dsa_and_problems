# Time complexity: O(1), we know that input will only be size of 12.
# we will only ever have at most 2 ^ 32 ip adresses
# O( 2 ^ 32) converges to O(1). 8 bits can can represent 0 -255, so 256 numbers total
# 8 bits * 4 sections in the IP = 32

# Space complexity: O(1), we can only generate a list that has 2 ^32 valid ip addresses, whihc is impossible but
# its an upper bound

# Time complexity: O(1)
# Space complexity: O(1)
def validIPAddresses(string):
    ipAddressesFound = list()
    # bc the first postion for our period can only be after the first digit
    # min of length of string end 4, so we can move to 1, 2 and 3
    # we start by placing the first period:
    for i in range(1, min(len(string), 4)):
        currentIPAddressParts = ['', '', '', '']

        # we make sure that part one is indeed valid
        currentIPAddressParts[0] = string[:i]
        if not isValidPart(currentIPAddressParts[0]):
            continue # if not we try a different placement for the first period

        # where we place the second period and to 4 so we can check the 3 places
        # min here to make sure we dont have an index error
        # here we check the second period
        for j in range(i + 1, i + min(len(string) - i, 4)):
            currentIPAddressParts[1] = string[i: j]
            # we check to see if the second part is valid
            if not isValidPart(currentIPAddressParts[1]):
                continue # if not we try a different placement for the 2nd period

            # here we place the 3rd period
            for k in range(j + 1, j + min(len(string) - j, 4)):
                currentIPAddressParts[2] = string[j: k]
                currentIPAddressParts[3] = string[k:]

                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
                    # reason is bc we need to combine all 4 parts and delimeted by a period
                    ipAddressesFound.append('.'.join(currentIPAddressParts))

    return ipAddressesFound


def isValidPart(string):
    stringAsInt = int(string)
    if stringAsInt > 255:
        return False
    return len(string) == len(str(stringAsInt))     # check for any leading zeros





