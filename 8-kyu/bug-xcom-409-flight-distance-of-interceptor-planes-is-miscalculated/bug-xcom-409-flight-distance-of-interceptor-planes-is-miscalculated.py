# speed of aircrafts is given in *knots*
# travelTime is in *minutes*
# travel distance should be returned in *kilometers*
​
def travel_distance(avg_speed, travel_time):
    KM_PER_MILE = 1.609344
    MILE_PER_KNOT = 1.15078
    travel_hours = travel_time / 60 
    travel_miles = (avg_speed * MILE_PER_KNOT) * travel_hours
    travel_kms = travel_miles * KM_PER_MILE
    return travel_kms