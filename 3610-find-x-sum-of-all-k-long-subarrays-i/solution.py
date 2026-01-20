class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n-k +1):
            freq = Counter(nums[i:i+k])
            heap = [(-count,-num) for num,count in freq.items()]
            heapq.heapify(heap)
            s = 0
            for _ in range(min(x,len(heap))):
                frq,num = heapq.heappop(heap)
                s += (-frq) * (-num)
            ans.append(s) 
        return ans
