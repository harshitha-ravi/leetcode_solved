"""
EASY

Problem --> Given two LLs with non-negative integers in reversed order - add the numbers and send back the list (head of the result LL)

Technique --> loop through both LLs and add the values,
          --> maintain carry ( sum // 10)
          --> maintain the actual value (sum % 10)
          --> create a dummy result ListNode  and keep adding the next nodes to it to form a result LL¬

Looping strategy : when two LLs : while l1 or l2  (sometimes and - based on condition)
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

    def addTwoNumbers(self, l1, l2):
        # initialise the pointers
        # we need result node
        result = ListNode()
        current = result
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry

            # to compute th carry -> take the quotient obtained from dividing it by 10
            carry = sum // 10
            # to compute the remainder value -> mod by 10 (%10)
            sum = sum % 10

            # create a node with the sum obtaimed and assign it to the next pointer of current
            current.next = ListNode(sum)

            # update the current pointer
            current = current.next

            # updating the l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


def main():
    solver = Solution()
    # Create an instance of LinkedList
    l1 = LinkedList()

    # Append elements to the linked list
    l1.append(2)
    l1.append(4)
    l1.append(3)

    l2 = LinkedList()

    # Append elements to the linked list
    l2.append(5)
    l2.append(6)
    l2.append(4)

    print(solver.addTwoNumbers(l1.head, l2.head))


if __name__ == "__main__":
    main()
