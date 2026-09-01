class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        leftsum = 0
        for i,num in enumerate(nums):
            rightsum = totalsum - leftsum - num
            if leftsum == rightsum:
                return i
            leftsum += num
        return -1