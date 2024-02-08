# 279. Perfect Squares
# Level : Medium 

class Solution:
    def numSquares(self, n: int) -> int:

        # n = 21
        dp = [20000] * (n+1)
        dp[0] = 0
        ps= []
        i = 1

        while i*i <= n :
            ps.append(i*i)
            i += 1
        
        for i in range(n+1) :
            for j in ps :
                if i+j <= n:
                    dp[i+j] = min(dp[i]+1, dp[i+j])
                else :
                    break

        return dp[-1]
        
# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
 

# Constraints:

# 1 <= n <= 104