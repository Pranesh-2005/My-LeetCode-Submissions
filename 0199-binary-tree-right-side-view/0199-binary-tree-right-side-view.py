# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self,root):
        if not root:
            return []
        q,res = deque([root]),[]
        while q:
            lvl = []
            for _ in range(len(q)):
                cur = q.popleft()
                lvl.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(lvl)
        return res    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return [lvl[-1] for lvl in self.levelOrder(root)]