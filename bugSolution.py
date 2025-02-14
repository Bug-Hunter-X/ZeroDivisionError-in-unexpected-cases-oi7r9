def function_with_uncommon_error(a, b):
    if a == 0 or b == 0:
        return 0  # Handle zero division gracefully, preventing errors
    else:
        return a / b

result = function_with_uncommon_error(0, 10) 
print(result) # Output: 0 
result2 = function_with_uncommon_error(10, 0)
print(result2) # Output: 0