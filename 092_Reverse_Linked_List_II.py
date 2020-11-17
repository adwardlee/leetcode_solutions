'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        prev = ListNode(-1)
        prev.next = head
        first = prev
        second = prev
        count = m
        while first.next != None and count > 1:
            first = first.next
            count -= 1

        second = first
        count = n - m + 1
        while second.next != None and count > 0:
            second = second.next
            count -= 1
        for i in range(n - m):
            tmp = second.next
            second.next = first.next
            first.next = first.next.next
            second.next.next = tmp
        return prev.next
        
