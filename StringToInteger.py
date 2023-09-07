def string_to_integer_recursive(s):
    # Base case: If the string is empty, return 0
    if not s:
        return 0
    
    # Recursive case: Convert the substring excluding the last character to an integer
    # and multiply it by 10, then add the integer value of the last character.
    return string_to_integer_recursive(s[:-1]) * 10 + int(s[-1])

# Example usage:
numeric_string = input()
result = string_to_integer_recursive(numeric_string)
print(result)
