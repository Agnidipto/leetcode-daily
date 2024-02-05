# 1043. Partition Array for Maximum Sum
# Level : Medium 

from typing import *

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        dp = [0] * n

        for i in range(n) :
            maxi = arr[i]
            for j in range(k) :
                if i-j < 0 :
                    break
                if arr[i-j] > maxi :
                    maxi = arr[i-j]
                a = (j+1) * maxi
                a += dp[i-j-1] if i-j-1 >=0 else 0
                dp[i] = max(dp[i], a)
        
        # print(dp)
        return dp[-1]

# Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

# Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

# Example 1:

# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# Explanation: arr becomes [15,15,15,9,10,10,10]
# Example 2:

# Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# Output: 83
# Example 3:

# Input: arr = [1], k = 1
# Output: 1
 

# Constraints:

# 1 <= arr.length <= 500
# 0 <= arr[i] <= 109
# 1 <= k <= arr.length