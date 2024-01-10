# 2385. Amount of Time for Binary Tree to Be Infected
# Level : Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:

    def convert(self, current: Optional[TreeNode], parent: int, hashmap: dict) :

        if current == None :
            return 
        val = current.val
        if current.val not in hashmap:
            hashmap[val] = set()
        if parent != 0 :
            hashmap[val].add(parent)
        if current.left :
            hashmap[val].add(current.left.val)
        if current.right :
            hashmap[val].add(current.right.val)
        self.convert(current.left, current.val, hashmap)
        self.convert(current.right, current.val, hashmap)
        
        
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        hashmap = {}
        self.convert(root, 0, hashmap)

        self.highest = 0
        self.travelled = set()

        def dfs(curr:int, depth:int, hashmap:dict):

            if curr in self.travelled :
                return
            self.travelled.add(curr)
            
            if depth > self.highest :
                self.highest = depth
            
            for i in hashmap[curr] :
                dfs(i, depth+1, hashmap)
        
        dfs(start, 0, hashmap)
        return self.highest


# You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

# Each minute, a node becomes infected if:

# The node is currently uninfected.
# The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected.

 

# Example 1:


# Input: root = [1,5,3,null,4,10,6,9,2], start = 3
# Output: 4
# Explanation: The following nodes are infected during:
# - Minute 0: Node 3
# - Minute 1: Nodes 1, 10 and 6
# - Minute 2: Node 5
# - Minute 3: Node 4
# - Minute 4: Nodes 9 and 2
# It takes 4 minutes for the whole tree to be infected so we return 4.
# Example 2:


# Input: root = [1], start = 1
# Output: 0
# Explanation: At minute 0, the only node in the tree is infected so we return 0.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 105
# Each node has a unique value.
# A node with a value of start exists in the tree.