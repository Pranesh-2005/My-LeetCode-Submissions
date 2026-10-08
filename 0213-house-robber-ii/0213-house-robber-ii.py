class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0],self.houseRob1(nums[1:]),self.houseRob1(nums[:-1]))
    def houseRob1(self,nums):
        rob1,rob2 = 0,0
        for num in nums:
            newrob = max(num+rob1,rob2)
            rob1 = rob2
            rob2 = newrob
        return rob2
