class Solution:
    def performOp(self, op: str, num1: int, num2: int) -> int:
        if op == "+":
            return str(num2 + num1)
        elif op == "-":
            return str(num2 - num1)
        elif op == "/":
            if num2 / num1 < 0:
                return str(math.ceil(num2 / num1))
            return str(num2 // num1)
        else:
            return str(num2 * num1)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in range(len(tokens)):
            if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "/" or tokens[i] == "*":
                stack.append(self.performOp(tokens[i], int(stack.pop()), int(stack.pop())))
            else:
                stack.append(tokens[i])
        return int(stack.pop())


"""
    stack push/pop solution
    1. have a stack of integers
    2. loop through tokens and push if its a number
    3. when we encounter a symbol, pop the last two elements and perform the operation
    4. push the res of operation back in the stack and keep looping

    Edge cases:
        are we sure rpn is valid?
        can a list of 1 contain an op?
    
    O(n) time and O(n) space
"""