# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        carry = 0
        while l1 or l2 or carry:
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)            
            val = l1.val + l2.val + carry           
            remainder = val % 10
            result.append(ListNode(remainder))
            carry = 0 if val < 10 else 1
            l1 = l1.next
            l2 = l2.next
        for i in range(len(result) - 1):
            result[i].next = result[i + 1]
        return result[0]
            