class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  #[inf, inf,inf,inf]
        pos=0              # [pos,neg,pos,neg,pos,neg]
        neg=1
        for i in range(n):
            if nums[i] >0:
                result[pos] = nums[i]
                pos+=2
            else:
                result[neg] = nums[i]
                neg+=2
        return result
