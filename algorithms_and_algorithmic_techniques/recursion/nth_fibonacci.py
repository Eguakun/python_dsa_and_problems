# fib(n) = fib(n - 1) + fib(n - 2) for n>2
# Recursive solution
# Time complexity - lot of unnecessary calculations
# - O(2 ^ n)
# Space complexity - O(n) - taking up space on the call stack

# Recursive with memoization time complexity --> O(n)

# O(2^n) time | O(n) space
# Naive recursive solution:
def getNthFibonacci(n):
    # recursive base case
    if n == 2:
        return 1
    if n == 1:
        return 0
    else:
        return getNthFibonacci(n - 1) + getNthFibonacci(n - 2)

# Memoization recursive solution
def getMemoNthFibonacci(n, memoize={1 : 0, 2 : 1}):
    # recursive base case
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getMemoNthFibonacci(n - 1, memoize) + getMemoNthFibonacci(n - 2, memoize)
        return memoize[n]

# Iterative solution: O(n) time | O(1) space
def getNthFibIterative(n):
    lastTwo = [0,1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]
