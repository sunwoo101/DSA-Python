class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()

        i = 0

        for c in s:
            i += 1
            if c == '(' or c == '{' or c == '[':
                stack.push(c)
            elif c == ')':
                if stack.peek() != '(':
                    return False
                stack.pop()
            elif c == '}':
                if stack.peek() != '{':
                    return False
                stack.pop()
            elif c == ']':
                if stack.peek() != '[':
                    return False
                stack.pop()

        return stack.peek() == "Stack is empty"


solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("([])"))
print(solution.isValid("([)]"))
