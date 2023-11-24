import tkinter as tk
import math

def compute_amount_apple_orange():
    apple_quantity = int(apple_entry.get())
    orange_quantity = int(orange_entry.get())
    apple_price = 20
    orange_price = 25
    amount = (apple_price * apple_quantity) + (orange_price * orange_quantity)
    result_label.config(text=f"You can buy {apple_quantity} apples and {orange_quantity} oranges with {amount} pesos.")

root = tk.Tk()
root.title("Apple and Orange Calculator")

apple_label = tk.Label(root, text="How many apples do you want: ")
apple_label.pack()

apple_entry = tk.Entry(root)
apple_entry.pack()

orange_label = tk.Label(root, text="How many oranges do you want: ")
orange_label.pack()

orange_entry = tk.Entry(root)
orange_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=compute_amount_apple_orange)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
compute_amount_apple_orange()