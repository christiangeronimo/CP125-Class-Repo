def find_largest_drop(temps):
    max_drop = 0.0

    for i in range(1, len(temps)):
        previous = temps[i - 1]
        current = temps[i]

        if current < previous:
            drop = previous - current
            if drop > max_drop:
                max_drop = drop

    return max_drop


# Test
temps = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(temps)
print("Largest Drop:", result)
