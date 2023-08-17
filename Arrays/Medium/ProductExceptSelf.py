# Given a array -> give the product of the array except self. SHould be done in O(n) time
# Time: O(n) Space: O(1)
# prefix-suffix concept -> answer array values = prefix * suffix
class Solution:

    def productExceptSelf(self, nums):

        # initialising result array
        res = [1] * len(nums)

        # 2 loops - for prefix and suffix, using prefix and suffix concept
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]  # updating the prefix

        suffix = 1
        # python syntax to traverse the list from the end
        for i in range(len(nums) - 1, -1, -1):
            # multiplying the already stored prefix in the res array with the suffix to obtain the result at that
            # index position
            res[i] *= suffix
            suffix *= nums[i]

        return res


def main():
    solver = Solution()
    print(solver.productExceptSelf([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
