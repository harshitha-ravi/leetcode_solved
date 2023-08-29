"""
EASY

Problem --> Given a Binary Tree, Invert it

Technique --> Visit each node, swap the left and right children with each other
              Recursion -> base case ? -> if root not null (if not root)
              DFS Strategy applied


Goal --> Invert the tree

Time Complexity : O(n) - Because each node is visited only once

Companies : Google

Trivia : This problem was inspired the original tweet from Max Howell (Max Howell, the creator of the Homebrew
package manager for macOS.) :
"Google: 90% of our engineers use the software you wrote (Homebrew), but you can't
invert a binary tree on white board, so f*** off"

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root):
        # We will solve this problem using recursion:
        # Base case: check if the root is null -> if yes return None
        if not root:
            return None

        # swap left and right child
        temp = root.left
        root.left = root.right
        root.right = temp

        # Applying DFS - make recursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

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
    elements = [4, 2, 7, 1, 3, 6, 9]
    root = solver.construct_tree(elements)
    root = solver.invertTree(root)
    solver.preorder_traversal(root)


if __name__ == "__main__":
    main()
