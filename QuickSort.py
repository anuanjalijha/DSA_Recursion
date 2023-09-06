from typing import List
def partition(arr,startIndex,endIndex):
    pivot = arr[startIndex]
    c = 0
    for i in range(startIndex,endIndex+1):
        if arr[i]<pivot:
            c= c+1
    arr[startIndex+c],arr[startIndex]= arr[startIndex],arr[startIndex+c]
    pivot_index = startIndex+c
    i = startIndex
    j = endIndex 
    while i<j:

        if arr[i]<pivot:
           i+=1 
        elif arr[j]>=pivot:
            j-=1 
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    return pivot_index               



def quickSort(arr: List[int], startIndex: int, endIndex: int):
    if startIndex>=endIndex:
        return 
    pivot_index = partition(arr,startIndex,endIndex)
    quickSort(arr,startIndex,pivot_index-1) 
    quickSort(arr,pivot_index+1,endIndex)   
