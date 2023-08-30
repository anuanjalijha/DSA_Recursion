def checkNumber(arr, x):
    if not arr:
        return False
    if arr[0]==x:
        return True
    return checkNumber(arr[1:], x)    
