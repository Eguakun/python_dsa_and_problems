# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:
            # every key is always a closing parentheses
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
                # if we get an open parentheses
            else:
                stack.append(c)
        return True if not stack else False


