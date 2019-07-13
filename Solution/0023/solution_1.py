# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = []
        for elem in lists:
            while elem:
                res.append(elem.val)
                elem = elem.next
        res.sort()
        if len(res) == 0:
            return None

        temp0 = ListNode(res[0])
        result = temp0
        for i in range(1, len(res)):
            temp1 = ListNode(res[i])
            temp0.next = temp1
            temp0 = temp1

        return result
