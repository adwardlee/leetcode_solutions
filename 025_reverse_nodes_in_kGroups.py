'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        start = the_first = ListNode(0)
        the_first.next = head
        second = start.next
        while second != None:
            for i in range(k):
                if second == None:
                    return the_first.next
                second = second.next
            start = self.reverselist(start, k)
        return the_first.next
        
        
    def reverselist(self,start,k):
        cur = start.next
        temp = cur.next
        for i in range(k-1):
            one_temp = start.next
            
            
            start.next = temp
            cur.next = temp.next
            temp.next = one_temp
            
            temp = cur.next
        return cur
