'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        numbers = len(lists)
        spread = 1
        while numbers > spread:
            for i in range( 0, numbers - spread, spread * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+spread])
            spread *= 2
        return lists[0] if numbers > 0 else None
                
        
        
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        temp = head
        if l1 == None and l2 == None:
            return None
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            else:
                head.next = l2
                l2 = l2.next
                head = head.next
        if l1 == None:
            head.next =  l2
        elif l2 == None:
            head.next = l1
        return temp.next
