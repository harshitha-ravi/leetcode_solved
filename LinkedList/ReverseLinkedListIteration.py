"""
EASY

Problem --> Given a head of the LL, reverse the LL (LinkedList)

Technique --> For Iterative method, use two pointers : curr and prev

Goal --> is to reverse the list, keep updating the curr.next in each iteration. And forward the curr and next piinters by one step each

Time Complexity : O(n)
Space Complexity : O(1)

Companies : Google, Facebook

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
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

    def reverseLinkedList(self, head):
        prev, curr = None, head

        # we need two pointers -> curr, and prev ---> these two pointers just keep moving by one step in each iteration

        # we will loop until curr is null (use while loop)
        while curr:
            # First store the next in a temp variable
            tempNext = curr.next

            # Now, set the next pointer of the node to it's previous pointer -> this is the main goal in reversing
            # the LL. It will be set to its previous node (prev value)
            curr.next = prev

            # Update the curr and next pointers by one step ahead each
            prev = curr
            curr = tempNext

        # In the end, the prev pointer will be pointing to te new head of our reversed
        # We are returning the listNode
        return prev


def main():
    solver = Solution()
    # Create an instance of LinkedList
    linked_list = LinkedList()

    # Append elements to the linked list
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    print(solver.reverseLinkedList(linked_list.head).val)


if __name__ == "__main__":
    main()
