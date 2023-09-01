"""
EASY

Problem --> Given a Binary Tree, IFind the max depth of the tree

Technique --> Max depth is defined the long path from the root, either left or right


Goal --> Find the max depth

Time Complexity : O(n) - Because each node is visited only once

Companies : Amazon

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root):
        # Recursive DFS Approach
        # We will solve this problem using recursion:
        # Base case: check if the root is null -> if yes return 0
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

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
    def construct_tree(self, elements):
        root = None
        for element in elements:
            root = self.insert(root, element)
        return root

    def preorder_traversal(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)


def main():
    solver = Solution()
    elements = [3, 9, 20, 15, 7]
    root = solver.construct_tree(elements)
    maxDepth = solver.maxDepth(root)
    print(maxDepth)


if __name__ == "__main__":
    main()
