class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m-1
        ptr2 = n-1
        idx = m+n - 1

        while(ptr1 >= 0 and ptr2 >= 0):
            if nums1[ptr1] > nums2[ptr2]:
                nums1[idx] = nums1[ptr1]
                ptr1 -=1
            else:
                nums1[idx] = nums2[ptr2]
                ptr2 -=1
            idx -=1   
        while(ptr2 >= 0):
            nums1[idx] = nums2[ptr2]
            ptr2 -=1
            idx -=1 
        return nums1

