class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        if n == 0:
            return
        elif m == 0:
            for i in range(0,n):
                nums1[i] = nums2[i]
        else: 
            p1 = m - 1
            p2 = n - 1
            lp = m + n - 1

            while p2 >=0:
                if p1 >= 0 and nums1[p1] > nums2[p2]:
                    nums1[lp] = nums1[p1]
                    p1 -= 1
                else: 
                    nums1[lp] = nums2[p2]
                    p2 -= 1
                lp -= 1

            



        