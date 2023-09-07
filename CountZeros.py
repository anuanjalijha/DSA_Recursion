def countZeros(n):
    if n<10:
        if n==0:
            return 1 
        else:
            return 0 
    last_digit = n%10 
    remaining = n//10
    smallOutput = countZeros(remaining)
    if last_digit==0:
        return smallOutput+1 
    else:
        return smallOutput 

n = int(input())
print(countZeros(n))                        
