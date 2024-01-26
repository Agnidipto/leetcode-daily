# 233. Number of Digit One
# Level : Hard 

import math
class Solution:
    def countDigitOne(self, n: int) -> int:

        # n = 101

        if n == 0 :
            return 0

        ranges = {0:0}
        no = int(math.log10(n)) + 1

        for i in range(1, no) :
            ranges[i] = i * (10**(i-1))

        def check(n, ranges) :

            if n == 0 :
                return 0
            d = int(math.log10(n)) + 1
            firstDigit = int(str(n)[0])

            res = 0
            
            for i in range(firstDigit) :
                res += ranges[d-1]
                if i == 1 :
                    res += 10 ** (d-1)
            
            if firstDigit == 1 :
                if d > 1 :
                    res += int(str(n)[1:]) + 1
                else :
                    res += 1

            if d > 1:
                res += check(int(str(n)[1:]), ranges)
            return res
        
        return check(n, ranges)
    
# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

 

# Example 1:

# Input: n = 13
# Output: 6
# Example 2:

# Input: n = 0
# Output: 0
 

# Constraints:

# 0 <= n <= 109

  