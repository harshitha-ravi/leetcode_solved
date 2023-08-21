"""
Problem --> Given a string, return the length of the longest substring --> return the max length

Technique --> Sliding Window -> Two Pointers (left and right)

Looping strategy --> Iterate through each character

Additional DS --> HashSet (to identify duplicates)

Identify the Window --> substring : represented with left pointer

Based on the condition --> either shrink the window or update the solution

Goal --> Need to return max length
         2 variable strategy -> local and global max
"""

class Solution:
    def fetchMaxLengthSubstring(self, string):

        # define the window
        left = 0

        # define the max variable
        maxLength = 0

        # define the charSet
        charSet = set()

        # right pointer
        for right in range(len(string)):

            # based on the condition -> either update the window or update the solution
            while string[right] in charSet:
                # If a duplicate is found -> shrink the window from the left
                # continue to shrink until there exists a duplicate -> hence a while loop
                charSet.remove(string[left])

                # increment the left pointer
                left += 1

            # if not present in charSet -> add it
            charSet.add(string[right])
            # compute the max length
            maxLength = max(maxLength, right - left + 1)

        return maxLength


def main():
    solver = Solution()
    print(solver.fetchMaxLengthSubstring("abcabcbb"))


if __name__ == "__main__":
    main()
