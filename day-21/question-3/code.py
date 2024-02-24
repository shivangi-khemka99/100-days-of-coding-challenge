# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = k
        dummy = ListNode(0, head)
        l, r = dummy, dummy
        while n > 0:
            r = r.next
            n-=1
        temp = r
        while r:
            l = l.next
            r = r.next
        l.val, temp.val = temp.val, l.val
        return head