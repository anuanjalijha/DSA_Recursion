def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n)
n = int(input())
result = print_1_to_n(n)
print(result)