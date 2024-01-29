# 329. Longest Increasing Path in a Matrix
# Level : Hard

from typing import *
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        m = self.m
        n = self.n
        self.dp = [[-1] * n for _ in range(m)]

        dp = self.dp

        def dfs(i,j, prev) :
            
            if i<0 or j<0 or i>=self.m or j>=self.n or self.matrix[i][j] <= prev:
                return 0
            
            if dp[i][j] != -1 :
                return dp[i][j]
            
            curr = self.matrix[i][j]

            top = dfs(i-1, j, curr) 
            down = dfs(i+1, j, curr)
            left = dfs(i, j-1, curr)
            right = dfs(i, j+1, curr)

            dp[i][j] = 1 + max(top, down, left, right)
            return dp[i][j]
        
        maxi = 0
        for i in range(m) :
            for j in range(n) :
                res = dfs(i,j, -1)
                maxi = max(maxi, res)
        

        return maxi
      
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

# Example 1:


# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:


# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
# Example 3:

# Input: matrix = [[1]]
# Output: 1
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 231 - 1