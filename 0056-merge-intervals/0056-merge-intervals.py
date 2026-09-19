class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for start,end in intervals[1:]:
            last = res[-1][1]
            if start <= last:
                res[-1][1] = max(last,end)
            else:
                res.append([start,end])
        return res