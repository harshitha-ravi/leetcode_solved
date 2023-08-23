class Solution:
    def fetchMaxLength(self, string, k):

        # left pointer -> starting from the 0th index
        left = 0

        # max variable
        maxLength = 0

        # variable to store k
        k_temp = k

        # right pointer traversing through the entire string
        for right in range(len(string)):

            if string[right] != string[left]:

                if k_temp == 0:
                    # reassign the right index value to left
                    left = right

                    # reset the k_temp  value
                    k_temp = k

                else:
                    # if not keep computing the maxLength and decrement the k_temp
                    k_temp -= 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength


def main():
    solver = Solution()
    print(solver.fetchMaxLength("AABABBA", 1))


if __name__ == "__main__":
    main()
