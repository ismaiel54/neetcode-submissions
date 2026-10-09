"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        start = node
        o_to_n = {}
        stk = [node]
        seen = set()
        seen.add(node)

        while stk:
            node = stk.pop()
            copy = Node(node.val)
            o_to_n[node] = copy
            for nei in node.neighbors:
                if nei not in seen:
                    seen.add(nei)
                    stk.append(nei)

        for old, new in o_to_n.items():
            for nei in old.neighbors:
                new_n = o_to_n[nei]
                new.neighbors.append(new_n)
        
        return o_to_n[start]



