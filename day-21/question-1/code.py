# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # With space complexity as O(N/2) = O(N)
        '''temp_dic = dict()
        n = 0
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            n+=1
            fast = fast.next.next
        n*=2
        temp = head
        i=0
        while i < n//2:
            temp_dic[n-1-i] = temp.val
            i+=1
            temp = temp.next
        maxx = 0
        while i in temp_dic and slow:
            temp_dic[i] = temp_dic[i] + slow.val
            maxx = max(maxx, temp_dic[i])
            i+=1
            slow = slow.next
        return maxx '''

        # Reverse the linked list from beginning till half of LL
        slow,fast = head,head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        res = 0
        while prev and slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res