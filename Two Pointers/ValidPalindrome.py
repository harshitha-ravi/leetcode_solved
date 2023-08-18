"""
Problem : Given a string  -> return true if it is palindrome, else return false \
conditions: do not consider - non-alphanumeric chars, case-insensitive

Technique: Two pointers, ord() function to fetch ASCII values
Time : O(n)  Space: O(1)

Beware if array index out of bound exceptions : add valid checks -: l<r, r>l

"""


class Solution:
    def isPalindrome(self, string):
        # initialize the pointers
        left, right = 0, len(string) - 1

        while left < right:
            # Check for non-alphanumeric characters (use loop)
            # Keep track of the pointers -> to avoid array index out of bound exceptions
            while left < right and not self.isAlphanum(string[left]):
                left += 1

            while right > left and not self.isAlphanum(string[right]):
                right -= 1

            # check if the characters doesn't match -> then return False
            if string[left].lower() != string[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def isAlphanum(self, char):
        """
        This function checks if the given character lies in the required ASCII range [A-Z] [a-z] [0-9]

        ord is the function to Python to fetch ASCII values

        :param char:
        :return:
        """
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z')
                or ord('0') <= ord(char) <= ord('9'))


def main():
    solver = Solution()
    print(solver.isPalindrome("A man, a plan, a canal: Panama"))
    print(solver.isPalindrome("race a car"))


if __name__ == "__main__":
    main()
