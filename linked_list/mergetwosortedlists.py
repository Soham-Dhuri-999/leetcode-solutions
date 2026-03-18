# Question: Merge two sorted linked lists and return the merged list.
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        c1 = list1
        c2 = list2
        new = ListNode()
        temp = new

        while c1 and c2:
            if c1.val <= c2.val:
                temp.next = c1
                temp = temp.next
                c1 = c1.next
            else:
                temp.next = c2
                temp = temp.next
                c2 = c2.next

        if c1:
            temp.next = c1
        if c2:
            temp.next = c2

        return new.next
