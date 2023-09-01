"""
EASY

Problem --> Given a Binary Tree, Find if the height is balanced
            height balanced tree - depth of the 2 subtrees of every node never defers by more than 1

Technique --> Thi requires two things, at each recursive step, we compute both the balanced boolean variable and height
          - starting from the bottom
          - BOTTOM - UP APPROACH
          - Base case - if the root is null -> the height of the tree is considered as 0 and balanced
          - find the left and right height
          - balanced :
            # to make sure it is balanced - we check three things here
            # 1 - left subtree should be balanced
            # 2 - right subtree should be balanced
            # 3 -  present node should be balanced

          - height = 1 + max(left, right)

Goal --> Find whether it is balanced or not

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

    def isBalanced(self, root):
        def dfs(root):

            # base case
            if not root:
                return [True, 0]
                # meaning - if it hits the nul tree, height is 0 and tree is balanced

            # compute left and right subtree height using dfs - recursively call
            left = dfs(root.left)
            right = dfs(root.right)

            # compute the variable balanced
            # to make sure it is balanced - we check three things here
            # 1 - left subtree should be balanced
            # 2 - right subtree should be balanced
            # 3 -  present node should be balanced
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <=1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

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
    maxDepth = solver.isBalanced(root)
    print(maxDepth)


if __name__ == "__main__":
    main()
