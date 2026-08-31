class Solution:
    def evalRPN(self, s: List[str]) -> int:
        mp = {'+': lambda a,b: a+b, '-': lambda a,b: a-b, '*': lambda a,b : a*b, '/': lambda a,b: int(a/b)}
        stk = []
        for ch in s:
            if ch in mp and stk:
                b,a = stk.pop(),stk.pop()
                stk.append(mp[ch](a,b))
            else:
                stk.append(int(ch))
        return stk[-1]

