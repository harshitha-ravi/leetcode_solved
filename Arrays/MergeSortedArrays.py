class Solution:
    def mergeSortedArray(self, nums1, nums2, m, n):

        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k = k - 1
                i = i - 1
            else:
                nums1[k] = nums2[j]
                k = k - 1
                j = j - 1

        print(nums1)


def main():
    solver = Solution()
    nums1 = [1, 2, 3, 0, 0, 0, 0]
    nums2 = [2, 3, 5, 6]
    solver.mergeSortedArray(nums1, nums2, 3, 4)


if __name__ == "__main__":
    main()
