def lastIndex(arr,x,si):
    l = len(arr)
    if si==l:
        return -1 
    smaller_output = lastIndex(arr,x,si+1)
    if smaller_output!=-1:
        return smaller_output
    else:
        if arr[si]==x:
            return si 
        else:
            return -1      
