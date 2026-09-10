# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return (0,0)
            leftsum,leftheight = dfs(root.left)
            rightsum, rightheight = dfs(root.right)
            sum = leftsum+rightsum+root.val
            height = leftheight + rightheight + 1
            if root.val == (sum // height):
                res += 1
            return (sum,height) 
        dfs(root)
        return res