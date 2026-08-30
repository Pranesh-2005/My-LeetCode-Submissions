class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        l,r = max(nums),sum(nums)
        res = r
        def canShip(cap):
            curcap = cap
            shp = 1
            for num in nums:
                if curcap - num < 0:
                    shp += 1
                    curcap = cap
                curcap -= num
            return shp <= days
        while l <= r:
            m = l + (r - l) // 2
            if canShip(m):
                res = min(res,m)
                r = m - 1
            else:
                l = m + 1
        return res