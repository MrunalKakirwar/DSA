class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        high = len(arr) - 1
        while(high - low >= k):
            lowDist = abs(arr[low] - x)
            highDist = abs(arr[high] - x)
            if lowDist > highDist:
                low += 1
            else:
                high -= 1
        res = []
        for i in range(low, high+1):
            res.append(arr[i])
        return res

            

        