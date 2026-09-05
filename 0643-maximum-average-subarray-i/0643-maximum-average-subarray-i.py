class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wsum = sum(nums[:k])
        mxsum = wsum
        for i in range(k,len(nums)):
            wsum += nums[i] - nums[i-k]
            mxsum = max(mxsum,wsum)
        return mxsum / k
        