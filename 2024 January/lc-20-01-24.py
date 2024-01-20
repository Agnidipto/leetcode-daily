# 907. Sum of Subarray Minimums
# Level : Medium 

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        n = len(arr)
        stk = []
        res = 0

        for i in range(len(arr)) :

            left = i
            
            while len(stk) > 0 and stk[-1][0] > arr[i] :
                left = stk[-1][2]
                res += stk[-1][0] * (i-stk[-1][1]) * (stk[-1][1]-stk[-1][2]+1)
                # print(stk[-1][0] , (i-stk[-1][1]) * (stk[-1][1]-stk[-1][2]+1))
                stk.pop(-1)
            
            stk.append((arr[i], i, left))
            # print(stk)

        i += 1
        while len(stk) > 0 :
            res += stk[-1][0] * (i-stk[-1][1]) * (stk[-1][1]-stk[-1][2]+1)
            # print(stk[-1][0] , (i-stk[-1][1]) * (stk[-1][1]-stk[-1][2]+1))
            stk.pop(-1)   
        
        return res%(10 ** 9 + 7)


# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

# Example 1:

# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
# Example 2:

# Input: arr = [11,81,94,43,3]
# Output: 444
 

# Constraints:

# 1 <= arr.length <= 3 * 104
# 1 <= arr[i] <= 3 * 104