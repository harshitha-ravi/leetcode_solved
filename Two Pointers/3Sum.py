"""
Extended version of Two Sum II

Given an array, return the triplets that sum up to zero. No duplicate triplets allowed

Hint : Break down the problem to Two Sum
-> to break it down to 2 sum -> sort()

a + b + c = 0

2 loops, external loop for the element a
inner while loop for two sum -> for b and c (left and right pointers) same  concept as two sum

inside this loop -> in the end -> need to increment left pointer (no need to increment right)
"""


class Solution:

    def findThreeSum(self, nums):

        # First step : sort the array
        nums.sort()

        # defining a result array
        result = []

        for i, a in enumerate(nums):

            # check if the array element is same as the previous element, if yes, then skip (don't want duplicate
            # sequences. Whenever adding¬ condition w.r.t neighbour values (in this case previous value) -> add
            # necessary checks i> 0
            if i > 0 and a == nums[i - 1]:
                continue

            # Finding b and c --> problem is now reduced to Two sum problem
            # initialize left and right pointers
            left, right = i + 1, len(nums) - 1

            while left < right:

                threeSum = a + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    # increment the left pointer (no need to increment the right pointer)

                    # and keep on checking if the current value is same as previous value -> in that case we need to
                    # again increment the left
                    # use the while loop -> not if (THINK)
                    # whenever adding condition w.r.t two pointers -> add necessary checks left < right
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result


def main():
    solver = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(solver.findThreeSum(nums))
    print(solver.findThreeSum([0, 0, 0]))


if __name__ == "__main__":
    main()
