# Technique : HASHMAP {key:value} -> {value:index}
class Solution:

    def fetchIndices(self, nums, target):
        indexMap = {}

        for i in range(len(nums)):
            value = target - nums[i]

            if value in indexMap:
                return [indexMap[value], i]

            indexMap[nums[i]] = i

        return


def main():
    solver = Solution()
    print(solver.fetchIndices([2, 7, 11, 15], 18))


if __name__ == "__main__":
    main()
