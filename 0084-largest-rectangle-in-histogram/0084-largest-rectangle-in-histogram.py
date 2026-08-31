class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        res = 0
        stk = []
        for i,num in enumerate(nums):
            st = i
            while stk and stk[-1][1] > num:
                ind,hei = stk.pop()
                res = max(res, hei * (i-ind))
                st = ind
            stk.append((st,num))
        for i,num in stk:
            # ind,hei = stk.pop()
            res = max(res,num * (len(nums)-i))
        return res
