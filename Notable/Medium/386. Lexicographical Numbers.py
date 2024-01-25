# 386. Lexicographical Numbers
# Level : Medium

from typing import *

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = []

        def trav(x, n, res) :
            if x <= n :
                res.append(x)
                trav(x*10, n, res)
                if x%10 != 9 :
                    trav(x+1, n, res)
                return None
            else :
                return None
        
        trav(1, n, res)
        
        return res
        
# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

# You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

# Example 1:

# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
# Example 2:

# Input: n = 2
# Output: [1,2]
 

# Constraints:

# 1 <= n <= 5 * 104