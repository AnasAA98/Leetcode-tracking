class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def search(is_left):
            index = -1
            lo = 0
            hi = n - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] > target:
                    hi = mid - 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    index = mid
                    if is_left:
                        hi = mid - 1
                    else:
                        lo = mid + 1
            return index
        low = search(True)
        high = search(False)
        return [low,high] if low != -1 and high != -1 else [-1,-1]
