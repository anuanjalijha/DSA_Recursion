def sum(n):
    if n == 0:
        return 0 
    smallOutput = sum(n-1)
    output =  n+smallOutput
    return output
n = int(input())
result = sum(n)
print(result)