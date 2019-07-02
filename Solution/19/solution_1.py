# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 1
        head_copy = head
        while head_copy.next:
            head_copy = head_copy.next
            length += 1
        if length == n:
            return head.next
        head_copy = head
        for i in range(length):
            if length - i - 1 == n:
                head_copy.next = head_copy.next.next
                break
            head_copy = head_copy.next
        return head