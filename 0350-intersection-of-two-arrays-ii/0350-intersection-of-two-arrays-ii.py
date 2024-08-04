class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        hm = {}
        for num in nums1:
            if num in hm:
                hm[num] +=1
            else:
                hm[num] = 1
        res = []
        for num in nums2:
            if num in hm:
                hm[num] -= 1
                res.append(num)
                if hm[num] == 0:
                    hm.pop(num)
        return res


        