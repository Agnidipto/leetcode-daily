# 931. Minimum Falling Path Sum
# Level : Medium

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)

        dp=[[0] * n for i in range(n)]

        for i in range(n) :
            dp[0][i] = matrix[0][i]

        for i in range(1,n) :
            for j in range(n) :
                x = 100000
                if j>0 and dp[i-1][j-1] < x :
                    x = dp[i-1][j-1]
                if dp[i-1][j] < x :
                    x = dp[i-1][j]
                if j<(n-1) and dp[i-1][j+1] < x :
                    x = dp[i-1][j+1]
                dp[i][j] = x + matrix[i][j]

        # print(dp)

        return min(dp[n-1])


# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

# Example 1:


# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
# Example 2:


# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100