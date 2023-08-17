# Given an array -> return the length of the longest consecutive sequence
"""
1 - Consecutive -> in order, in sequence (1,2,3,4)
2 - Challenge here is -> O(n) time, not to use sorting

3 - Hint: Use HashSet -> convert the array to set
4 - Observe the patterns ->  Grab the tails of the start point of the sequence (value-1) -> doesn't exist in set
5- Once you grab the tail of the sequence -> check if the next numbers are there (value + 1) is in set
6 - have two variables length and longest (whenever you  need to decide the longest amongst 3-4 choices -> you will need two variables)
 i.e. local and global
"""


class Solution:
    def getLongestConsecutiveSequence(self, nums):

        valueSet = set(nums)  # convert to set

        longestLength = 0  # variable to define the longestLength

        for value in nums:

            # grab the tail of the sequence
            if (value - 1) not in valueSet:

                length = 1

                # add it with the length and not 1 (because it will enter infinite loop)
                while (value + length) in valueSet:
                    length += 1

                longestLength = max(length, longestLength)

        return longestLength


def main():
    solver = Solution()
    print(solver.getLongestConsecutiveSequence([100, 4, 200, 1, 3, 2]))


if __name__ == "__main__":
    main()
