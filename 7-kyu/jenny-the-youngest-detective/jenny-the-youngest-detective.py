def missing(nums, s):
    try:
        s = s.replace(" ", "")
        nums = sorted(nums)
        return "".join([s[i] for i in nums]).lower()
    
    except IndexError:
        return "No mission today"
    except:
        s == "Good Morning"
        return "No mission today"