for day in range(1, 16):
    if day == 7:
        print("Day 7: Fulpati!")
        continue
    if day == 10:
        print("Day 10: Vijaya Dashami, tika day!")
        break
        
    print(f"Day {day}")
balance = 0
while True:
    choice = input("1 Add  2 Spend  3 Balance  4 Quit: ").strip()
    
    if choice == "1":
        amount = int(input("Amount: "))
        balance += amount
        
    elif choice == "2":
        amount = int(input("Amount: "))
        if amount > balance:
            print("Not enough money!")
            continue
        balance -= amount
        
    elif choice == "3":
        print(f"Balance: Rs {balance}")
        
    elif choice == "4":
        print("Bye! Happy Dashain.")
        break
        
    else:
        print("Wrong choice, try again.")