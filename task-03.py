kites = ["red", "blue", "green"]
kites.append("yellow")
kites.insert(0, "black")
kites.remove("green")
sold_kite = kites.pop()
print(f"Kite sold: {sold_kite}")
kites.sort()
print("First two kites in alphabetical order:", kites[:2])
print(f"Number of kites left in stock: {len(kites)}")
print(f"Is 'blue' kite in stock?: {'blue' in kites}")
new_arrivals_str = "pink,orange,white"
new_arrivals_list = new_arrivals_str.split(",")
kites.extend(new_arrivals_list) 
print("Current stock overview:", " | ".join(kites))
kites_copy = kites.copy()
kites_copy.append("gold")
print(f"Original stock list: {kites}")
print(f"Display showroom copy list (with gold): {kites_copy}")
prices = [["small", 50], ["big", 150]]
big_kite_price = prices[1][1]
print(f"Price of a big kite: Rs. {big_kite_price}")