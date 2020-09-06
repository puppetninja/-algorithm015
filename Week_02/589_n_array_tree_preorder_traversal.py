"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None: return []
        if root.children is None: return [root.val]
        
        preorder_list = [root.val]
        for child in root.children:
            preorder_list = preorder_list + self.preorder(child)
            
        return preorder_list
