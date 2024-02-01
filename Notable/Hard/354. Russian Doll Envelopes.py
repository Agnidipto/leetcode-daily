# 354. Russian Doll Envelopes
# Level : Hard 

from typing import *

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # print(envelopes)
        
        res = []		
		# Perform LIS
        for _, h in envelopes:
            l,r=0,len(res)-1
			# find the insertion point in the Sort order
            if len(res) == 0 or h > res[-1] :
                res.append(h)
            else :
                while l <= r:
                    mid=(l+r)//2
                    if res[mid]>=h:
                        r=mid-1
                    else:
                        l=mid+1        
                idx = l
                res[idx]=h

            # print(res)
        return len(res)
        

# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

# Note: You cannot rotate an envelope.

 

# Example 1:

# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# Example 2:

# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
 

# Constraints:

# 1 <= envelopes.length <= 105
# envelopes[i].length == 2
# 1 <= wi, hi <= 105