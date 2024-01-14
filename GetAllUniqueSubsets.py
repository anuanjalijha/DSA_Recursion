from math import *
from collections import *
from sys import *
from os import *
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        smallerArr = nums[1:]
        smallerOutput = self.subsetsWithDup(smallerArr)

        output = []
        for sub in smallerOutput:
            output.append(sub)

        for sub in smallerOutput:
            sub_with_zeroth = [nums[0]] + sub  # Create a new list for each subset
            output.append(sub_with_zeroth)
        output = [list(subset) for subset in set(map(tuple, output))]   

        return output

        # write the code  logic here !!! 

if __name__ == "__main__":
    n= int (input())
    nums=list(map(int, input().split()))  
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()