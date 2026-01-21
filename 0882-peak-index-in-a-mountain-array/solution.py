class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        lo,hi=0 ,n-1
        while lo< hi:
            mid = (lo+hi)//2
            if arr[mid]> arr[mid + 1]:
                hi = mid 
            else:
                lo = mid + 1
        return lo 
