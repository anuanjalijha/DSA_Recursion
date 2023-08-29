def fact(n):
    if n == 0:
        return 1 
    smallOutput = fact(n-1)
    return n*smallOutput
n = int(input())
result = fact(n)
print(result)