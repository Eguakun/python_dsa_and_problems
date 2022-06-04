# Time complexity: O(1)
# space complexity: O(1)
class MinMaxStack:
    def __init__(self):
        # holds min and max values at any point in the stack
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]
