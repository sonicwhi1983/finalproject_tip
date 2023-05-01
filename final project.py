import tkinter as tk

def calculate_tip():
    bill_amount = float(bill_entry.get())
    tip_percentage = float(tip_percentage_entry.get()) / 100
    tip_amount = bill_amount * tip_percentage
    total_amount = bill_amount + tip_amount
    tip_amount_label.config(text=f"Tip Amount: ${tip_amount:.2f}")
    total_amount_label.config(text=f"Total Amount: ${total_amount:.2f}")

def clear_entries():
    bill_entry.delete(0, tk.END)
    tip_percentage_entry.delete(0, tk.END)
    tip_amount_label.config(text="Tip Amount: ")
    total_amount_label.config(text="Total Amount: ")

root = tk.Tk()
root.title("Tip Calculator")

# Create UI elements
bill_label = tk.Label(root, text="Bill Amount:")
bill_label.pack()

bill_entry = tk.Entry(root)
bill_entry.pack()

tip_percentage_label = tk.Label(root, text="Tip Percentage:")
tip_percentage_label.pack()

tip_percentage_entry = tk.Entry(root)
tip_percentage_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_tip)
calculate_button.pack()

tip_amount_label = tk.Label(root, text="Tip Amount: ")
tip_amount_label.pack()

total_amount_label = tk.Label(root, text="Total Amount: ")
total_amount_label.pack()

clear_button = tk.Button(root, text="Clear", command=clear_entries)
clear_button.pack()

root.mainloop()
