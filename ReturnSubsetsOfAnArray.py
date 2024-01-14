from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def subsets(arr):
    if len(arr) == 0:
        return [[]]

    smallerArr = arr[1:]
    smallerOutput = subsets(smallerArr)

    output = []
    for sub in smallerOutput:
        output.append(sub)

    for sub in smallerOutput:
        sub_with_zeroth = [arr[0]] + sub  # Create a new list for each subset
        output.append(sub_with_zeroth)

    return output

# Read input
n = int(input())
arr = list(map(int, input().strip().split(' ')))
output = subsets(arr)

# Print all subsets
for subset in output:
    print(*subset)
