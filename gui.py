import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Define the gas prices and initial IVA tax rate
GAS_PRICES = {
    "Regular": 1.742,
    "Premium": 1.885,
    "Diesel": 1.681,
    "Diesel A+": 1.780,
    "Premium 100": 1.489
}

# Function to calculate the cost
def calculate_cost():
    # Get user inputs
    fuel_type = fuel_var.get()
    quantity_text = quantity_entry.get()
    iva_rate = iva_entry.get()

    try:
        # Check if the quantity input is empty
        if not quantity_text:
            raise ValueError("Please enter a valid quantity.")

        quantity = float(quantity_text)
        price_per_liter = GAS_PRICES.get(fuel_type, 0)
        iva_rate = float(iva_rate) / 100  # Convert IVA rate from percentage to decimal

        # Calculate the total cost and IVA tax amount
        total_cost = round(price_per_liter * quantity * (1 + iva_rate), 2)
        iva_amount = round(total_cost - (total_cost / (1 + iva_rate)), 2)

        receipt_type = receipt_type_var.get()

        client_name = name_entry.get()
        client_address = address_entry.get()
        client_dni = dni_entry.get()
        client_postal_code = postal_code_entry.get()
        client_phone = phone_entry.get()

        # Prepare the receipt text based on the selected receipt type
        if receipt_type == "Simple":
            receipt = f"      Fuel Type: {fuel_type}\n"
            receipt += f"        Quantity (liters): {quantity}\n"
            receipt += f"           Price per Liter: €{price_per_liter:.3f}\n"
            receipt += f"    Total Cost: €{total_cost:.2f}\n"
            receipt += f"              IVA Tax ({iva_rate * 100}%): €{iva_amount:.2f}\n"
        else:
            receipt = f"          Fuel Type: {fuel_type}\n"
            receipt += f"            Quantity (liters): {quantity}\n"
            receipt += f"               Price per Liter: €{price_per_liter:.3f}\n"
            receipt += f"        Total Cost: €{total_cost:.2f}\n"
            receipt += f"                 IVA Tax ({iva_rate * 100}%): €{iva_amount:.2f}\n"
            receipt += f"    Name: {client_name}\n"
            receipt += f"       Address: {client_address}\n"
            receipt += f"DNI: {client_dni}\n"
            receipt += f"             Postal Code: {client_postal_code}\n"
            receipt += f"    Phone: {client_phone}"

        # Update the result label with the receipt text
        result_label.config(text=receipt, font=("Arial", 14))

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Function to clear input fields
def clear_fields():
    fuel_var.set("")  # Clear the selected fuel type
    quantity_entry.delete(0, "end")  # Clear the quantity input field
    receipt_type_var.set("")  # Clear the receipt type selection
    name_entry.delete(0, "end")  # Clear the client name input field
    address_entry.delete(0, "end")  # Clear the client address input field
    dni_entry.delete(0, "end")  # Clear the client DNI input field
    postal_code_entry.delete(0, "end")  # Clear the client postal code input field
    phone_entry.delete(0, "end")  # Clear the client phone number input field

# Function to save receipt to a file
def save_receipt():
    receipt_text = result_label.cget("text")
    if not receipt_text:
        messagebox.showerror("Save Error", "No receipt to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(receipt_text)
        messagebox.showinfo("Save Successful", "Receipt saved successfully.")

# Create the main window
window = tk.Tk()
window.title("Shell Petrol Station")
window.geometry("600x600")

# Create and position widgets using grid layout
label_font = ("Arial", 14)
entry_font = ("Arial", 14)

# Initialize the row counter
row = 0

# Create and position widgets for user input
tk.Label(window, text="\nSelect Fuel Type:\n", font=label_font).grid(row=row, column=0, sticky="w")
fuel_var = tk.StringVar()
fuel_dropdown = tk.OptionMenu(window, fuel_var, *GAS_PRICES.keys())
fuel_dropdown.grid(row=row, column=1)
row += 1

# Display fuel prices
for fuel_type, price in GAS_PRICES.items():
    tk.Label(window, text=f"{fuel_type} Price (€/L): {price:.3f}", font=label_font).grid(row=row, column=0, sticky="w")
    row += 1

tk.Label(window, text="\nEnter Quantity (Liters):", font=label_font).grid(row=row, column=0, sticky="w")
quantity_entry = tk.Entry(window)
quantity_entry.grid(row=row, column=1)
row += 1

tk.Label(window, text="Select Receipt Type:\n", font=label_font).grid(row=row, column=0, sticky="w")
receipt_type_var = tk.StringVar()
receipt_type_dropdown = tk.OptionMenu(window, receipt_type_var, "Simple", "Detailed")
receipt_type_dropdown.grid(row=row, column=1)
row += 1

tk.Label(window, text="Name:", font=label_font).grid(row=row, column=0, sticky="w")
name_entry = tk.Entry(window)
name_entry.grid(row=row, column=1)
row += 1

tk.Label(window, text="Address:", font=label_font).grid(row=row, column=0, sticky="w")
address_entry = tk.Entry(window)
address_entry.grid(row=row, column=1)
row += 1

tk.Label(window, text="DNI:", font=label_font).grid(row=row, column=0, sticky="w")
dni_entry = tk.Entry(window)
dni_entry.grid(row=row, column=1)
row += 1

tk.Label(window, text="Postal Code:", font=label_font).grid(row=row, column=0, sticky="w")
postal_code_entry = tk.Entry(window)
postal_code_entry.grid(row=row, column=1)
row += 1

tk.Label(window, text="Phone Number:", font=label_font).grid(row=row, column=0, sticky="w")
phone_entry = tk.Entry(window)
phone_entry.grid(row=row, column=1)
row += 1

tk.Label(window, text="IVA Rate (%):", font=label_font).grid(row=row, column=0, sticky="w")
iva_entry = tk.Entry(window)
iva_entry.insert(0, "21")  # Set the default value
iva_entry.grid(row=row, column=1)
row += 1

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_cost, font=("Arial", 14))
calculate_button.grid(row=row, column=0, pady=(20, 0))

# Create the clear button
clear_button = tk.Button(window, text="Clear", command=clear_fields, font=("Arial", 14))
clear_button.grid(row=row, column=1, pady=(20, 0))

# Create the save receipt button
save_button = tk.Button(window, text="Save Receipt", command=save_receipt, font=("Arial", 14))
save_button.grid(row=row, column=2, pady=(20, 0))

# Create and position the result label to display the cost
result_label = tk.Label(window, text="Cost: €0.00", font=("Arial", 14))
result_label.grid(row=row + 1, column=0, columnspan=3, pady=(10, 20))

# Start the GUI main loop
window.mainloop()
