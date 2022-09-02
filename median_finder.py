# leetcode 295 两个最值堆实现logn插入，查找中位数
class MedianFinder:
    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        minheap = self.minheap
        maxheap = self.maxheap

        if not minheap or num >= self.minheap[0]: # 让minheap始终大于等于maxheap可以让代码写的简洁一些
            heapq.heappush(self.minheap, num)
            if len(minheap) > len(maxheap)+1:
                node = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -node)
        else:
            heapq.heappush(self.maxheap, -num)
            if len(self.maxheap) > len(self.minheap):
                node = -heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, node)

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2
        else:
            return self.minheap[0]
