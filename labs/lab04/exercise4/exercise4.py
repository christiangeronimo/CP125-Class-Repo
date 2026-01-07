
def analyze_performance(lap_times):
    n = len(lap_times)
    mid = (n + 1) // 2

    first_sum = 0
    for i in range(mid):
        first_sum += lap_times[i]
    first_avg = first_sum / mid

    second_sum = 0
    for i in range(mid, n):
        second_sum += lap_times[i]
    second_avg = second_sum / (n - mid)

    return second_avg > first_avg

# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True

