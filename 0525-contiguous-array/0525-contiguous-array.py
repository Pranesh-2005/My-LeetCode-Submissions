class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0
        oc,zc = 0,0
        for i,num in enumerate(nums):
            if num == 0:
                zc += 1
            else:
                oc += 1
            if oc-zc not in mp:
                mp[oc-zc] = i
            if oc == zc:
                res = oc+zc
            else:
                ind = mp[oc-zc]
                res = max(res,i - ind)
        return res