from functools import wraps


def large_length(func):
    @wraps(func)
    def wrapper(line_one, line_two):
        if len(line_one) > len(line_two):
            return func(line_two, line_one)

        if len(line_one) == 0 or len(line_two) == 0:
            return 0
        else:
            return func(line_one, line_two)

    return wrapper


@large_length
def Lev(line_one, line_two):
    n, m = len(line_one), len(line_two)
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if line_one[j - 1] != line_two[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[-1]




