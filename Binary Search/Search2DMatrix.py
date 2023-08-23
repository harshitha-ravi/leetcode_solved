"""
EASY

Problem --> Given a 2D array matrix, and target ---> return True if target  found, else return False

Technique --> Binary Search, left and right pointers, keep recalculating mid -> until the target found)

Goal --> Search

Time Complexity :

Companies : Microsoft

My approach

"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):

            if target > matrix[i][-1]:
                continue

            elif target < matrix[i][-1]:
                return self.binarySearch(matrix[i], target)

            else:
                return True

    def binarySearch(self, nums, target):

        # left and right pointers
        left, right = 0, len(nums) - 1

        # Keep traversing until left <= right
        while left <= right:

            # (l + r) // 2 can lead to overflow
            mid = left + (right - left) // 2

            if target < nums[mid]:
                # if target less than mid -> update right pointer
                right = mid - 1
            elif target > nums[mid]:
                # if target greater than mid -> update the left pointer
                left = mid + 1
            else:
                # if target is mid, return true
                return True

        # if the search is unsuccessful return -1
        return False


def main():
    solver = Solution()
    print(solver.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))


if __name__ == "__main__":
    main()
