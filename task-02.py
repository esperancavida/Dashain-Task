name_input = input("Enter shopper's name: ")
item_input = input("Enter item name: ")
price_input = input("Enter price per item (Rs.): ")
qty_input = input("Enter quantity: ")
price = float(price_input)
quantity = int(qty_input)
shopper_name = name_input.title()
item_name = item_input.upper()
item_code = item_name[:3]
total_bill = price * quantity
print("\n==============================")
print("      DASHAIN SHOPPING RECEIPT ")
print("==============================")
print(f"Customer:    {shopper_name}")
print(f"Item Name:   {item_name} (Code: {item_code})")
print(f"Quantity:    {quantity}")
print(f"Price/Unit:  Rs. {price:.2f}")
print("------------------------------")
print(f"Total Bill:  Rs. {total_bill:.2f}")
print("==============================")
notes_500 = int(total_bill) // 500
change_left = total_bill % 500
print(f"Payable in Rs. 500 notes: {notes_500} note(s)")
print(f"Remaining balance/change: Rs. {change_left:.2f}")
print("------------------------------")
is_over_1000 = total_bill > 1000
print(f"Is total over Rs. 1000?: {is_over_1000}")
print("Data type of price variable:", type(price))
print("==============================")