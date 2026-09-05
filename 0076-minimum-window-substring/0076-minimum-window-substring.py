class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        mps,mpt = defaultdict(int),defaultdict(int)
        for i in range(len(t)):
            mpt[t[i]] += 1
        hv,nd = 0,len(mpt)
        res,resL = [-1,-1],float("inf")
        l = 0
        for r in range(len(s)):
            mps[s[r]] += 1
            if s[r] in mpt and mps[s[r]] == mpt[s[r]]:
                hv += 1
            while hv == nd:
                if r-l+1 < resL:
                    res = [l,r]
                    resL = r-l+1
                mps[s[l]] -= 1
                if s[l] in mpt and mps[s[l]] < mpt[s[l]]:
                    hv -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resL != float("inf") else ""