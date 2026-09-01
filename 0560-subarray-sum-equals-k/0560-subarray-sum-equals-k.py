class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        res,prefix = 0,0
        for num in nums:
            prefix += num
            res += mp[prefix-k]
            mp[prefix] += 1
        return res
