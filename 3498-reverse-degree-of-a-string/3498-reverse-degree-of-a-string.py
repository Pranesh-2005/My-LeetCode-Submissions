class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i,ch in enumerate(s):
            mul = (ord('z') - ord(ch) + 1) * (i+1)
            print(mul)
            res = res + mul 
        return res