# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum=0
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        def rangeSumCheck(node,L,R):
            if not node:
                return 0
            if L <= node.val <= R:
                    self.sum+=node.val
                    
            rangeSumCheck(node.left, L, R)
            rangeSumCheck(node.right, L, R)
        

        rangeSumCheck(root,L,R)
        return self.sum
            
   
 
        