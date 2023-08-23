"""
Problem --> Given an array of tokens in Reversed Polish Notation (operators followed by operands) --> return the result of evaluated expression

Condition --> div by 0 not allowed

Technique --> Stack

Looping strategy --> Loop through each token in the array

Stack operations -->
   push : when operand
   pop : when operator (pop two items) nand perform the respective operation

Goal --> Evaluate the expression

Time Complexity : O(n)
Space Complexity : O(n)

Companies : Amazon

"""


class Solution:

    def evaluateExpression(self, tokens):

        stack = []

        for char in tokens:

            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                # be careful about the order of the subtraction (bottom most elem - top elem)
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                # be careful about the order of the division
                a, b = stack.pop(), stack.pop()
                # rounding off the division to zero using int()
                stack.append(int(b / a))
            else:
                stack.append(int(char))

        # the single element left after evaluating  the  expression is its result, return it
        return stack[0]


def main():
    solver = Solution()
    print(solver.evaluateExpression(["2", "1", "+", "3", "*"]))
    print(solver.evaluateExpression(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))


if __name__ == "__main__":
    main()
