'''
recursion for merge K Lists
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.lists = lists
        if len(self.lists) == 0:
            return None
        else:
            return self.merge(0, len(self.lists))
    
    def merge(self,left, right):
        length = len(self.lists[left:right])
        if length == 1:
            return self.lists[left]
        mid = (left + right) // 2
        head = self.mergeTwoLists(self.merge(left, mid), self.merge(mid, right))
        return head
        
        
    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return None
        head = temp = ListNode(0)
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            elif l1.val >= l2.val:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1 == None:
            head.next = l2
        elif l2 == None:
            head.next = l1
        return temp.next
        head = ListNode(0)
        temp = head
