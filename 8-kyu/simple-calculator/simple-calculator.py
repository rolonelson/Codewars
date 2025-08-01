def calculator(x, y, op):
    ops = ['+', '-', '*', '/']
​
    if op not in ops:
        return "unknown value"
    try:
        float(x)
        float(y)
    except:
        return "unknown value"
    
    return eval(f"{x} {op} {y}")
print(calculator(1, "k", "*"))