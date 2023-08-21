class Solution:

    def isValid(self, string):
        stack = []  # Last in first out data structure

        # mp to store the matching open symbol for every closing symbol
        # k:v pair    --> closing symbol : opening symbol
        symbolMap = {")": "(", "}": "{", "]": "["}

        # loop through every character in the string
        for char in string:

            # First check if the char is closing symbol or opening symbol
            if not char in symbolMap:
                # if it is an opening symbol -> add it to the stack
                stack.append(char)
                continue

            # if it did not go through the condition -> then it is a closing symbol
            # Check if the closing symbol is matching or not with its respective opening symbol
            # If not -> return False
            if not stack or stack[-1] != symbolMap[char]:
                return False

            # if yes -> pop the char from the stack
            stack.pop()

        # in the end -> if the stack is empty -> it indicates the string is valid, if not -> the string is not valid
        return not stack


def main():
    solver = Solution()
    print(solver.isValid("()[]{}"))
    print(solver.isValid("(]"))


if __name__ == "__main__":
    main()
