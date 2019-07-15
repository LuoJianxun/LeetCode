# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        res = head.next
        while head:
            if head.next:
                node = head.next
                temp = node.next
                node.next = head
                if temp is None:
                    head.next = temp
                elif temp.next is None:
                    head.next = temp
                    head = temp
                else:
                    head.next = temp.next
                    head = temp
            else:
                break

        return res
