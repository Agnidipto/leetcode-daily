# 312. Burst Balloons
# Level : Hard

from pprint import pprint
from typing import *
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        def solve(i, j) :
            nums = self.nums
            n = self.n
            dp = self.dp
            if i > j :
                return 0
            if i==j :
                res = nums[i]
                if i-1 >= 0 : res *= nums[i-1]
                if i+1 < n : res *= nums[i+1]
                return res

            if dp[i][j] != -1 :
                return dp[i][j]

            maxi = 0
            for k in range(i, j+1) :
                res = nums[k]
                if i-1 >= 0 : res *= nums[i-1]
                if j+1 < n : res *= nums[j+1]
                res += solve(i,k-1) + solve(k+1,j)
                maxi = max(maxi, res)
            dp[i][j] = maxi
            return maxi

        new_nums = [1]
        for i in nums :
            if i != 0 :
                new_nums.append(i)
        new_nums.append(1)
        self.nums = new_nums
        self.n = len(self.nums)

        self.dp = [[-1] * self.n for i in range(self.n)]

        return solve(1, len(self.nums)-2)

        
# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

# Return the maximum coins you can collect by bursting the balloons wisely.

 

# Example 1:

# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# Example 2:

# Input: nums = [1,5]
# Output: 10
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# 0 <= nums[i] <= 100