class Solution:
    def calculate(self, s):
        if not s:
            return 0

# we are starting our operator with a plus because
# were going to have a stack to hold our values and allow us to multiply or divide from the top of the stack * curr num
# curr_num to keep track of the current number that were iterating so we can multiply or divide when necessary
# operator will keep track of our current operator so we know what to actually do at each iteration
        stack, curr_num, operator = [], 0, "+"
# have all operators dictionary for instant lookup checks to see if a character is an operator
        all_operators = {"+", "-", "*", "/"}
# a set for insant lookups to see if a character is a number
        nums = set(str(x) for x in range(10))
# iterate through teh string
        for idx in range(len(s)):
    # for each character in the string
            char = s[idx]
    # if the character is a number add it to current number. Doing it this way ensures that if we get another number after this, we will append combine the numbers
            if char in nums:
                curr_num = curr_num * 10 + int(char)
            if char in all_operators or idx == len(s) - 1:

                if operator == "+":
                    stack.append(curr_num)

                elif operator == "-":
                    stack.append(-curr_num)

                elif operator == "*":
                    stack[-1] *= curr_num

                elif operator == "/":
                    stack[-1] = int(stack[-1] / curr_num)

                curr_num = 0
                operator = char
        return sum(stack)
