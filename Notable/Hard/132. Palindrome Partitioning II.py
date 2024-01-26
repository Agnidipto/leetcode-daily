# 132. Palindrome Partitioning II
# Level : Hard

from pprint import pprint
class Solution:
    def minCut(self, s: str) -> int:

        # s = 'aabaac'
        
        n = len(s)
        dp = [set() for i in range(n)]
        
        #index = 1
        for i in range(1,n) :
            if s[i] == s[i-1] :
                dp[i].add(2)
        
        #index = 2
        for i in range(2,n) :
            if s[i] == s[i-2] :
                dp[i].add(3)

        # index > 2 
        for i in range(3,n) :
            for x in dp[i-1].copy() :
                if i-x-1 >= 0 and s[i] == s[i-x-1] :
                    dp[i].add(x+2)
        
        # pprint(dp)

        res = [i for i in range(n)]

        for i in range(1,n) :
            res[i] = res[i-1] + 1
            for x in dp[i] :
                left = i-x
                if left >= 0 :
                    res[i] = min(res[i], res[left] + 1)
                else :
                    res[i] = 0

        # print(res)

        return res[-1]

                
# Given a string s, partition s such that every 
# substring
#  of the partition is a 
# palindrome
# .

# Return the minimum cuts needed for a palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
# Example 2:

# Input: s = "a"
# Output: 0
# Example 3:

# Input: s = "ab"
# Output: 1
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase English letters only.