from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for object in tokens:
            if object == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif object == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif object == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif object == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(object))
        return stack[0]


inputList = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
sol = Solution()
print(sol.evalRPN(inputList))
