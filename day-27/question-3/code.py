class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_tail = list2
        while list2_tail.next:
            list2_tail = list2_tail.next
        list2_last_node = list2_tail

        node_before_a, node_after_b = None, None
        index, current_node = 0, list1
        while current_node:
            if index == a - 1:
                node_before_a = current_node
            if index == b:
                node_after_b = current_node.next
                break
            index += 1
            current_node = current_node.next

        node_before_a.next = list2
        list2_last_node.next = node_after_b

        return list1