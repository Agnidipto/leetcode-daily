# 76. Minimum Window Substring
# Level : Hard 

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hashmap = {}
        for i in t :
            hashmap[i] = hashmap.get(i,0) + 1
        
        temp_hash = {}
        look = set(t)
        req = len(hashmap)
        formed = 0

        l, r = 0, 0

        ans = [-1, 0, 0]

        while r < len(s) :

            c = s[r]
            
            if c in look :
                temp_hash[c] = temp_hash.get(c,0) + 1
                if temp_hash[c] == hashmap[c] :
                    formed += 1
            
            # print(l,r, formed, req)
            
            while l<=r and formed == req :

                c = s[l]

                if ans[0] == -1 or r+1-l < ans[0] :
                    ans[0] = r+1-l
                    ans[1] = l
                    ans[2] = r+1
                
                if c in look:
                    temp_hash[c] -= 1
                    if temp_hash[c] < hashmap[c] :
                        formed -= 1
                
                l+=1
                # print(l,r, formed, req)
            r+=1

            
        return '' if ans[0] == -1 else s[ans[1]:ans[2]]

        
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?