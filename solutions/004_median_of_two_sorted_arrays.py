import heapq

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        min_heap = []
        max_heap = []
        for num in nums1+nums2:
            if len(min_heap) == len(max_heap):
                heapq.heappush(max_heap, -heapq.heappushpop(min_heap, -num))
            else:
                heapq.heappush(min_heap, -heapq.heappushpop(max_heap, num))

        if len(min_heap) == len(max_heap):
            return float(max_heap[0] - min_heap[0]) / 2.0
        else:
            return float(max_heap[0])
 