# 387. First Unique Character in a String
# Level : Easy

class Solution:
    def firstUniqChar(self, s: str) -> int:

        dp = [False] * len(s)
        hashmap = {}

        for i in range(len(s)) :
            c = s[i]

            if c not in hashmap :
                hashmap[c] = i
                dp[i] = True

            elif hashmap[c] != -1:
                dp[i] = False
                dp[hashmap[c]] = False
                hashmap[c] = -1

            # print(dp)
        # print(dp)
        # print(hashmap)
        for i in range(len(dp)) :
            if dp[i] :
                return i
        return -1
            
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.