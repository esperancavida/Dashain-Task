menu = {
    "momo": 180,
    "chowmein": 150,
    "sel roti": 30,
    "tea": 40
}
def ask_quantity():
    qty_input = input("Quantity: ")
    qty = int(qty_input)
    if qty <= 0:
        raise ValueError("Quantity must be more than 0")
    return qty
def print_bill(cart_items):
    total = 0
    for item, qty in cart_items.items():
        cost = menu[item] * qty
        total += cost
        print(f"{item} x{qty} = Rs {cost}")
    print(f"Total: Rs {total}")
cart = {}
print("=== Safe Dashain Food Shop ===")
while True:
    item_input = input("Item (or done): ").strip().lower()
    if item_input == "done":
        break
        
    try:
        if item_input not in menu:
            raise KeyError
            
        qty = ask_quantity()
        
    except KeyError:
        print(f"Sorry, no {item_input} on the menu.")
        
    except ValueError as e:
        print(f"Wrong quantity: {e}")
        
    else:
        if item_input in cart:
            cart[item_input] += qty
        else:
            cart[item_input] = qty
        print(f"Added {qty} x {item_input}")
        
    finally:
        print("-" * 20)
print_bill(cart)