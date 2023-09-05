# NOTE : For me, in Leetcode, this turned out to be Time Limit Exceeded, not sure why?, but this is the
# proposed solution on Neetocde
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        """
        To solve this problem without using sorting - we will use QuickSelect Algo
        - which is similar to quick sort algo

        Concept?
        - partitioning the array - using pivot, p, left and right pointers
        - pivot? - choosing the right most element value
        - p? - indicator-left most index
        - in the end swap the pivot with p
        - In place sorting

        """

        # Finding the index - where the Kth largest locates
        k = len(nums) - k

        # quick select function
        def quickSelect(left, right):

            # initialize pivot - right most Value
            pivot = nums[right]

            # initialize p (start indicator) - left most INDEX
            p = left

            # loop through array
            for i in range(left, right):

                # compare the nums[i] with pivot - if smaller - swap with nums[p]
                # making sure the at a certian point - everything left to pivot is smaller
                # and everything right to pivot is greater
                if nums[i] <= pivot:
                    # in python we can do swaping without swaping helper
                    nums[p], nums[i] = nums[i], nums[p]

                    # increment the p-indicator
                    p += 1

            # At last, swap the pivot with p-indicator value
            nums[p], nums[right] = pivot, nums[p]

            # keep calling this quick select recursively
            if p > k:
                return quickSelect(left, p - 1)
            elif p < k:
                return quickSelect(p + 1, right)
            else:
                # if p-indicator = k -> we've reached the solution
                return nums[p]

        return quickSelect(0, len(nums) - 1)
