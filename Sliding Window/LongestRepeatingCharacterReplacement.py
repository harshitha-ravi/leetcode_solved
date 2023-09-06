"""
MEDIUM

Problem --> Given a string and k (where k is the number of replacements that can be done)
        - return the length of the longest substring

Technique --> Sliding window + HashMap for string the count of char
            - left pointer, right pointer, max variable

Goal --> is to reverse the list, keep updating the curr.next in each iteration. And forward the curr and next piinters by one step each

Time Complexity : O(n)
Space Complexity : O(n)

Companies : Google

"""


class Solution:
    def fetchMaxLength(self, s, k):

        count = {}
        res = 0

        # left pointer
        left = 0

        # right pointer -> will traverse the entire string
        for right in range(len(s)):

            # fetch the count for the right pointer value
            count[s[right]] = count.get(s[right], 0) + 1

            # The main idea here is -> in the given window, the replaceable character count should be <= k
            # Because k is the number of times we can perform the replacements
            # If this doesn't satisfy then , we need to shrink the left pointer
            # by decrementing the count of that character by 1
            # and finally increment the left pointer (advance towards right)
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res


def main():
    solver = Solution()
    print(solver.fetchMaxLength("AABABBA", 1))


if __name__ == "__main__":
    main()
