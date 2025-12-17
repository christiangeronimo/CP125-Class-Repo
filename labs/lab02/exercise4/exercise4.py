# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
    if vehicle_type == "Electric":
        return 2
    if vehicle_type == "Hybrid" and 6 >= hour_24 or hour_24 >= 22:
        return 2
    if vehicle_type == "Other":
        return 5
    
    return 5 
      
