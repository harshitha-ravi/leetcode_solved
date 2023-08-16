# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Time : O(n) ; Space : O(1)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        i = len(s) - 1
        count = 0

        # This loop checks for any white spaces in the end of the string
        while s[i].isspace():
            i -= 1

        # until we encounter whitespace we keep track of the count of the charcaters, that will be the length of the
        # last word
        while i >= 0 and not s[i].isspace():
            count += 1
            i -= 1

        print(count)

        return count


def main():
    solution = Solution()
    # test cases
    solution.lengthOfLastWord("Hello World")
    solution.lengthOfLastWord(" Catch me if you can  ")


if __name__ == "__main__":
    main()
