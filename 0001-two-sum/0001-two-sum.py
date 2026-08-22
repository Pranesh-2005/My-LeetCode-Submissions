class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i,num in enumerate(nums):
            cmp = target - num
            if cmp in mp:
                return [mp[cmp],i]
            mp[num] = i
        return []