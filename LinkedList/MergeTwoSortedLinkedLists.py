"""
EASY

Problem --> Given two sorted LLs - merge it

Technique --> loop through both LLs and add it accordingly to a dummy node (separate LL)

Goal --> merge

Time Complexity : O(n)


Companies : Microsoft

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


class Solution:

    def merge(self, l1, l2):

        # create a dummy node - to create the output linked list
        dummy = ListNode()

        # assign the dummy to a temp pointer - Why?
        temp = dummy

        # loop only until both l1 and l2 are non-empty
        while l1 and l2:

            # comparison between the two LLs
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next

            # update the temp pointer
            temp = temp.next

        # once the loop is done, check for the edge cases - where any of the items is left in either l1 or l2
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2

        return dummy.next


def main():
    solver = Solution()
    # Create an instance of LinkedList
    l1 = LinkedList()

    # Append elements to the linked list
    l1.append(10)
    l1.append(20)
    l1.append(30)

    l2 = LinkedList()

    # Append elements to the linked list
    l2.append(10)
    l2.append(40)
    l2.append(50)
    l2.append(60)
    l2.append(70)

    print(solver.merge(l1.head, l2.head))


if __name__ == "__main__":
    main()
