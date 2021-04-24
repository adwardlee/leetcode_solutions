'''
Description
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example
Example 1:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // return 1.00000
m.next(10) = (1 + 10) / 2 // return 5.50000
m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
m.next(5) = (10 + 3 + 5) / 3 // return 6.00000
'''

from collections import deque
class MovingAverage(object):
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.list = deque([])
        self.cur_size = 0
        self.sum = 0

    """
    @param: val: An integer
    @return:
    """
    def next(self, val):
        # write your code here
        self.cur_size += 1
        if len(self.list) >= self.size:
            self.sum -= self.list[0]
            self.list.popleft()
            self.cur_size -= 1
        self.sum += val
        self.list.append(val)

        result = self.sum / self.cur_size
        return result
