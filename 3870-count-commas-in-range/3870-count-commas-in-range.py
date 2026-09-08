class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n)) < 4:
            return 0
        count = 0
        while len(str(n)) >= 4:
            count += 1
            n -= 1
        return count