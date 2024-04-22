# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        while prev and prev.next:
            new_head, last_node, next_head = self.reverseList(prev.next,k)
            prev.next = new_head
            if last_node: last_node.next = next_head
            prev = last_node
        return dummy.next

    def reverseList(self, head, k):
        dummy = ListNode(0,head)
        pre,temp,i = dummy, head,k
        while temp and i > 0: #Check if k nodes are there
            pre = temp
            temp=temp.next
            i-=1
        if i == 0 : # if k nodes are there then reverse the linkedlist
            cur,prev = head,dummy
            while cur and k > 0:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                k-=1
            dummy.next = None
            return prev,head,cur
        else:
            return head, pre, temp