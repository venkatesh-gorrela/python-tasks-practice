# dmart 
# name=input("enter your name: ")

# items='''

# '''

# Define the items and their prices
#items= '''
#     apple    100
#     banana   50
#     orange   150
#     bread    200
#     milk     300
#     eggs     250
# '''

# print(items)



from datetime import datetime

customer_name = input("Enter your name: ")

# List of items
item_list = '''
Basumati rice  :  Rs 90/kg
Sugar          :  Rs 30/kg
Salt           :  Rs 20/Kg
Oil            :  Rs 140/liter
Carrot         :  Rs 20/kg
Potatos        :  Rs 50/kg
Diary milk     :  Rs 90/each
Surf excel     :  Rs 85/each
'''

# Declaration
total_price = 0
price_list = []
item_name_list = []
quantity_list = []
price_per_unit_list = []

# Rates for items
item_rates = {
'basumati rice':   90,
'sugar'        :   30,
'Salt'         :   20,
'oil'          :   140,
'carrot'       :   20,
'potatos'      :   50,
'diary milk'   :   90,
'surf excel'   :   85
}

option = int(input("For list of items, press 1: "))
if option == 1:
    print(item_list)
    for i in range(len(item_rates)):
        inp1 = int(input("If you want to buy an item, press 1 or 2 to exit: "))
        if inp1 == 2:
            break
        if inp1 == 1:
            item = input("Enter the item name: ").lower()
            quantity = int(input("Enter quantity: "))
            if item in item_rates.keys():
                price = quantity * (item_rates[item])
                price_list.append((item, quantity, item_rates, price))
                total_price += price
                item_name_list.append(item)
                quantity_list.append(quantity)
                price_per_unit_list.append(item_rates[item])

                Gst = (total_price * 1) / 100

                final_amount = Gst + total_price
            else:
                print("Sorry, the item you entered is not available.")
        else:
            print("You entered an invalid number.")
            
    inp = input("Can I bill the items? (Yes or No): ")
    if inp.lower() == 'yes':
        if final_amount != 0:
            print(25 * ">", "GVL--MART", 25 * "<")
            print(23 * " ", "---RAJAHMUNDRY---")
            print(f"Name: {customer_name}", 30 * " ", f"Date: {datetime.now()}")
            print(75 * "_")
            print("S.No.", 8 * " ", 'Item', 4 * " ", 'Quantity', 5 * " ", 'Price')
            for i in range(len(price_list)):
                print(i, 8 * ' ', 4 * ' ', item_name_list[i], 5 * ' ', quantity_list[i], 12 * " ", price_per_unit_list[i])
                print(75 * "_")
            print(50 * " ", 'Total Amount:', 'Rs', total_price)
            print("GST Amount:", 47 * " ", f"Rs {Gst}")
            print(50 * " ", 'Final Amount:', 'Rs', final_amount)
            print(75 * "_")
            print(45 * " ", 'Thank you for shopping in GVL--MART!')
















