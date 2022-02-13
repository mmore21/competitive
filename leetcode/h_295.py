"""
Problem 295 - Find Median from Data Stream
Difficulty: Medium
URL: https://leetcode.com/problems/find-median-from-data-stream/
"""

import bisect

class MedianFinder:
    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)

    def findMedian(self) -> float:
        arr_len = len(self.arr)
        idx = arr_len // 2
        if arr_len % 2 == 0:
            return (self.arr[idx-1] + self.arr[idx]) / 2
        else:
            return self.arr[idx]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
