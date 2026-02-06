class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = [str(x) for x in nums]

        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        strs.sort(key=cmp_to_key(compare))
        return "0" if strs[0] == "0" else "".join(strs)

