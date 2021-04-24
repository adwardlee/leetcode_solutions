'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            if lists[0] == None:
                return None
            return lists[0]
        node = self.merge(lists, 0, len(lists) - 1)
        return node
    
    def merge(self, lists, left, right):
        if left > right:
            return None
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        return self.mergeTwo(self.merge(lists, left, mid), self.merge(lists, mid + 1, right))
    
    def mergeTwo(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        head = tmp = ListNode(-1)
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tmp.next = l1
                tmp = tmp.next
                l1 = l1.next
            else:
                tmp.next = l2
                tmp = tmp.next
                l2 = l2.next
        if l1 != None:
            tmp.next = l1
        else:
            tmp.next = l2
        return head.next
            
            
        
    def sortLists(self, lists):
        indexes = {}
        for x in range(len(lists)):
            indexes[x] = 1
        while True:
            minvalue = 2e30
            remove_index = []
            valid_index = -1
            for i in indexes:
                if lists[i] == None:
                    remove_index.append(i)
                    continue
                if lists[i].val < minvalue:
                    minvalue = lists[i].val
                    valid_index = i
            if minvalue != 2e30:
                self.head.next = lists[valid_index]
                self.head = self.head.next
                lists[valid_index] = lists[valid_index].next
            else:
                break
            for x in remove_index:
                indexes.pop(x)
        return