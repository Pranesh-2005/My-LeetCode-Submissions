class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = defaultdict(int)
        for task in tasks:
            mp[task]+=1
        count = mp.values()
        maxc = max(count)
        tied = sum(c==maxc for c in count)
        return max(len(tasks), (maxc - 1) * (n+1)+tied)