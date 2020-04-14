def two_sum_two_arr(a, b, t):
    results = []
    for i in a:
        if t - i in b:
            results.append((i, t-i))
    return results 

# worse solution
def two_sum_two_arr2(a, b, t):
    results = []
    for i in a:
        for j in b:
            if i + j == t:
                results.append((i, j))
    return results