# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    total_tent = math.ceil(participants / tent_capacity)
    tent_cost = total_tent * tent_price

    meal_cost = meal_price * participants 
    total_cost = meal_cost + tent_cost
    return total_cost
   
    # TODO: Implement this function
    # Calculate total cost for tents and meals



# Test your code here
#print(calculate_event_cost())
