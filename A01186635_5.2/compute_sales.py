"""
Module: compute_sales.py
This script reads a price catalogue and sales records from JSON files,
calculates the total cost of all sales, and outputs the results in a human-readable format.
Results are printed to the console and saved to 'SalesResults.txt'.
"""

import sys
import time
import json

def read_json_file(filename):
    """Reads and parses a JSON file, handling errors gracefully."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'.")
        sys.exit(1)
    except (OSError, IOError) as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def build_price_catalogue(product_catalog):
    """Builds a dictionary mapping product titles to their prices."""
    return {product["title"]: product["price"] for product in product_catalog}

def compute_total_sales(price_catalogue, sales_records):
    """Computes the total sales cost based on price catalogue and sales records."""
    total_sales = 0.0
    itemized_totals = []

    for sale in sales_records:
        product = sale.get("Product")
        quantity = sale.get("Quantity", 0)

        if product not in price_catalogue:
            print(f"Warning: Product '{product}' not found in price catalogue. Skipping.")
            continue

        price = price_catalogue[product]
        total_cost = price * quantity
        total_sales += total_cost
        itemized_totals.append(f"{product}: {quantity} x {price} = {total_cost:.2f}")

    return total_sales, itemized_totals

def write_results_to_file(results, elapsed_time):
    """Writes total sales results to an output file."""
    with open('SalesResults.txt', 'w', encoding='utf-8') as file:
        file.write(results + f"\nExecution Time: {elapsed_time:.4f} seconds\n")

def main():
    """Main function to handle file reading, computation, and output."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py <priceCatalogue.json> <salesRecord.json>")
        sys.exit(1)

    price_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]
    start_time = time.time()

    product_catalog = read_json_file(price_catalogue_file)
    price_catalogue = build_price_catalogue(product_catalog)
    sales_records = read_json_file(sales_record_file)

    total_sales, itemized_totals = compute_total_sales(price_catalogue, sales_records)

    results = "Sales Summary:\n" + "\n".join(itemized_totals) + f"\nTotal Sales: {total_sales:.2f}"
    print(results)

    elapsed_time = time.time() - start_time
    print(f"Execution Time: {elapsed_time:.4f} seconds")
    write_results_to_file(results, elapsed_time)

if __name__ == "__main__":
    main()
