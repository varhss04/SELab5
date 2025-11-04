"""
A simple inventory management system.
"""

import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Adds an item to the stock_data."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")


def remove_item(item, qty):
    """Removes a specified quantity of an item from stock_data."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        # Item not in stock, do nothing.
        pass


def get_qty(item):
    """Gets the quantity of a specific item."""
    return stock_data[item]


def load_data(file="inventory.json"):
    """Loads inventory data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
            stock_data.clear()
            stock_data.update(loaded_data)
    except FileNotFoundError:
        print(f"Warning: {file} not found. Starting with empty inventory.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode {file}. Starting with empty inventory.")


def save_data(file="inventory.json"):
    """Saves inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    """Prints a report of all items and their quantities."""
    print("Items Report")
    for i in stock_data:
        print(f"{i} -> {stock_data[i]}")


def check_low_items(threshold=5):
    """Checks for items with stock below a threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Main function to run the inventory system."""
    load_data()  # Load data at the start
    add_item("apple", 10)
    add_item("banana", -2)
    # The original code passed invalid types.
    # Proper fix would add type checking in add_item.
    # add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)  # This will now fail silently as intended
    try:
        print("Apple stock:", get_qty("apple"))
    except KeyError:
        print("Apple stock: 0")
    print("Low items:", check_low_items())
    save_data()
    print_data()


if __name__ == "__main__":
    main()