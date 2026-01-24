class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        curr_window = sum(arr[:k])
        result = 1 if curr_window //k >= threshold else 0
        for i in range(k,n):
            curr_window = curr_window + arr[i] - arr[i-k]
            if curr_window // k >= threshold:
                result +=1
        return result

