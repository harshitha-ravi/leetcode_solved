"""
Problem Level: HARD
Problem : Given an array of heights, that define the elevation map (visual imagination), compute
 the total water blocks that can be captured

Technique --> Two Pointers (left and right) + additional variables to store leftMax and rightMax

Looping strategy --> while left < right

Pointers fine-tuning strategy -->
            Note: left will always increment, right will always decrement
            1- Comparison strategy ? : height[left] and height[right] values against each other
            2- Why against each other? : Because no other third party value
            3- When to increment left ? : height[left] < height[right]
            4- When to decrement right ? : height[left] >= height[right]

Goal --> Need to calculate the total water blocks captured
    --> Keep updating leftMax and rightMax values
    Hint --> water-blocks  += leftMax - height[left]  (same with right)
"""


class Solution:
    def trapRainWater(self, height):

        # checking the base case -> if the height array is empty -> then return 0
        if not height:
            return 0

        # variable to capture the blocks of water captured
        waterBlocks = 0
        # defining the left and right pointers
        left, right = 0, len(height) - 1

        # defining 2 additional pointers:  leftMax and the rightMax (keeps track of the max left and right pointer
        # values ta nay given point of time
        leftMax = height[left]
        rightMax = height[right]

        # Looping strategy : left < right
        while left < right:

            # fine-tuning strategy, comparison strategy (left < right) --> increment left else --> decrement right
            if height[left] < height[right]:
                left += 1

                # Update the leftMax pointer Note : doing this step right before calculating water-blocks -> will
                # always lead in a positive difference
                leftMax = max(height[left], leftMax)

                # calculate the water-blocks
                # logic : water-blocks = leftMax-height[left]
                waterBlocks += leftMax - height[left]

            else:
                right -= 1

                # update the rightMax pointer
                rightMax = max(height[right], rightMax)

                # calculate the water-blocks
                # logic : water-blocks = rightMax-height[right]
                waterBlocks += rightMax - height[right]

        return waterBlocks


def main():
    solver = Solution()
    print(solver.trapRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


if __name__ == "__main__":
    main()
