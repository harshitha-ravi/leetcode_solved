"""
EASY

Problem --> Given a Binary Tree, Find the diameter of the tree (longest path between two nodes -may or may not be through the root node)

Technique --> Thi requires two things, at each recursive step, we compute both the diamter and the height
          - starting from the bottom
          - fetching diameter and height
          - Base case - if the root is null -> the height of the tree is considered as -1 for null tree
          - find the left and right height
          - diameter = left height + right height + 2 ( to support with the math we have for -1)
          - height = 1 + max(left, right)
          - keep updating the result max variable in each recursive step

Goal --> Find the max depth

Time Complexity : O(n) - Because each node is visited only once

Companies : Google

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameter(self, root):
        # Recursive DFS Approach We will solve this problem using recursion: Base case: check if the root is null ->
        # return the height as -1, because height of a node is considered 0, for null tree it is -1

        res = 0

        def dfs(root_elem):
            nonlocal res

            # Bottom up approach
            if not root_elem:
                return -1

            # find the height of left tree - suing DFS approach
            left = dfs(root_elem.left)
            right = dfs(root_elem.right)

            # compute the diameter
            res = max(res, 2 + left + right)

            # return height in each recursive call
            return 1 + max(left, right)

        dfs(root)
        return res

    # additional set of methods to insert elements into the tree and tree traversal

    def insert(self, root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    # construct tree from the list of elements
    # def construct_tree(self, elements):
    #     root = None
    #     for element in elements:
    #         root = self.insert(root, element)
    #     return root
    def construct_tree(self, preorder):
        def helper(lower=float('-inf'), upper=float('inf')):
            nonlocal index
            if index == len(preorder):
                return None

            value = preorder[index]
            if value < lower or value > upper:
                return None

            index += 1
            node = TreeNode(value)
            node.left = helper(lower, value)
            node.right = helper(value, upper)

            return node

        index = 0
        return helper()

    def preorder_traversal(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)


def main():
    solver = Solution()
    elements = [1,2,3,4,5]
    root = solver.construct_tree(elements)
    diameter = solver.diameter(root)
    print(diameter)


if __name__ == "__main__":
    main()
