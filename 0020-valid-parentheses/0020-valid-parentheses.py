class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')':'(', '}':'{', ']':'['}
        stk = []
        for ch in s:
            if ch in mp:
                if not stk or stk.pop() != mp[ch]:
                    return False
            else:
                stk.append(ch)
        return not stk