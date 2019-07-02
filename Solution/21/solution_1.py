# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l = l1
            l1 = l1.next
        else:
            l = l2
            l2 = l2.next
        ll = l
        while l1 or l2:
            if l1 is None:
                ll.next = l2
                break
            if l2 is None:
                ll.next = l1
                break
            if l1.val < l2.val:
                ll.next = l1
                l1 = l1.next
            elif l2.val <= l1.val:
                ll.next = l2
                l2 = l2.next
            ll = ll.next
        return l