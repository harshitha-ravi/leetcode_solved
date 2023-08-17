import collections


# HashMap, HashSet -> to check duplicates
# Time: O(9^2) Space: O(n)
# Can't solve it in linear time, as it's a matrix -> need to use nested loops

# Hint : 3 HashMaps to store row, col, and square grid values ;
# Values stored as HashSet -> to validate Duplicates


class Solution:

    def isValid(self, nums):
        # here nums is 2d array (or can be a list(list("str")

        # First step -> we need 3 data structures to store the row, column and 3*3 grid elements
        # 3 HashMaps (key -> row index, column index, value -> HashSet (row values, column values)
        row = collections.defaultdict(set)  # creating a default dict with the default value as empty set
        column = collections.defaultdict(set)

        # Logic to identify 3*3 grid -> divide the row or column index value by 3
        # key -> (r/3, c/3)
        square = collections.defaultdict(set)

        # looping through the matrix; range 9 -> sudoku board

        for r in range(9):
            for c in range(9):

                if nums[r][c] == ".":  # check for the unfilled blocks in the board represented by "."
                    continue

                # if the board value is already contained either in th e row, col or the square grid -> return false
                if nums[r][c] in row[r] or nums[r][c] in column[c] or nums[r][c] in square[(r // 3, c // 3)]:
                    return False

                # If not present add it to the set
                row[r].add(nums[r])
                column[c].add(nums[c])
                square[(r // 3, c // 3)].add(nums[r][c])

        return True


def main():
    solver = Solution()


if __name__ == "__main__":
    main()
