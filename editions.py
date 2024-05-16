import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime
import jdatetime
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import arabic_reshaper
from bidi.algorithm import get_display

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
        
        return seller_profit_plus_Raw_price, seller_profit, tax

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

    pdfmetrics.registerFont(TTFont('BNazanin.ttf', 'C:/Users/Amir/Documents/Shop/BNazanin.ttf'))
    
    def generate_receipt(customer_name, customer_number, item_name, price, tax, total_payment):
        # Convert current date and time to Persian calendar
        persian_datetime = jdatetime.datetime.fromgregorian(datetime=datetime.now())
        persian_date = persian_datetime.strftime('%Y/%m/%d')
        persian_time = persian_datetime.strftime('%H:%M:%S')
    
        # Create a PDF file
        c = canvas.Canvas(f"{customer_name}_receipt.pdf", pagesize=letter)
        c.setFont('BNazanin.ttf', 12)
        def format_persian_text(text):
            reshaped_text = arabic_reshaper.reshape(text)  # Reshape the text
            bidi_text = get_display(reshaped_text)  # Apply BiDi algorithm
            return bidi_text
    
        # Format prices with thousands separators
        formatted_price = '{:,.0f}'.format(price)
        formatted_tax = '{:,.0f}'.format(tax)
        formatted_total_payment = '{:,.0f}'.format(total_payment)
    
        text_objects = {
            format_persian_text('نام مشتری'): format_persian_text(customer_name),
            format_persian_text('شماره مشتری'): customer_number,
            format_persian_text('نام کالا'): format_persian_text(item_name),
            format_persian_text('جمع کل ارزش افزوده'): format_persian_text(formatted_price),
            format_persian_text('مالیات'): format_persian_text(formatted_tax),
            format_persian_text('مبلغ قابل پرداخت'): format_persian_text(formatted_total_payment),
            format_persian_text('تاریخ'): persian_date,
            format_persian_text('زمان'): persian_time
        }
        for i, (key, text) in enumerate(text_objects.items()):
            c.drawString(100, 750 - (i * 20), f"{key}: {text}")
    
        c.save()


    # Function to handle 'تایید' button click
    item_options = ['انگشتر', 'النگو', 'سرویس', 'نیم سرویس', 'گوشواره', 'دستبند']
    check_vars = [tk.BooleanVar() for _ in item_options]
    def on_confirm():
        # Ask for customer's name and number
        customer_name = simpledialog.askstring("نام مشتری", "لطفا نام مشتری را وارد کنید:")
        customer_number = simpledialog.askstring("شماره مشتری", "لطفا شماره مشتری را وارد کنید:")
        selected_items = [item for item, var in zip(item_options, check_vars) if var.get()]
        
        # Ensure the item name is valid
        if not selected_items:
            messagebox.showerror("خطا", "لطفا حداقل یک کالا را انتخاب کنید.")
            return
            
        selected_items_str = ', '.join(selected_items)
        
        # Calculate the price and other financial details
        price, added_value, tax = calculate()
        total_payment = price + tax
        
        # Generate the receipt PDF
        generate_receipt(customer_name, customer_number, selected_items_str, price, tax, total_payment)

    for i, item in enumerate(item_options):
        tk.Checkbutton(root, text=item, variable=check_vars[i]).grid(row=i+6, column=0, sticky='w')

    # Add a 'تایید' button to the interface
    confirm_button = tk.Button(root, text="تایید", command=on_confirm)
    confirm_button.grid(row=len(item_options)+6, column=0, columnspan=2, pady=10)

    # Run the Tkinter event loop
    root.mainloop()

# Call the function to initiate the process
calculate_gold_price()
