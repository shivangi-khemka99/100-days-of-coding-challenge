# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        tail, n = head, 1
        while tail.next:
            tail = tail.next
            n+=1
        
        k= k%n
        if k==0:
            return head
        cur = head
        for i in range(n-k-1):
            cur = cur.next
        
        temp = cur.next
        cur.next = None
        tail.next = head
        head = temp

        return head