import sys
def maximumProfit(arr,n):
    arr.sort()
    count = 1 
    max_cost = -1 
    for i in range(n-1,-1,-1):
        curr_cost = arr[i]*count 
        if  curr_cost>max_cost:
            max_cost = curr_cost
        count+=1 
    return max_cost        
	

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr,n)
print(ans)