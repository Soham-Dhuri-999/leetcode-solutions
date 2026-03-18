# Question: Given the head of a singly linked list, reverse the list and return its head.
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        prev = None

        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node

        return prev
