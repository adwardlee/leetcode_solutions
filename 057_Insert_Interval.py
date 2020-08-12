'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''
class Solution:
    def insert(self, intervals, newInterval):
        i = 0
        if len(intervals) == 0:
            return [newInterval]
        if len(newInterval) == 0:
            return intervals
        '''
        if newInterval[0] > intervals[-1][1]:
            return intervals + newInterval
        '''

        index = 0
        if newInterval[0] < intervals[0][0]:
            intervals = [newInterval] + intervals
        else:
            for idx, x in enumerate(intervals):
                if newInterval[0] >= x[0]:
                    index = idx
            intervals = intervals[:index + 1] + [newInterval] + intervals[index + 1:]
        i = index
        length = len(intervals)
        while i < length - 1:
            if intervals[i][1] < intervals[i + 1][0]:
                i += 1
            else:
                intervals = intervals[:i] + [[intervals[i][0], max(intervals[i][1], intervals[i + 1][1])]] + intervals[i + 2:]
                
                length -= 1
        return intervals
