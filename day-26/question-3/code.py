# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        res_head = ListNode()
        res = res_head

        while head and head.next:
            if head.val == 0:
                head = head.next
                continue

            summ = 0
            while head and head.val != 0:
                summ += head.val
                head = head.next

            res.next = ListNode(summ)
            res = res.next

        return res_head.next