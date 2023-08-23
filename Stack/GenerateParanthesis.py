"""
MEDIUM

Problem --> Given n set of parentheses, generate all possible combination of parentheses

Condition --> should be valid

Technique --> Recursion, Backtracking, Stack

Recursion --> base case, conditions (where you call the function again)

Stack operations -->
   push : "(" {when openN < n} and ")" {when closeN < openN} --> upon valid conditions
   pop : for cleanup

Goal --> Generate all possible valid combination of parentheses

Companies : Amazon

"""


class Solution:

    def generateParanthesis(self, n):

        # This problem will be solved using recursion and backtracking technique

        stack = []
        res = []  # result array

        # writing another function to recurse
        def backtrack(openN, closedN):

            # first step in recursion is to define:
            # base case
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # 1st condition
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()  # debug --> why?

            # This is the tricky logic here
            # At any given point while pushing to stack --> the closed count should be less than open ->
            # then only we can insert the closed parentheses
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()  # debug --> why?

        backtrack(0, 0)
        return res


def main():
    solver = Solution()
    print(solver.generateParanthesis(2))


if __name__ == "__main__":
    main()
