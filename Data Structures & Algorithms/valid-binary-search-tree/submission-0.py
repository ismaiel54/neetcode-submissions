# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
                
        def isValidtree(node, right, left):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            
            return (isValidtree(node.left, node.val, left) and isValidtree(node.right, right, node.val))
            
        return isValidtree(root, float("inf"), float("-inf"))
        
            

        

        
        

        