def replaceChar(s,a,b):
    l = len(s)
    if l==0:
        return s  # Base case: empty string
    smallOutput = replaceChar(s[1:],a,b)    
    
    if s[0] == a:
        return b+smallOutput  # Skip the 'x' character and continue with the rest
    else:
        return s[0] + smallOutput  # Keep the current character and continue with the rest

# Test the function
input_string = "xabcdefgg"
a = 'g'
b = 'y'
result = replaceChar(input_string,a,b)
print(result)  # Output: "ample string"
