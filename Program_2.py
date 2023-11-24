import tkinter as tk
import math

def compute_apple_price():
    money_available = int(money_entry.get())
    apple_price = int(price_entry.get())
    max_apples = money_available // apple_price
    remaining_money = money_available - (max_apples * apple_price)
    result_label.config(text=f"You can buy {max_apples} apples and will have {remaining_money} pesos left.")

root = tk.Tk()
root.title("Apple Price Calculator")

money_label = tk.Label(root, text="How much money do you have right now: ")
money_label.grid(row=0, column=0)

money_entry = tk.Entry(root)
money_entry.grid(row=0, column=1)

price_label = tk.Label(root, text="What is the price of an apple: ")
price_label.grid(row=1, column=0)

price_entry = tk.Entry(root)
price_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate", command=compute_apple_price)
calculate_button.grid(row=2, column=0)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=1)

root.mainloop()
compute_apple_price()