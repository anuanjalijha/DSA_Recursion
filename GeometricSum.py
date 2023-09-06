def geometricSum(k):
    if k==0:
        return 1 
    smallOutput = geometricSum(k-1)
    return smallOutput+1/2**k 

k = int(input())
result = geometricSum(k)
formatted_result = "{:.5f}".format(result)
print(formatted_result)
