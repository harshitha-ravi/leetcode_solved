# Problem: Remove the given value from the nums [IN-PLACE]
# This has to be done in-place, without using any additional intermediate DS to store the data
# Space complexity = O(1) Time: O(n)

# Hint: Remove ~ consider this as soft delete. POINTER technique
class Solution:

    def removeElement(self, nums, val):

        k = 0  # Take a pointer k

        # the pointer value will be updated only when it's not equal to val
        # val elements are ignored
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


def main():
    solver = Solution()

    # print the results
    print(solver.removeElement([3, 2, 2, 3], 3))


if __name__ == "__main__":
    main()
