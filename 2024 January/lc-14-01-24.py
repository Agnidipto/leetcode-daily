# 1657. Determine if Two Strings Are Close
# Level : Medium

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        def findi(s1, s2, num) :
            for i in range(26) :
                if s2[i] == num :
                    if s1[i] != 0  :
                        return i
            return -1

        if len(word1) != len(word2) :
            return False

        s1 = [0] * 26
        s2 = [0] * 26

        for i in word1 :
            s1[ord(i) - ord('a')] += 1
        
        for i in word2 :
            s2[ord(i) - ord('a')] += 1

        for i in range(26) :

            if s1[i] == 0 :
                continue
            
            if s1[i] == s2[i] :
                s1[i] = -1
                s2[i] = -1
            
            else :
                yo = findi(s1, s2, s1[i]) 
                if yo == -1 :
                    return False
                s1[i] = -1
                s2[yo] = -1
        
        return True
        
        
# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

# Example 1:

# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
# Example 2:

# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
# Example 3:

# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
 

# Constraints:

# 1 <= word1.length, word2.length <= 105
# word1 and word2 contain only lowercase English letters.