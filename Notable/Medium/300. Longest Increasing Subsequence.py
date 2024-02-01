# 300. Longest Increasing Subsequence
# Level : Medium

from typing import *

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        res = []
        size = 0

        for i in range(n) :
            
            if size == 0 or nums[i] > res[-1] :
                res.append(nums[i])
                size += 1
            
            else :

                l,r = 0, size-1

                while l<=r :
                    mid = (l+r) // 2
                    if nums[i] > res[mid] :
                        l = mid+1
                    else :
                        r = mid-1

                res[l] = nums[i]
        
        return size

# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
 

# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?