class NumArray:

    def __init__(self, nums: List[int]):
        prefix = [0]*(len(nums)+1)
        for i,num in enumerate(nums):
            prefix[i+1] = prefix[i]+nums[i]
        self.prefix = prefix

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)