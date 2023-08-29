def powerOfANumber(x,n):
    if n == 1:
        return x 
    if n == 0:
        return 1 
    return x*powerOfANumber(x,n-1)        
    

x, n = input().split()
x = int(x)
n = int(n)
d = powerOfANumber(x,n)
print(d)