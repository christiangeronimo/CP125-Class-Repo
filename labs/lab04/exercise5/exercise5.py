def find_momentum_days(prices):
    momentum_days = []
    for day in range(2, len(prices)):
        today_change = prices[day] - prices[day - 1]
        prev_change = prices[day - 1] - prices[day - 2]

        if today_change > 0 and today_change > prev_change:
            momentum_days.append(day)

    return momentum_days

        

# Test
prices = [100, 102, 105, 107, 106, 108, 112, 114]
result = find_momentum_days(prices)
print(f"Momentum days: {result}")  # Expected: [2, 5, 6]
