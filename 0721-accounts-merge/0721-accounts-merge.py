class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            res = n1
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return False
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return True
        emailtoacc = {}
        for i,a in enumerate(accounts):
            for email in a[1:]:
                if email in emailtoacc:
                    union(i,emailtoacc[email])
                else:
                    emailtoacc[email] = i
        emailgrp = defaultdict(list)
        for e,a in emailtoacc.items():
            leader = find(a)
            emailgrp[leader].append(e)
        res = []
        for i,e in emailgrp.items():
            name = accounts[i][0]
            res.append([name]+list(sorted(e)))
        return res