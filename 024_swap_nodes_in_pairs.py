'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        start = cur = ListNode(0)
        cur.next = head
        first = head
        if head == None or head.next == None:
            return head
        second = head.next.next
        
        while second != None:
            cur.next = first.next
            cur.next.next = first
            first.next = second
            
            cur = cur.next.next
            first = first.next
            if second.next == None:
                break
            second = second.next.next
            
        if first.next != None:
            cur.next = first.next
            cur.next.next = first
            first.next = None
        
        return start.next
