# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next if head else None
        while fast and fast.next:
            if fast.val != slow.val:
                slow.next = fast
                slow = fast
            fast = fast.next
        if slow and fast:
            if slow.val == fast.val:
                slow.next = None
            else:
                slow.next = fast
        return head