# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        if not head or not head.next:
            return head
        prev,cur = dummy, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        dummy.next,head.next = None,None
        return prev
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = self.reverseList(head)
        prev,cur,carry = ListNode(0,new_head),new_head,0
        while cur:
            ans = (cur.val * 2) + carry
            cur.val = ans % 10
            carry = ans // 10
            prev = cur
            cur = cur.next
        if carry == 1:
            prev.next = ListNode(1,None)
        return self.reverseList(new_head)