# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        
        n = 0
        stk = []
        curr = root

        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.left

            curr = stk.pop()
            n +=1
            
            if n == k:
                return curr.val
            curr = curr.right
            

            
