"""
Problem : Enhanced version of Two Sum
Given : Sorted array
Conditions -> no extra space

Technique : Two pointers, left (start from beginning) and right(start from end)
- pointer operations : left: increment , right : decrement
- Leverage the fact that the array is sorted,

- When to increment or decrement?
- when sum > target  --> decrement
- when sum < target  --> increment

Code Word : Fine-tuning the pointers in sorted array

"""


class Solution:

    def fetchIndices(self, nums, target):

        # defining two pointers left and right
        left, right = 0, len(nums) - 1

        while left < right:
            # add the values of left and right pointers
            value = nums[left] + nums[right]

            # leverage that the array is sorted -> if value > target  decrement the right pointer
            if value > target:
                right -= 1
            # if value < target  increment the left pointer
            elif value < target:
                left += 1
            else:
                return [left + 1, right + 1]


def main():
    solver = Solution()
    print(solver.fetchIndices([2, 7, 11, 15], 9))


if __name__ == "__main__":
    main()
