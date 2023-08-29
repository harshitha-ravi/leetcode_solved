class Solution:
    def findDuplicate(self, nums):

        # taking two pointers
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            # break when these two pointers intersect
            if slow == fast:
                break

        # taking second slow pointer
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


def main():
    solver = Solution()
    print(solver.findDuplicate([1, 3, 4, 2, 2]))


if __name__ == "__main__":
    main()
