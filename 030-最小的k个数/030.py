# -*- coding:utf-8 -*-
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k > len(tinput):
            return []
        maxHeap = []
        for item in tinput:
            item = -item
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, item)
            else:
                heapq.heappushpop(maxHeap, item)
        return [-heapq.heappop(maxHeap) for i in range(len(maxHeap))][::-1]