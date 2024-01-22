# 645. Set Mismatch
# Level : Easy

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        twice = None

        dp = [False] * (len(nums) + 1)
        dp[0] = True

        for i in range(len(nums)) :
            if dp[nums[i]] :
                twice = nums[i]
            else :
                dp[nums[i]] = True
        
        missing = dp.index(False)

        return [twice, missing]

        
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104