
def was_backward_detected(path):
    for i in range(1, len(path)):
        x1 , y1 , z1 = path [i - 1]
        x2 , y2 , z2 = path [i]

        if x2 < x1 or y2 < y1 :
            return True 
    return False 


# Test
path = ((0, 0, 10), (5, 5, 12), (4, 6, 10), (10, 10, 15))
result = was_backward_detected(path)
print(f"Backward Movement: {result}")  # Expected: True
