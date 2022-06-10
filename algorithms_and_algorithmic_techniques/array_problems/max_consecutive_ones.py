def findMaxConsecutiveOnes(nums):
    # our approach is going to be to use two pointers
    # left pinter starts at 0 index
    # right pointer iterates dowen throiugh array
    # check to see if number is a 1. if it is, then increment the right pointer until you reach a number thats not a 1

    l, output = 0,0

    for r,n in enumerate(nums):
        if n==0:
            l =r + 1
        output = max(output, r -l + 1)
    return output