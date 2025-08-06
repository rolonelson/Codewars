def mul_by_n(lst, n):
    result = (x * n for x in lst)
    return list(result)
print(mul_by_n([1, 2, 3], 4))