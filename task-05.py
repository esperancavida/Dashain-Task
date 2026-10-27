name_input = input("Name: ").strip()
if not name_input:
    print("Please enter your name.")
else:
    name = name_input.title()
    age = int(input("Age: "))
    height = int(input("Height (cm): "))
    coupon_code = input("Coupon code: ").strip().lower()
    if age < 5 or height < 110:
        print(f"Sorry {name}, the big ping is not safe for you.")
    else:
        if age >= 60:
            base_price = 0
        elif age < 12:
            base_price = 50
        else:
            base_price = 100
        final_price = base_price
        if base_price > 0 and (coupon_code == "dashain" or coupon_code == "tihar"):
            final_price = base_price - 20
            print("Coupon used! Rs 20 off.")
        print(f"{name}, your ping ticket is Rs {final_price}.")
