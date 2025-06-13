from tkinter import *
from tkinter import ttk

# Dummy conversion rates (for demonstration)
conversion_rates = {
    "USD": {"INR": 83.2, "EUR": 0.92, "USD": 1},
    "INR": {"USD": 0.012, "EUR": 0.011, "INR": 1},
    "EUR": {"USD": 1.09, "INR": 90.3, "EUR": 1}
}

def convert():
    try:
        amt = float(entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        rate = conversion_rates[from_curr][to_curr]
        result = amt * rate
        result_label.config(text=f"{amt} {from_curr} = {round(result, 2)} {to_curr}", fg="green")
    except:
        result_label.config(text="❌ Error: Invalid input", fg="red")

root = Tk()
root.title("💱 Currency Converter")
root.geometry("360x300")
root.configure(bg="#eef2f3")

# Heading
Label(root, text="Currency Converter", font=("Arial", 16, "bold"), bg="#eef2f3", fg="#333").pack(pady=10)

# Amount input
Label(root, text="Enter Amount:", font=("Arial", 12), bg="#eef2f3").pack(anchor="w", padx=30)
entry = Entry(root, font=("Arial", 12), width=25)
entry.pack(pady=5)

# From currency
Label(root, text="From Currency:", font=("Arial", 12), bg="#eef2f3").pack(anchor="w", padx=30)
from_currency = ttk.Combobox(root, font=("Arial", 12), values=["USD", "INR", "EUR"], state="readonly")
from_currency.current(0)
from_currency.pack(pady=5)

# To currency
Label(root, text="To Currency:", font=("Arial", 12), bg="#eef2f3").pack(anchor="w", padx=30)
to_currency = ttk.Combobox(root, font=("Arial", 12), values=["USD", "INR", "EUR"], state="readonly")
to_currency.current(1)
to_currency.pack(pady=5)

# Convert button
Button(root, text="Convert", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=convert).pack(pady=15)

# Result
result_label = Label(root, text="", font=("Arial", 12, "bold"), bg="#eef2f3")
result_label.pack()

root.mainloop()
