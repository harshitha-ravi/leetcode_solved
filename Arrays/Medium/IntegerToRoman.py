# Given an integer -> need to convert it to the roman value

class Solution:
    def convert(self, num):
        # create a 2d list to store the reference values
        # Note: Adding the additional 6 instances for 4,9,40,90,400 and 900
        symbolList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                      ["C", 100], ["CD", 400], ["D", 500],
                      ["CM", 900], ["M", 1000]]

        result = ""

        # Looping through the symbolList in a reversed order
        for symbol, value in reversed(symbolList):
            # This condition checks which digit placement we need to refer to, proceeds only when the quotient is not 0
            # That mean for the number 58 -> it just has tens place and units place
            if num // value:
                # Gives the count of how many occurences of the symbol do we need
                count = num // value

                result += (symbol * count)  # string concatenation

                # updating the num, to the remaining value (moving left to right in the digit system 1000, 100, 10,
                # 1 places)
                # Stopping criteria -> we stop when all the digits have been touched -> when num = 0
                num = num % value

        return result


def main():
    solver = Solution()
    print(solver.convert(1994))


if __name__ == "__main__":
    main()
