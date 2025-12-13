# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):

    round_trip_km = one_way_km * 2
    liters_needed = round_trip_km / km_per_liter
    trip_cost = liters_needed * price_per_liter
    return trip_cost <= budget


