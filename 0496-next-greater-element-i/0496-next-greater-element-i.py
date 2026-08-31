class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = defaultdict(int)
        stk = []
        for i,num in enumerate(nums2):
            while stk and stk[-1] < num:
                mp[stk.pop()] = num
            stk.append(num)
        return [mp.get(num,-1) for num in nums1]