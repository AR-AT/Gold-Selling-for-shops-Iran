import tkinter as tk

def calculate_gold_price():
    # Create a Tkinter window
    root = tk.Tk()
    root.title("محاسبه قیمت طلا")

    # Function to calculate gold price for the first panel
    def calculate_first(panel):
        # Get input values
        gold_price_18k = float(gold_price_entries[panel].get())
        weight_grams = float(weight_entries[panel].get())
        selling_Ojrat_percent = float(selling_Ojrat_percent_entries[panel].get())
        seller_profit_percent = float(seller_profit_percent_entries[panel].get())

        # Calculate raw price
        Raw_price = (gold_price_18k + (gold_price_18k * selling_Ojrat_percent / 100)) * weight_grams
        # Calculate seller's profit
        seller_profit = Raw_price * seller_profit_percent / 100
        # Calculate total price with profit
        seller_profit_plus_Raw_price = seller_profit + Raw_price
        # Calculate tax
        tax = (seller_profit_percent + selling_Ojrat_percent) / 10 * seller_profit_plus_Raw_price / 100

        # Display results
        results_labels[panel].config(text='جمع کل ارزش افزوده: {:,}\nسود: {:,}\nمالیات: {:,}\nمبلغ قابل پرداخت: {:,}'.format(
            int(seller_profit_plus_Raw_price), int(seller_profit), int(tax), int(tax + seller_profit_plus_Raw_price)))

    # Placeholder function for the second calculation
    def calculate_second(panel):
        # Get input values
        gold_price_18k = float(gold_price_entries[panel].get())
        weight_grams = float(weight_entries[panel].get())
        reduction_percent = float(reduction_percent_entries[panel].get())

        # Placeholder for the actual calculation logic
        # Calculate the total price after reduction
        reduced_price = gold_price_18k * weight_grams * (1 - reduction_percent / 100)

        # Display results
        results_labels[panel].config(text='مبلغ قابل پرداخت: {:,}'.format(int(reduced_price)))

    # Placeholder function for the third calculation
    def calculate_third(panel):
        # Get input values
        gold_price_18k = float(gold_price_entries[panel].get())
        weight_grams = float(weight_entries[panel].get())
        profit_percent = float(profit_percent_entries[panel].get())

        # Placeholder for the actual calculation logic
        # Calculate the total price with profit
        total_price = gold_price_18k * weight_grams
        profit = total_price * profit_percent / 100
        final_price = total_price + profit

        # Display results
        results_labels[panel].config(text='مبلغ قابل پرداخت: {:,}\nسود: {:,}'.format(int(final_price), int(profit)))

    # Create three panels
    panels = []
    for i in range(3):
        panel = tk.Frame(root, padx=10, pady=10, bd=2, relief=tk.GROOVE)
        panel.grid(row=1, column=i, padx=10, pady=10)
        panels.append(panel)

    # Define dictionaries to hold entry and label widgets
    gold_price_entries = {}
    weight_entries = {}
    selling_Ojrat_percent_entries = {}
    seller_profit_percent_entries = {}
    reduction_percent_entries = {}
    profit_percent_entries = {}
    results_labels = {}

    titles = ['فروش طلای نو','خرید طلای کهنه','فروش طلای کهنه']

    for i in range(3):
        # Add a title above each panel
        title_label = tk.Label(root, text=titles[i], font=("Helvetica", 14))
        title_label.grid(row=0, column=i, padx=10, pady=10)

        # Add labels and entry widgets for input in each panel
        gold_price_label = tk.Label(panels[i], text='\u200Fقیمت هر گرم طلا: ')
        gold_price_label.grid(row=0, column=0, padx=10, pady=5)
        gold_price_entry = tk.Entry(panels[i])
        gold_price_entry.grid(row=0, column=1, padx=10, pady=5)
        gold_price_entries[i] = gold_price_entry

        weight_label = tk.Label(panels[i], text='\u200Fوزن طلا: ')
        weight_label.grid(row=1, column=0, padx=10, pady=5)
        weight_entry = tk.Entry(panels[i])
        weight_entry.grid(row=1, column=1, padx=10, pady=5)
        weight_entries[i] = weight_entry

        if i == 0:
            selling_Ojrat_percent_label = tk.Label(panels[i], text='\u200Fدرصد اجرت: ')
            selling_Ojrat_percent_label.grid(row=2, column=0, padx=10, pady=5)
            selling_Ojrat_percent_entry = tk.Entry(panels[i])
            selling_Ojrat_percent_entry.grid(row=2, column=1, padx=10, pady=5)
            selling_Ojrat_percent_entries[i] = selling_Ojrat_percent_entry

            seller_profit_percent_label = tk.Label(panels[i], text='\u200Fدرصد سود: ')
            seller_profit_percent_label.grid(row=3, column=0, padx=10, pady=5)
            seller_profit_percent_entry = tk.Entry(panels[i])
            seller_profit_percent_entry.grid(row=3, column=1, padx=10, pady=5)
            seller_profit_percent_entries[i] = seller_profit_percent_entry

            # Add a button to trigger calculation for the first panel
            calculate_button = tk.Button(panels[i], text="محاسبه", command=lambda panel=i: calculate_first(panel))
        
        elif i == 1:
            reduction_percent_label = tk.Label(panels[i], text='\u200Fدرصد کاهش: ')
            reduction_percent_label.grid(row=2, column=0, padx=10, pady=5)
            reduction_percent_entry = tk.Entry(panels[i])
            reduction_percent_entry.grid(row=2, column=1, padx=10, pady=5)
            reduction_percent_entries[i] = reduction_percent_entry

            # Add a button to trigger calculation for the second panel
            calculate_button = tk.Button(panels[i], text="محاسبه", command=lambda panel=i: calculate_second(panel))
        
        elif i == 2:
            profit_percent_label = tk.Label(panels[i], text='\u200Fدرصد سود: ')
            profit_percent_label.grid(row=2, column=0, padx=10, pady=5)
            profit_percent_entry = tk.Entry(panels[i])
            profit_percent_entry.grid(row=2, column=1, padx=10, pady=5)
            profit_percent_entries[i] = profit_percent_entry

            # Add a button to trigger calculation for the third panel
            calculate_button = tk.Button(panels[i], text="محاسبه", command=lambda panel=i: calculate_third(panel))

        calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Add a label to display results
        results_label = tk.Label(panels[i], text="")
        results_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        results_labels[i] = results_label

    # Run the Tkinter event loop
    root.mainloop()

# Call the function to initiate the process
calculate_gold_price()
