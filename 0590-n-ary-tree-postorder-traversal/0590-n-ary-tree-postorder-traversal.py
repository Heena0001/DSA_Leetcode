"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans=[]
        if root is None:
            return ans
        stack = [root]
        while stack:
            current_node = stack.pop()
            ans.append(current_node.val)
            if current_node.children:
                for child in current_node.children:
                    stack.append(child)
        
        ans.reverse()  # Reverse the list to get the postorder traversal
        return ans
        