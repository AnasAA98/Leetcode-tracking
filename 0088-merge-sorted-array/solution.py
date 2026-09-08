class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p = 0, 0, 0
        temp = nums1[:m]
        while p1 < m and p2 < n:
            if temp[p1] <= nums2[p2]:
                nums1[p] = temp[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1
        if p1 < m:
            nums1[p:] = temp[p1:]
        if p2 < n:
            nums1[p:] = nums2[p2:] 

