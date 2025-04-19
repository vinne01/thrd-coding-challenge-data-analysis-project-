# Pricing Engine

A Python script that automatically adjusts product prices based on inventory levels and recent sales performance while ensuring a minimum profit margin.

---

## **Overview**
This pricing engine dynamically adjusts product prices using predefined business rules to optimize supply and demand. It ensures prices are always at least 20% above the cost price to maintain profitability.

---

## **Prerequisites**
- Python 3.x
- Input CSV files (`products.csv` and `sales.csv`) in the correct format (see [Input Files](#input-files)).

---

## **Input Files**

### 1. **`products.csv`**
- **Columns**:
  - `SKU` (string): Unique identifier for the product.
  - `current_price` (float): Current selling price of the product.
  - `cost_price` (float): Cost price of the product.
  - `stock` (int): Current inventory count.

### 2. **`sales.csv`**
- **Columns**:
  - `SKU` (string): Unique identifier for the product.
  - `quantity_sold` (int): Number of units sold in the last 30 days.

**Note**: If a product exists in `products.csv` but not in `sales.csv`, its `quantity_sold` defaults to `0`.

---

## **Usage**
1. **Place Input Files**:  
   Ensure `products.csv` and `sales.csv` are in the same directory as the script.

2. **Run the Script**:
   ```bash
   python pricing_engine.py
