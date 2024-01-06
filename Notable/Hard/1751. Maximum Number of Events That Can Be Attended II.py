# 1751. Maximum Number of Events That Can Be Attended II
# Level : Hard

from pprint import pprint
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        # events = [[1,2,4],[3,4,3],[2,3,1],[4,6,5],[2,4,8]]

        events = sorted(events, key = lambda x : x[0])
        print(events)

        n = len(events)
        dp = [[0] * n for i in range(k)]
        dp[0][n-1] = events[n-1][2]

        for i in reversed(range(0,n-1)) :
            
            start = events[i][0]
            end = events[i][1]
            value = events[i][2]

            dp[0][i] = max(value, dp[0][i+1])

            imm_next = None

            for j in range(i, n) :
                if events[j][0] > end :
                    imm_next = j
                    break

            if imm_next :
                for j in range(1, k) :

                    dp[j][i] = max(value + dp[j-1][imm_next], dp[j][i+1], dp[j-1][i])
            
            else :
                for j in range(1, k) :

                    dp[j][i] = max(dp[j][i+1], dp[j-1][i])
        
        return (dp[k-1][0])
        

# You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

# You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

# Return the maximum sum of values that you can receive by attending events.

 

# Example 1:



# Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
# Output: 7
# Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
# Example 2:



# Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
# Output: 10
# Explanation: Choose event 2 for a total value of 10.
# Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
# Example 3:



# Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
# Output: 9
# Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
 

# Constraints:

# 1 <= k <= events.length
# 1 <= k * events.length <= 106
# 1 <= startDayi <= endDayi <= 109
# 1 <= valuei <= 106