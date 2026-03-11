# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv

def calculate_order_total(products_file, order_file, output_file):
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    prices = {}
    f = open(products_file, 'r', newline='') 
    reader = csv.reader(f)
    next(reader)
    for row in reader:
            product_id = row[0]
            price = float(row[2])
            prices[product_id] = price

    grand_total = 0.0

 
    g = open(order_file, 'r', newline='')
    out = open(output_file, 'w', newline='')

    order_reader = csv.reader(g)
    writer = csv.writer(out)

    next(order_reader)  

    writer.writerow(["product_id", "total_cost"])

    for row in order_reader:
            product_id = row[0]
            quantity = int(row[1])

            total_cost = prices[product_id] * quantity
            grand_total += total_cost

            writer.writerow([product_id, f"{total_cost:.2f}"])

    return grand_total


# Test your code here
result = calculate_order_total(
    "labs/lab08/exercise3/data/products.csv",
    "labs/lab08/exercise3/data/order.csv",
    "labs/lab08/exercise3/data/total.csv"
)

print(f"Grand total: ${result:.2f}")
