class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x: int) -> int:
            return int(str(x)[::-1])

        my_map = {}
        min_dist = math.inf

        for i, num in enumerate(nums):
            if num in my_map:
                min_dist = min(min_dist, i - my_map[num])

            my_map[reverse(num)] = i

        return min_dist if min_dist != math.inf else -1
