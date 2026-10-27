menu = [("buff momo", 180), ("veg momo", 150), ("chicken momo", 220), ("tea", 40)]

def total_bill(*prices, discount=0):
    return int(sum(prices) - discount)

print(total_bill(180, 150, 60))            
print(total_bill(180, 150, 60, discount=40))

cart = [180, 220]
print(total_bill(*cart))                

def make_order(customer, *items, **extras):
    print(f"Order for {customer}:")
    for item in items:
        print(f"  - {item}")
    for key, value in extras.items():
        print(f"  {key}: {value}")

make_order("Sita", "buff momo", "jhol momo", spicy="yes", table=4)

sorted_menu = sorted(menu, key=lambda x: x[1])
print("Cheap to costly:", sorted_menu)

costliest_item = max(menu, key=lambda x: x[1])
print("Costliest:", costliest_item)

service_charge_prices = list(map(lambda x: int(x[1] * 1.1), menu))
print("With 10% service:", service_charge_prices)

filtered_menu = list(filter(lambda x: x[1] < 200, menu))
print("Under 200:", filtered_menu)