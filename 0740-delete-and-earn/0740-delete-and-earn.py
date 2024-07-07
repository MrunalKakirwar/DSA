class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = max(nums)
        arr = [0] * (length+1)
        for num in nums:
            arr[num] += num

        d = [-1] * (len(arr))
        def helper(arr, idx):
            # base:
            if idx >= (len(arr)):
                return 0
            if d[idx] != -1:
                return d[idx]
            # logic:
            choose = arr[idx] + helper(arr, idx + 2)
            notChoose = 0 + helper(arr, idx + 1)
            d[idx] = max(choose, notChoose)
            return d[idx]
        return helper(arr, 0)

        

           

