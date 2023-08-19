"""
Problem --> Given an array of heights --> return the container with the max water (visual imagination)

Condition --> Slant container scenario not allowed --> as it will spill

Technique --> Two Pointers (left and right)

Looping strategy --> while left < right

Pointers fine-tuning strategy -->
            Note: left will always increment, right will always decrement
            1- Comparison strategy ? : height[left] and height[right] values against each other
            2- Why against each other? : Because no other third party value
            3- When to increment left ? : height[left] < height[right]
            4- When to decrement right ? : height[left] >= height[right]

Goal --> Need to find max area
    Hint --> max among multiple areas -->
    Note: So consider 2 variables (local area and global maxArea)
    maxArea = max(area, maxArea) in each iteration

"""


class Solution:
    def calculateMaxArea(self, height):
        # define the result variable
        maxArea = 0

        # declare two pointers
        left, right = 0, len(height) - 1

        while left < right:
            # to compute area of rectangle = length * breadth here, length is difference between indices -> (
            # right-left) breadth = min(height[left, height[right] --> the reason we take min is, slant container
            # scenario not allowed.
            area = (right - left) * min(height[left], height[right])
            maxArea = max(area, maxArea)

            # Fine-tuning the pointers
            # Fine-tuning strategy
            # Compare the left and right heights against each other - as there is no third party agent (value)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea


def main():
    solver = Solution()
    print(solver.calculateMaxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(solver.calculateMaxArea([1, 1]))


if __name__ == "__main__":
    main()
