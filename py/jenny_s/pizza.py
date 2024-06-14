#!/usr/bin/python3
# smallpiz 100, medium200, large300
# pepperoni for small 30, pepperoni fpr mid an large 50 cheese for any size-20

print("Welcome...  Please place your order:")
print("\n1. Small Pizza  ||  2. Medium Pizza  ||  3. Large Pizza")
print("\nYou can add extras:\nA. Pepperoni    ||    B. Cheese")

s_p, m_p, l_p, pp_s, pp_ml, chs = 100, 200, 300, 30, 50, 20
pizza = input("\nWhat will you have.? (Choose 1, 2, or 3.) ")
topping = input("Would you like extras.? (Enter A or B.. or N if Not)\n").upper()
bill = 0

if pizza == "1":
    if topping == 'N':
        bill = s_p
    elif topping == 'A':
        bill = s_p + pp_s
    elif topping == 'B':
        bill = s_p + chs

    print(f"\nGreat! Your bill is ₦{bill}.00")

elif pizza == "2":
    if topping == 'N':
        bill = m_p
    elif topping == 'A':
        bill = m_p + pp_ml
    elif topping == 'B':
        bill = m_p + chs

    print(f"\nGreat! Your bill is ₦{bill}.00")

elif pizza == "3":
    if topping == 'N':
        bill = l_p
    elif topping == 'A':
        bill = l_p + pp_ml
    elif topping == 'B':
        bill = l_p + chs

    print(f"\nGreat! Your bill is ₦{bill}.00")
else:
    print("Invalid option. Try Again..")
