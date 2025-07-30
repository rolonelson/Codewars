def multiples(m, n):
    results = []
    for i in range(1, m + 1):
        results.append(i * n)
    return results
print(multiples(10, 5.0))