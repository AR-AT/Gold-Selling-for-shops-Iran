import tkinter as tk

def calculate_gold_price():
    # Create a Tkinter window
    root = tk.Tk()
    root.title("محاسبه قیمت طلا")

    # Function to calculate gold price
    def calculate():
        # Get input values
        gold_price_18k = float(gold_price_entry.get())
        weight_grams = float(weight_entry.get())
        selling_Ojrat_percent = float(selling_Ojrat_percent_entry.get())
        seller_profit_percent = float(seller_profit_percent_entry.get())

        # Calculate raw price
        Raw_price = (gold_price_18k + (gold_price_18k*selling_Ojrat_percent/100)) * weight_grams
        # Calculate seller's profit
        seller_profit = Raw_price * seller_profit_percent/100
        # Calculate total price with profit
        seller_profit_plus_Raw_price = seller_profit + Raw_price
        # Calculate tax
        tax = (seller_profit_percent + selling_Ojrat_percent)/10 * seller_profit_plus_Raw_price/100

        # Display results
        results_label.config(text='جمع کل ارزش افزوده: {:,}\nسود: {:,}\nمالیات: {:,}\nمبلغ قابل پرداخت: {:,}'.format(
            int(seller_profit_plus_Raw_price), int(seller_profit), int(tax), int(tax + seller_profit_plus_Raw_price)))

    # Add labels and entry widgets for input
    gold_price_label = tk.Label(root, text='\u200Fقیمت هر گرم طلا: ')
    gold_price_label.grid(row=0, column=0, padx=10, pady=5)
    gold_price_entry = tk.Entry(root)
    gold_price_entry.grid(row=0, column=1, padx=10, pady=5)

    weight_label = tk.Label(root, text='\u200Fوزن طلا: ')
    weight_label.grid(row=1, column=0, padx=10, pady=5)
    weight_entry = tk.Entry(root)
    weight_entry.grid(row=1, column=1, padx=10, pady=5)

    selling_Ojrat_percent_label = tk.Label(root, text='\u200Fدرصد اجرت: ')
    selling_Ojrat_percent_label.grid(row=2, column=0, padx=10, pady=5)
    selling_Ojrat_percent_entry = tk.Entry(root)
    selling_Ojrat_percent_entry.grid(row=2, column=1, padx=10, pady=5)

    seller_profit_percent_label = tk.Label(root, text='\u200Fدرصد سود: ')
    seller_profit_percent_label.grid(row=3, column=0, padx=10, pady=5)
    seller_profit_percent_entry = tk.Entry(root)
    seller_profit_percent_entry.grid(row=3, column=1, padx=10, pady=5)

    # Add a button to trigger calculation
    calculate_button = tk.Button(root, text="محاسبه", command=calculate)
    calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Add a label to display results
    results_label = tk.Label(root, text="")
    results_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    # Run the Tkinter event loop
    root.mainloop()

# Call the function to initiate the process
calculate_gold_price()
