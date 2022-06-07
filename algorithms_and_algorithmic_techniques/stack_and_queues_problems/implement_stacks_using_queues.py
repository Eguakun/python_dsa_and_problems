# When implementing a stack using a queue, you have the 4 operations:
    # - void push(int x) --> same for both stack and queue, we add to the right side of the array or back of the line.
    # - int top() --> same for both stack and queue, we just return the value at the right end of the array or the back of the line.
    # - boolean empty() --> same for both just check if len is 0
    # - int pop() --> with a stack, you pop from the right side of the array or back of the line
                # --> with a queue, you pop from the left side of the array or the front of the line.

# the algorithm here is to iterate through the array and append each value that we touch to the end of the line
# up until we get to the last value in the array. When we get to the last value, we remove, pop, return the last value
# the stack functionality has now been implemented with a queue.


# time complexity of this algorithm is O(n) where n is the number of values in the array since we have to iterate
# through to every value until the end.

class MyStack:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self):
        for i in range(len(self.q) - 1):
            self.q.append(self.q.pop(0))
        return self.q.pop(0)

    def top(self):
        return self.q[-1]

    def empty(self):
        return len(self.q) == 0




