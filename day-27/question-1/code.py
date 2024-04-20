class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Find the middle of the list
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev = None
        temp = slow.next
        slow.next = None
        while temp:
            next_temp = temp.next
            temp.next = prev
            prev = temp
            temp = next_temp

        # Merge the first half and the reversed second half
        first_half, second_half = head, prev
        while second_half:
            next_first = first_half.next
            next_second = second_half.next
            first_half.next = second_half
            second_half.next = next_first
            first_half = next_first
            second_half = next_second