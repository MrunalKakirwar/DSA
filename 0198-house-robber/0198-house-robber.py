class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = [-1] * (len(nums))
        def helper(nums, idx):
            if idx >= len(nums):
                return 0
            if d[idx] != -1:
                return d[idx]
            choose = nums[idx] + helper(nums, idx+2)
            notChoose = helper(nums, idx+1)
            d[idx] = max(choose, notChoose)
            return d[idx]
        return helper(nums, 0)

