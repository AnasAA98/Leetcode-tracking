class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        score = 0
        heap = [(nums[i],i) for i in range(n)]
        heapq.heapify(heap)
        while heap:
            val,indx = heapq.heappop(heap)
            if marked[indx] == True:
                continue
            marked[indx] = True
            score +=  val
            if indx + 1 < n:
                marked[indx + 1] = True
            if indx - 1 >=0:
                marked[indx - 1] = True
        return score

