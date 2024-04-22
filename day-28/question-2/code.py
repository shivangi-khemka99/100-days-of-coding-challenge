# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # Find the intersection point of the two pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No cycle

        # Move one pointer back to the head
        slow = head

        # Move both pointers at the same pace until they meet again
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # Return the node where the cycle begins