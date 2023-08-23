"""
EASY

Problem --> Given an array nums, and target ---> return index of the target if found, else return -1

Technique --> Binary Search, left and right pointers, keep recalculating mid -> until the target found)

Goal --> Search

Time Complexity : O(log n)  (mathematical way of O(log base 2 N) : How many times n can be divided by 2)

Companies : Microsoft

"""


class Solution:

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
                return mid

        # if the search is unsuccessful return -1
        return -1


def main():
    solver = Solution()
    print(solver.binarySearch([-1, 0, 3, 5, 9, 12], 9))


if __name__ == "__main__":
    main()
