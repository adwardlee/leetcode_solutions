'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur = head
        sum = 0
        carry = 0
        while l1 or l2:
            if l1 != None:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2 != None:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            sum = val1 + val2 +carry
            
            num = sum % 10
            carry = sum // 10
            head.next = ListNode(num)
            head = head.next
        if carry != 0:
            head.next = ListNode(carry) 
        return cur.next
