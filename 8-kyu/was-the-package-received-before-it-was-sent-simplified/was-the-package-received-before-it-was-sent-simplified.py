def was_package_received_yesterday(tz_from, tz_to, start, duration):
    tz_from = int(tz_from)
    tz_to = int(tz_to)
    start = int(start)
    duration = int(duration)
    
    if tz_from - tz_to == 0 or tz_from - tz_to < 0:
        return False
    elif tz_from - tz_to > 0 and tz_from - tz_to > start + duration:
        return True
    else:
        return False
    