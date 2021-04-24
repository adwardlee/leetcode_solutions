'''
Description
We need to implement a data structure named DataStream. There are two methods required to be implemented:

void add(number) // add a new number
int firstUnique() // return first unique number
You can assume that there must be at least one unique number in the stream when calling the firstUnique.

Example
Example 1:

Input:
add(1)
add(2)
firstUnique()
add(1)
firstUnique()
Output:
[1,2]
Example 2:

Input:
add(1)
add(2)
add(3)
add(4)
add(5)
firstUnique()
add(1)
firstUnique()
add(2)
firstUnique()
add(3)
firstUnique()
add(4)
firstUnique()
add(5)
add(6)
firstUnique()
Output:
[1,2,3,4,5,6]
'''

class LinkedList():
    def __init__(self, key, thenext=None):
        self.key = key
        self.next = thenext

class DataStream:

    def __init__(self):
        # do intialization if necessary
        self.hash_dict = {}
        self.tail = self.head = LinkedList(-1)
        self.tail.next = LinkedList(-2)
        self.duplicate = set()
        """
        @param num: next number in stream
        @return: nothing
        """
    def add(self, num):
        # write your code here

        """
        @return: the first unique number in stream
        """
        if num in self.duplicate:
            return
        elif num in self.hash_dict:
            self.duplicate.add(num)
            node = self.hash_dict[num]
            if node.next == self.tail:
                self.tail = node
            node.next = node.next.next
            self.hash_dict[node.next.key] = node
            self.hash_dict.pop(num)
        else:
            node = LinkedList(num)
            tmp = self.tail.next
            node.next = tmp
            self.tail.next = node
            self.hash_dict[num] = self.tail
            self.tail = node
        return


    def firstUnique(self):
        # write your code here
        return self.head.next.key