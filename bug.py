def function_with_uncommon_error(a, b):
    if a == 0:
        return b / a
    else:
        return a / b

result = function_with_uncommon_error(0, 10)