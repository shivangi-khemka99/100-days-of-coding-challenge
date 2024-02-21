# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        #Find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #Reverse second half of the linkedlist
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        #Check palindrom
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True