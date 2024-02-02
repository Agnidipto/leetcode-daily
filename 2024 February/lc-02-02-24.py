# 1291. Sequential Digits
# Level : Medium 

from typing import *

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        # def get_length(n, x) :
        #     if n/(10**x) < 10 :
        #         return x
        #     return get_length(n, x+1)

        # def generate(start, i) :
        #     if i < 0 :
        #         return ''
        #     return str(start) + generate(start+1, i-1)
        
        # res = []

        # i = get_length(low, 0)
        # start = int(str(low)[0])
        # last = get_length(high, 0)

        # while i <= last :

        #     for j in range(start, 10-i) :

        #         temp = int(generate(j, i))
        #         if temp >= low and temp <= high :
        #             res.append(temp)
            
        #     i+=1
        #     start = 1

        # return res


        def get_length(n, x) :
            if n/(10**x) < 10 :
                return x
            return get_length(n, x+1)

        res = []

        s = '0123456789'

        f = int(str(low)[0])
        size = get_length(low, 0)

        while True :

            if f+size > 9 :
                f = 1
                size += 1

            if size>=9 :
                break
            
            t = int(s[f:f+size+1])

            if t > high :
                break

            if t >= low :
                res.append(t)

            f += 1
        
        return res


# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
 

# Constraints:

# 10 <= low <= high <= 10^9


