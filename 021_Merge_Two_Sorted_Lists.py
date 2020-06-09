'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        temp = head
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next
        if l1 != None:
            temp.next = ListNode(l1.val)
            
            temp.next.next = l1.next
        elif l2 != None:
            temp.next = ListNode(l2.val)
            temp.next.next = l2.next
            
        return head.next
