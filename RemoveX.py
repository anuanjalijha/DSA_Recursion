def removeX(s):
    l = len(s)
    if l==0:
        return ""  # Base case: empty string
    
    if s[0] == 'x':
        return removeX(s[1:])  # Skip the 'x' character and continue with the rest
    else:
        return s[0] + removeX(s[1:])  # Keep the current character and continue with the rest
       

# Main
string = input()
print(removeX(string))
