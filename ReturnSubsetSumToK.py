import sys
sys.setrecursionlimit(10 ** 8)

def helper(arr, k, si):
    if si == len(arr):
        if k == 0:
            return [[]]
        else:
            return []

    op1 = helper(arr, k - arr[si], si + 1)
    op2 = helper(arr, k, si + 1)

    output = op2
    for sublist in op1:
        new_sublist = [arr[si], ]
        new_sublist.extend(sublist)
        output.append(new_sublist)

    return output



def subsetsSumK(arr, k) :
    return helper(arr, k, 0)

    #Your code goes here























#taking input
def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


#printing the list of lists
def printListOfList(liOfLi) :
    for li in liOfLi :
        for elem in li :
            print(elem, end = " ")
        print()

#main
arr, n = takeInput()

if n != 0 :
    k = int(input().strip())
    liOfLi = subsetsSumK(arr, k)

    printListOfList(liOfLi)

