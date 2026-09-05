class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        prefix,count = 0,0
        for num in nums:
            prefix = (prefix+num) % k
            count += mp[prefix]
            mp[prefix] += 1
        return count
        