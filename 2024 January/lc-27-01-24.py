# 629. K Inverse Pairs Array
# Level : Hard

# from pprint import pprint
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        # n = 4
        # k = 5

        if k == 0:
            return 1
        
        dp = [[0] * (k+1) for i in range(n+1)]

        dp[0][0] = 1
        dp[1][0] = 1

        l = 1

        for i in range(2,n+1) :

            dp[i][0] = 1

            for j in range(1, min(k, l) + 1) :
                deduct = dp[i-1][j-i] if j-i >= 0 else 0

                dp[i][j] = dp[i][j-1] + dp[i-1][j] - deduct
            
            l+=i
        
        # pprint(dp)

        if dp[-1][-1] is None :
            return 0
        return dp[-1][-1] % (10 ** 9 + 7)


# For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

# Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 3, k = 0
# Output: 1
# Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
# Example 2:

# Input: n = 3, k = 1
# Output: 2
# Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 

# Constraints:

# 1 <= n <= 1000
# 0 <= k <= 1000