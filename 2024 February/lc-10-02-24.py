# 647. Palindromic Substrings
# Level : Medium

class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        dp = [[1 if i==j else 0 for j in range(n)] for i in range(n)]
        res = n

        for j in range(n) :
            for i in range(j) :
                if s[i]==s[j] and (j-i == 1 or dp[i+1][j-1] == 1) :
                    dp[i][j] = 1
                    res += 1
        
        # print(dp)

        return res

# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.