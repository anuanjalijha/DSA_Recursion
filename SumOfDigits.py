def sumOfDigits(n):
    if n<10:
        return n 
    last_digit = n%10 
    remaining = n//10 
    return last_digit+sumOfDigits(remaining)
n = int(input())
print(sumOfDigits(n))        
