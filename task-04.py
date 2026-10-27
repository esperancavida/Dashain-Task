trip_tuple = ("Pokhara", 3, "bus")
destination, days, transport = trip_tuple

print(f"Traveled to {destination} for {days} days using a {transport}.\n")
sita_visited = {"Mama Ghar", "Thulo Mamu", "Kaka Ghar", "Phupu Ghar"}
ram_visited = {"Mama Ghar", "Thulo Mamu", "Hajurba Ghar", "Maju Ghar"}

print("Both visited (Intersection):", sita_visited & ram_visited)
print("Everyone visited combined (Union):", sita_visited | ram_visited)
print("Only Sita visited (Difference):", sita_visited - ram_visited)
print()
raw_guests = ["Sita", "Ram", "Hari", "Sita", "Gita", "Ram", "Shyam"]
unique_guests = set(raw_guests)

print(f"Total entries: {len(raw_guests)} | Unique guests count: {len(unique_guests)}")
print(f"Unique guest list: {list(unique_guests)}\n")
tika_money = {
    "Mama Ghar": 1500,
    "Thulo Mamu": 1000
}
tika_money["Kaka Ghar"] = 500         
tika_money["Mama Ghar"] = 2000       
tika_money.update({"Phupu Ghar": 1200, "Thulo Mamu": 1500}) 
missing_check = tika_money.get("Maiju Ghar", 0) 
popped_value = tika_money.pop("Kaka Ghar")


print(f"Tika money from missing Maiju Ghar: Rs. {missing_check}")
print(f"Removed Kaka Ghar value: Rs. {popped_value}\n")

print("Current Tika Money Log:", tika_money)
print("Houses visited:", list(tika_money.keys()))
print("Total Tika Money Collected: Rs.", sum(tika_money.values()))
print()
nested_dashain_log = {
    "Sita": {"Total": 4700, "Status": "Completed"},
    "Ram": {"Total": 3500, "Status": "Active"}
}
ram_current_status = nested_dashain_log["Ram"]["Status"]

print(f"Ram's active Dashain visit log status: {ram_current_status}")
