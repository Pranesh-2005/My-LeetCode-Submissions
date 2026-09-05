class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        l,res,maxc = 0,0,0
        for r in range(len(s)):
            mp[s[r]] += 1
            maxc = max(maxc,mp[s[r]])
            while r-l+1-maxc > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res