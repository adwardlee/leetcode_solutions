'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

Runtime: 20 ms, faster than 99.90% of Python3 online submissions for Partition List.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Partition List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def swap_node(x, y):
    tmp = x.next
    tmp1 = y.next.next
    x.next = y.next
    x = x.next
    x.next = tmp
    y.next = tmp1
    return x, y


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None or head.next is None:
            return head
        first = ListNode(-1)
        first.next = head
        p = first
        while (p.next):
            if p.next.val >= x:
                in_pos = p
                break
            p = p.next
            if p.next is None:
                return first.next
        while (p and p.next):
            if p.next.val < x:
                in_pos, p = swap_node(in_pos, p)
                continue
            if p.next is None:
                return first.next
            # elif p.next.next is None:
            #     prev = p
            p = p.next


        if p.val < x:
            tmp = in_pos.next
            in_pos.next = p
            in_pos = in_pos.next
            in_pos.next = tmp
            prev.next = None
        return first.next
