import numpy as np
import matplotlib.pyplot as plt

inventory = np.array([], dtype=[('name', 'U50'), ('price', 'f4'), ('quantity', 'i4')])
sales = []  

def display_inventory():
    print("Current Inventory:")
    print("Name\tPrice\tQuantity")
    for item in inventory:
        print(f"{item['name']}\t{item['price']}\t{item['quantity']}")

def add_item(name, price, quantity):
    global inventory
    new_item = np.array([(name, price, quantity)], dtype=inventory.dtype)
    inventory = np.concatenate((inventory, new_item))

def update_quantity(name, quantity_sold):
    global inventory
    for i, item in enumerate(inventory):
        if item['name'] == name:
            if inventory[i]['quantity'] >= quantity_sold:
                inventory[i]['quantity'] -= quantity_sold
                print(f"Updated {name}: New quantity is {inventory[i]['quantity']}")
                return  
            else:
                print("Not enough stock")
                return  

def calculate_sales_profits():
    total_sales = 0
    total_profit = 0
    for name, quantity_sold in sales:
        for item in inventory:
            if item['name'] == name:
                sale_amount = item['price'] * quantity_sold
                profit = sale_amount * 0.1
                total_sales += sale_amount
                total_profit += profit
    return total_sales, total_profit

def scatter_plot(sales, profits):
    days = np.arange(1, len(sales) + 1)
    plt.scatter(days, sales, color="blue", label="Sales")
    plt.scatter(days, profits, color="green", label="Profits")
    plt.xlabel('Days')
    plt.ylabel('Amount')
    plt.title('Scatter Chart of Sales')
    plt.legend()
    plt.show()


add_item("paracetamol", 10.0, 100)
display_inventory()
sales
