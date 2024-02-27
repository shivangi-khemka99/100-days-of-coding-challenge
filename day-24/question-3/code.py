# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        cur = head.next
        head.next = None  # Break the original list after head
        while cur:
            prev = dummy
            start = dummy.next
            nxt = cur.next 
            while start and start.val < cur.val:
                prev = start
                start = start.next
            
            cur.next = start
            prev.next = cur
            cur = nxt
        return dummy.next