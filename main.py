import csv

# Read products data
products = []
with open('products.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = {
            'sku': row['sku'],
            'current_price': float(row['current_price']),
            'cost_price': float(row['cost_price']),
            'stock': int(row['stock'])
        }
        products.append(product)

# Read sales data and create a dictionary for quick lookup
sales_data = {}
with open('sales.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        sales_data[row['sku']] = int(row['quantity_sold'])

# Merge sales data with products
for product in products:
    sku = product['sku']
    product['quantity_sold'] = sales_data.get(sku, 0)

# Process each product to determine new price
updated_prices = []
for product in products:
    sku = product['sku']
    old_price = product['current_price']
    cost = product['cost_price']
    stock = product['stock']
    qty_sold = product['quantity_sold']
    
    new_price = old_price  # Default to old price if no rules apply
    
    # Rule 1: Low Stock, High Demand
    if stock < 20 and qty_sold > 30:
        new_price *= 1.15
    else:
        # Rule 2: Dead Stock
        if stock > 200 and qty_sold == 0:
            new_price *= 0.7
        else:
            # Rule 3: Overstocked Inventory
            if stock > 100 and qty_sold < 20:
                new_price *= 0.9
    
    # Rule 4: Minimum Profit Constraint
    min_price = cost * 1.2
    if new_price < min_price:
        new_price = min_price
    
    # Round to two decimal places
    new_price = round(new_price, 2)
    
    updated_prices.append({
        'sku': sku,
        'old_price': old_price,
        'new_price': new_price
    })

# Write the updated prices to CSV
with open('updated_prices.csv', 'w', newline='') as f:
    fieldnames = ['sku', 'old_price', 'new_price']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for entry in updated_prices:
        writer.writerow({
            'sku': entry['sku'],
            'old_price': "{0:.2f}".format(entry['old_price']),
            'new_price': "{0:.2f}".format(entry['new_price'])
        })
