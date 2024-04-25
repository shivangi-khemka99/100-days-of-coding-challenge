# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return

        final_list = lists[0]

        for i in range(1,len(lists)):
            final_list = self.sortLists(final_list, lists[i])
        return final_list

    def sortLists(self,l1,l2):
        new = dummy = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next
        new.next = l1 or l2
        return dummy.next