# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        
        dummy = ListNode(0,head)
        prev,cur = dummy,head

        LeftNode, RightNode = ListNode(), ListNode()

        for i in range(left-1):
            prev,cur=cur,cur.next
        
        LeftNode = cur
        pre=None

        for i in range(right-left+1):
            temp = cur.next
            cur.next=pre
            pre=cur
            cur=temp

        RightNode=pre
        prev.next=RightNode
        LeftNode.next=cur

        return dummy.next