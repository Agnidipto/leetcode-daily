# 1074. Number of Submatrices That Sum to Target
# Level : Hard

from typing import *

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        # matrix = [[1,2,1], [4,1,1], [1,6,1]]
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m) :
            for j in range(n) :
                add = 0
                if i-1 >=0 :
                    add += dp[i-1][j]
                    if j-1 >= 0 :
                        add -= dp[i-1][j-1]
                if j-1 >= 0 :
                    add += dp[i][j-1]
                dp[i][j] = matrix[i][j] + add
        
        # print(dp)
        count = 0

        for c1 in range(n) :
            for c2 in range(c1, n) :
                s = {}
                s[0] = 1
                summ = 0

                for row in range(m) :
                    summ = dp[row][c2]
                    if c1 > 0 :
                        summ -= dp[row][c1-1]

                    # print(c1, c2, row, summ)

                    if (summ-target) in s :
                        count += s[summ-target]
                        # print('yo')

                    s[summ] = s.get(summ, 0) + 1

        return count


# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

# Example 1:


# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
# Example 2:

# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
# Example 3:

# Input: matrix = [[904]], target = 0
# Output: 0
 

# Constraints:

# 1 <= matrix.length <= 100
# 1 <= matrix[0].length <= 100
# -1000 <= matrix[i] <= 1000
# -10^8 <= target <= 10^8