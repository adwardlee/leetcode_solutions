'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        first = tmp = ListNode(-1)
        while head.next != None:
            while head.next != None and head.val == head.next.val:
                head = head.next
            tmp.next = head
            tmp = tmp.next
            head = head.next 
            if head == None:
                break
        tmp.next = head
        return first.next
                    
