"""
EASY

Problem --> Given two trees root and subRoot, check subRoot is a subTree of root

Technique
        # To solve this problem we will break it into two sub problems
        # subTree and sameTree
        # We will make use of the helper function -> sameTree
        # Given : root and subRoot are the two binary trees given

        # The high level logic :
        # First -> Take care of the edge cases
        # Edge case 1: if subRoot  is null -> return true : because empty tree is subtree of given tree
        # Edge case 2: if root is null -> return False : because vice versa of the above is not true
        # Case 3: if both are non-null -> we check if both are same? if it returns true -> return True
        # Case 4 : if the above does not return true -> Check if subRoot is a subTree of root
        # Note : It should be subtree of either the left or right subtree of root

Goal --> is a subTree?

Time Complexity : O(p * q) - p and q is the size of the tree
Worst case will be -> when we end up traversing the entire tree

Companies : Amazon

"""
from typing import Optional


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # Edge case 1 : if subRoot  is null -> return true : because empty tree is subtree of given tree
        if not subRoot:
            return True

        # Edge case 2 : if root is null -> return False : because vice versa of the above is not true
        if not root:
            return False

        # Case 3:  if both are non-null -> we check if both are same? if it returns true -> return True
        if self.isSameTree(root, subRoot):
            return True

        # Case 4: Check if the subRoot is either the subtree of left or right subtree of root
        # Hence -> OR condition
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    # We already know how to solve this sub problem
    def isSameTree(self, p, q):

        # We will have multiple edge cases here

        # first - if both the roots are null -> then return true
        if not p and not q:
            return True
        # in the second case -> check if both are non-null and their value is same
        # if this is the case -> then -> call the function recursively
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # else -> this is the part where either of them is null -> should return false
        # As there's a mismatch in the structure
        else:
            return False
