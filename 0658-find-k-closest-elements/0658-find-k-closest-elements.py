class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        high = len(arr) - k 
        while(low < high):
            mid = (low + high) // 2
            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1
            else:
                high = mid
        res = []
        for i in range(low, low+k):
            res.append(arr[i])
        return res

            

        