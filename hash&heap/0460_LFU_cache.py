'''
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3
 

Constraints:

0 <= capacity, key, value <= 104
At most 105 calls will be made to get and put.
 

Follow up: Could you do both operations in O(1) time complexity?
'''

class LinkedList(object):
    def __init__(self, key, value, prev=None, next=None):
        self.next = next
        self.key = key
        self.value = value
        self.prev = prev
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_dict = {}
        self.key_count = {} ### key: [count,number] 0 , -1, -2 , -3
        self.head = LinkedList(-1, -1)
        self.tail = LinkedList(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hash_dict:
            node = self.hash_dict[key]
            value = node.value
            self._add(key, value)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.hash_dict:
            self._add(key, value)
        else:
            if self.capacity <= len(self.hash_dict.keys()):
                self._remove()
            self._add(key, value)
        return

    def _remove(self):
        key = self.get_minnode()
        if key == None:
            return
        node = self.hash_dict[key]
        prev = node.prev
        nextone = node.next
        prev.next = nextone
        nextone.prev = prev
        self.hash_dict.pop(key)
        self.key_count.pop(key)
        return

    def _add(self, key, value):
        for onekey in self.key_count:
            self.key_count[onekey][1] = self.key_count[onekey][1] - 1

        if key in self.key_count:
            self.key_count[key][0] = self.key_count[key][0] + 1
            self.key_count[key][1] = 0
            node = self.hash_dict[key]
            node.value = value
        else:
            self.key_count[key] = []
            self.key_count[key].append(1)
            self.key_count[key].append(0)
            node = LinkedList(key, value)
            self.hash_dict[key] = node
            prev = self.tail.prev

            prev.next = node
            node.prev = prev
            node.next = self.tail
            self.tail.prev = node

        return

    def get_minnode(self):
        mincount = float('inf')
        most_remote = float('inf')
        returnkey = None
        for key in self.key_count:
            count, recent = self.key_count[key]
            if count < mincount:
                mincount  = count
                returnkey = key
                most_remote = recent
            elif count == mincount and recent < most_remote:
                most_remote = recent
                returnkey = key
        return returnkey
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)