'''
Description
Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].
What is heap? What is heapify? What if there is a lot of solutions?

Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.
Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].
Return any of them.
Example
Example 1

Input : [3,2,1,4,5]
Output : [1,2,3,4,5]
Explanation : return any one of the legitimate heap arrays
Challenge
O(n) time complexity
'''

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        self.length = len(A)
        mid = self.length // 2 - 1
        for i in range(mid, -1, -1):
            self.oneheap(A, i)
        return A

    def oneheap(self, A, i):
        index = i
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        if lchild < len(A) and A[lchild] < A[index]:
            index = lchild
        if rchild < len(A) and A[rchild] < A[index]:
            index = rchild
        if index != i:
            A[i], A[index] = A[index], A[i]
            self.oneheap(A, index)
        return