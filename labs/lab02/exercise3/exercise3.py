# Lab 02 Exercise 3: Secure Vault System
# Write your code below:

def validate_entry(name, pin):
    if name == "Director" and pin == 1122:
        return True

    
    if name == "Security" and pin == 9900:
        return True
    
    return False