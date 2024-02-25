# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        cur = dummy.next 
        prev = dummy
        while cur and cur.next:
            tempA = cur.next
            tempB = cur.next.next
            prev.next = tempA
            tempA.next = cur
            cur.next = tempB
            prev = cur
            cur = cur.next
        return dummy.next