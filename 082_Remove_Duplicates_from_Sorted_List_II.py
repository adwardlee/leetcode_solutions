'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        first = tmp =  ListNode(-1)
        while head.next != None:
            if head.val != head.next.val:
                tmp.next = head
                tmp = tmp.next
                head = head.next
            else:
                while head.next != None and head.val == head.next.val:
                    head = head.next
                head = head.next
                if head == None:
                    break
        tmp.next = head
        return first.next
