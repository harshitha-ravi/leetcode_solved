# Given a roman value -> parse it into integer value

class Solution:
    def romanToInt(self, s):

        keyMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = 0

        for i in range(len(s)):
            # The logic here is if the value next to the index value is greater, then subtract, else add
            if i < (len(s) - 1) and keyMap[s[i]] < keyMap[s[i + 1]]:
                res -= keyMap[s[i]]
            else:
                res += keyMap[s[i]]

        return res


def main():
    solver = Solution()
    print(solver.romanToInt("MCMXCIV"))


if __name__ == "__main__":
    main()
