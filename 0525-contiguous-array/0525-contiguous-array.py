class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myMap = {}
        rsum = 0
        maxR = 0
        myMap[0] = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                rsum -=1
            if nums[i] == 1:
                rsum +=1
            if rsum not in myMap:
                myMap[rsum] = i
            else:
                maxR = max(maxR, i - myMap[rsum])
        return maxR
