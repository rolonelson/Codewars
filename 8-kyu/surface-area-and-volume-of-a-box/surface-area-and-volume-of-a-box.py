def get_size(w,h,d):
    if w == h == d:
        surface_area = (w ** 2) * 6
        volume = w * h * d     
    else: 
        surface_area = (2 * ((w * h)+(w * d)+(h * d)))
        volume = w * h * d
    return [surface_area, volume]
print(get_size(10,10,10))