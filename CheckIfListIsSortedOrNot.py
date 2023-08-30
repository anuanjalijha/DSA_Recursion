def isSortedBetter(a,si):
    l = len(a)
    if si==l-1 or si == l:
        return True 
    if a[si]>a[si+1]:
        return False
    isSmallerPartSorted = isSortedBetter(a,si+1)
    return isSmallerPartSorted

a = [1, 2, 3, 4]
result = isSortedBetter(a,0)
print(result)
