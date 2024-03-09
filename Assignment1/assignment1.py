# importing libraries
import csv
import datetime


# function to read csv files - it reads the file and skips the header
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            data.append(row)
    return data

# The input files, to test with different files, replace the file names here
products_data = read_csv("transactions_Products.csv")
sales_data = read_csv("transactions_Sales.csv")
returns_data = read_csv("transactions_Returns.csv")


# Creating dictionaries for sales count and revenue
sales_count = {}
sales_revenue = {}


# function to count sales and revenue then stored in a dictionary
for sale in sales_data:
    product_id = sale[2]
    quantity = int(sale[3])
    discount = float(sale[4])
    if product_id not in sales_count:
        sales_count[product_id] = 0
        sales_revenue[product_id] = 0
    sales_count[product_id] += quantity
    price_per_unit = float([product[2] for product in products_data if product[0] == product_id][0])
    total_price = price_per_unit * quantity * (1 - discount)
    sales_revenue[product_id] += total_price


# accounting for returns, lower the units sold and sales revenue by count of returns and revenue
for return_id, _ in returns_data:
    for sale in sales_data:
        if sale[0] == return_id:
            product_id = sale[2]
            quantity = int(sale[3])
            sales_count[product_id] -= quantity
            price_per_unit = float([product[2] for product in products_data if product[0] == product_id][0])
            total_price = price_per_unit * quantity
            sales_revenue[product_id] -= total_price


sorted_products_by_units_sold = sorted(sales_count.items(), key=lambda x: x[1], reverse=True)
sorted_products_by_revenue = sorted(sales_revenue.items(), key=lambda x: x[1], reverse=True)

# Print the top 3 products for both units sold and revenue generated
print("1.What is the product that led to the larger number of sales in units?")
print("solution")
for product_id, units_sold in sorted_products_by_units_sold[:3]:
    product_name = [product[1] for product in products_data if product[0] == product_id][0]
    print(f"{product_name:>20} {units_sold:3}")

print("\n2.What is the product that led to the larger number of sales in dollars?")
print("solution")
for product_id, revenue in sorted_products_by_revenue[:3]:
    product_name = [product[1] for product in products_data if product[0] == product_id][0]
    formatted_revenue = "${:,.2f}".format(revenue)
    print(f"{product_name:>20} {formatted_revenue}")


turnover_data = []

for product_id, units_sold in sales_count.items():
    product_name = [product[1] for product in products_data if product[0] == product_id][0]
    price_per_unit = float([product[2] for product in products_data if product[0] == product_id][0])
    total_revenue = sales_revenue[product_id]
    if units_sold == 0:
        total_discounted_amount = 0
        average_discount_given = 0
    else:
        total_discounted_amount = total_revenue / (1 - (sales_revenue[product_id] / (price_per_unit * units_sold)))
        total_discount_given = (1 - (total_revenue / (price_per_unit * units_sold))) * 100
        average_discount_given = total_discount_given / units_sold
    formatted_revenue = "${:,.2f}".format(total_revenue)
    formatted_discounted_amount = "${:,.2f}".format(total_discounted_amount)
    turnover_data.append((product_id, product_name, units_sold, formatted_revenue, f"{average_discount_given:05.2f}%", formatted_discounted_amount))

sorted_turnover_data = sorted(turnover_data, key=lambda x: float(x[5].replace("$", "").replace(",", "")), reverse=True)

print("3.What is the turnover for all sales?")
print("solution")
print("+---+--------------------+-----+-------------+--------+-------------+")
print("| ID|        Product     |Units|    Revenue  |Avg Dis |% Discount   |")
print("+---+--------------------+-----+-------------+--------+-------------+")
for product in sorted_turnover_data:
    print(f"|{product[0]:>3}|{product[1]:^20}|{product[2]:>5}|{product[3]:>13}|{product[4]:>8}|{product[5]:>13}|")
print("+---+--------------------+-----+-------------+--------+-------------+")



transactions_per_weekday = {}

for sale in sales_data:
    date = datetime.datetime.strptime(sale[1], "%Y-%m-%d")
    weekday = date.strftime("%A")
    if weekday not in transactions_per_weekday:
        transactions_per_weekday[weekday] = 0
    transactions_per_weekday[weekday] += 1
print("4.What are the number of transactions per weekday?")
print("solution")
for weekday, count in transactions_per_weekday.items():
    print(f"{weekday[:9]:>9}:{count:3}")



returned_products = {}

for return_id, _ in returns_data:
    for sale in sales_data:
        if sale[0] == return_id:
            product_id = sale[2]
            if product_id not in returned_products:
                returned_products[product_id] = 0
            returned_products[product_id] += 1
print("5.What are the returned products?")
print("solution")
for product_id, returns in returned_products.items():
    product_name = [product[1] for product in products_data if product[0] == product_id][0]
    print(f"{product_id} {product_name:<20} {returns:3}")



print("6.What is the performance of each product?")
print("solution")
with open("transactions_units.txt", "w") as file:
    for product_id, units_sold in sales_count.items():
        file.write(f"{product_id},{units_sold}\n")
print("File transactions_units")
