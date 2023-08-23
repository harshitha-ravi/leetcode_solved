"""
MEDIUM

Problem --> Given a 2D array matrix, and target ---> return True if target  found, else return False

Technique --> Binary Search, left and right pointers, keep recalculating mid -> until the target found)

Goal --> Search

Time Complexity : O(log m) + O(log n) = O(log m.n)
 ---> break down :
      finding which row? --> O(log m)
      Actual binary search on the row --> O(log n)

Companies : Microsoft

Optimized approach

"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        # finding the row
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        # if none found -> return false
        if not (top <= bot):
            return False

        # if the row is picked -> perform the actual binary search on it
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


def main():
    solver = Solution()
    print(solver.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))


if __name__ == "__main__":
    main()
