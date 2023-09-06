def product( M , N ):
    # if x is less than y swap
    # the numbers
    if M < N:
        return product(N, M)
      
    # iteratively calculate y
    # times sum of x
    elif N!= 0:
        return (M + product(M, N - 1))
      
    # if any of the two numbers is
    # zero return zero
    else:
        return 0
M = int(input())
N = int(input())
print(product(M,N))        
