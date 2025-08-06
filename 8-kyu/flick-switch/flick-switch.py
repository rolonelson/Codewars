def flick_switch(lst):
    results = []
    toggle = True
    for i in lst:
        if i == "flick":
            toggle = not toggle
        results.append(toggle)
    return results
    