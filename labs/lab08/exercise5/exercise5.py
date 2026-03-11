# Lab 08 Exercise 5: Sales Summary
# Write your code below:
import csv

def summarize_sales(input_file, output_file):
    """
    Calculate sales statistics: total, average, highest, and lowest revenue.
    """

    f = open(input_file, 'r', newline='')
    reader = csv.reader(f)
    next(reader)  # skip header

    total = 0.0
    count = 0
    highest = 0.0
    lowest = None

    for row in reader:
        product = row[0]
        quantity = int(row[1])
        price = float(row[2])

        revenue = quantity * price

        total += revenue
        count += 1

        if revenue > highest:
            highest = revenue

        if lowest is None or revenue < lowest:
            lowest = revenue

    f.close()

    average = total / count if count > 0 else 0.0

    out = open(output_file, 'w')
    out.write(f"Total Revenue: ${total:.2f}\n")
    out.write(f"Average Revenue: ${average:.2f}\n")
    out.write(f"Highest Revenue: ${highest:.2f}\n")
    out.write(f"Lowest Revenue: ${lowest:.2f}\n")
    out.close()

    return (total, average, highest, lowest)


# Test your code here
result = summarize_sales("data/sales.csv", "data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")