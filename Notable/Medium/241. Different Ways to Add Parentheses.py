# 241. Different Ways to Add Parentheses
# Level : Medium 

from typing import *
# from pprint import pprint

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def get_calc(x: list, y: list, s: str) :
            r = []
            for i in x :
                for j in y :
                    if s == '+' :
                        r.append(i+j)
                    elif s=='-' :
                        r.append(i-j)
                    else :
                        r.append(i*j)
            return r

        signs = {}
        nums = []

        t = ''
        x = 0.5
        for i in range(len(expression)) :
            if expression[i] in '+-*' :
                nums.append(int(t))
                signs[x] = expression[i]
                x += 1
                t = ''
            else :
                t += expression[i]
        nums.append(int(t))
        
        # print(signs)

        left = [[None] * len(nums) for i in range(len(nums))]
        right = [[None] * len(nums) for i in range(len(nums))]

        for i in range(len(nums)) :
            left[0][i] = [nums[i]]
            right[0][i] = [nums[i]]

        keys = list(signs.keys())
        
        for i in range(1, len(left)) :
            res = []
            y = 0

            left_insert = i
            right_insert = 0

            while y+i < len(nums) :
                tc = []
                l_i = 0
                r_i = i-1
                for x in range(y, y+i) :
                    sign = signs[keys[x]]
                    l = left[l_i][math.floor(keys[x])]
                    r = right[r_i][math.ceil(keys[x])]
                    tc += get_calc(l,r,sign)
                    # print(l, sign, r)
                    l_i+=1
                    r_i-=1
                # print(tc, '\n')
                left[i][left_insert] = tc
                right[i][right_insert] = tc
                left_insert += 1
                right_insert += 1
                y+=1



        # pprint(left)
        # pprint(right)

        return right[-1][0]



# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

# Example 1:

# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
 

# Constraints:

# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.
# All the integer values in the input expression are in the range [0, 99].