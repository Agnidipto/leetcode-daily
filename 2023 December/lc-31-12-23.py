#cat : Easy

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        hashmap = {}

        res = -1

        for i in range(len(s)) :
            c = s[i]
            if c not in hashmap :
                hashmap[c] = i
            else :
                if i-hashmap[c]-1 > res :
                    res = i-hashmap[c]-1
        
        return res



# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.
# Example 2:

# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
# Example 3:

# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.