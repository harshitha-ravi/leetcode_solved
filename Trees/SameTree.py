"""
EASY

Problem --> Given two trees, check if they are same -> meaning -> their structure and each node val should be same

Technique --> We can solve this by thinking of multiple base cases and edge cases
         ---> # first - if both the roots are null -> then return true
         ---> # in the second case -> check if both are non-null and their value is same
              # if this is the case -> then -> call the function recursively
         ---> # else -> this is the part where either of them is null -> should return false
              # As there's a mismatch in the structure

Goal --> if Same?

Time Complexity : O(p +  q) - Where both tree nodes are traversed once
Worst case will be -> when we end up traversing the entire tree

Companies : Amazon

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

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
