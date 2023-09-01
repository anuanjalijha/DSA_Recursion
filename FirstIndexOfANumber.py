def firstIndex(arr, x,si):
    l = len(arr)
    if si==l-1 or si==l:
        return -1
    if arr[si]==x:
        return si 
    is_smaller = firstIndex(arr,x,si+1)
    return is_smaller        
