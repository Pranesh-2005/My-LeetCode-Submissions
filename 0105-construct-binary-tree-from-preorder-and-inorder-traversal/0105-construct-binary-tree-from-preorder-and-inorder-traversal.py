# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ind = {v:i for i,v in enumerate(inorder)}
        preind = 0
        def build(l,r):
            nonlocal preind
            if l >= r:
                return None
            root = TreeNode(preorder[preind])
            preind += 1
            m = ind[root.val]
            root.left = build(l,m)
            root.right = build(m+1,r)
            return root
        return build(0,len(inorder))