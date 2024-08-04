import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []

        for num in arr:
            dist = abs(num - x)
            heapq.heappush(pq, (-dist, -num))
            if len(pq) > k:
                heapq.heappop(pq)
        return sorted(-num for diff, num in pq)
        

        