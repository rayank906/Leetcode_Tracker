class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack:
                stack.append(ast)
            else:
                if stack[-1] > 0 and ast > 0:
                    stack.append(ast)
                elif stack[-1] < 0:
                    stack.append(ast)
                else:
                    while stack and stack[-1] > 0 and abs(ast) > stack[-1]:
                        stack.pop()
                    if not stack or stack[-1] < 0:
                        stack.append(ast)
                    elif stack[-1] == abs(ast):
                        stack.pop()
        return stack


"""
    1. use a stack for the asteroids
    2. loop through asteroids
    3. if stack empty, if curr asteroid is negative, ignore else append to stack
    4. if stack[-1] is positive, if curr ast positive, append to the stack
            if negative, while mag(curr ast) > stack[-1] and stack
            pop the element
            if not stack, append curr ast
    5. if stack[-1] negative, append the element
    6. return stack
"""
        