"""
Problem --> Given an array of prices simulating the stock market scenario -->
return the max profit that can be made

Condition -->buy on one day, sell on other day. Should buy first -> in order to sell

Technique --> Sliding Window -> Two Pointers (left and right)

Looping strategy --> Iterate through each item

Identify the Window --> minimum buying price : minCP

Based on the condition --> either slide/shrink the window or update the solution

Goal --> Need to return  max Profit
         2 variable strategy -> local and global max
"""


class Solution:

    def getMaxProfit(self, prices):
        # window variable
        minCP = prices[0]

        # variable to hold the max profit
        maxProfit = 0

        for price in prices:

            # 2 steps here : based on the condition either update the window or update the solution
            if price < minCP:
                # update the window -> if the current price is less than minCP
                minCP = price
            else:
                # else -> update the solution
                maxProfit = max(maxProfit, price - minCP)

        return maxProfit


def main():
    solver = Solution()
    print(solver.getMaxProfit([7, 1, 5, 3, 6, 4]))


if __name__ == "__main__":
    main()
