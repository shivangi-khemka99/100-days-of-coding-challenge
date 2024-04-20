# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        dummy = ListNode(0,head)
        prev, temp = dummy, head

        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        dummy.next.next = None
        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list_head = self.reverseList(head)
        dummy = ListNode(0, reversed_list_head)
        minn = reversed_list_head.val
        prev,temp = dummy,reversed_list_head
        while temp:
            if temp.val < minn :
                prev.next = temp.next
            else:
                minn = temp.val
                prev = temp
            temp = temp.next
        return self.reverseList(dummy.next)
    

    # class Solution:
    # def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head.next:
    #         return head
    #     nextNode = self.removeNodes(head.next)
    #     if head.val < nextNode.val:
    #         return nextNode
    #     else:
    #         head.next = nextNode 
    #         return head
        