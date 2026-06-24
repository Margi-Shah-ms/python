# Q1 write a program to find the maximum number 
# from the given 3 numbers. (Using nested if statement)
a = int(input("enter A: "))
b = int(input("enter B: "))
c = int(input("enter C: "))
if a>b and a>c:
    print("A is greatest.")
else:
    if b>c and b>a:
        print("B is greatest.")
    else:
        if c>a and c>b:
            print("C is greatest.") 

# Q2 Write a program to find the minimum number
# from the given 3 numbers (using nested if statement)
a = int(input("enter A: "))
b = int(input("enter B: "))
c = int(input("enter C: "))
if a<b and a<c:
    print("A is lowest.")
else:
    if b<c and b<a:
        print("B is lowest.")
    else:
        if c<a and c<b:
            print("C is lowest.")

# Q3. Write a program to find the maximum number from the given
# four numbers (Using a nested if statement)
a = int(input("enter A: "))
b = int(input("enter B: "))
c = int(input("enter C: "))
d = int(input("enter D: "))
if a>b and a>c and a>d:
    print("A is greatest.")
else:
    if b>c and b>a and b>d:
        print("B is greatest.")
    else:
        if c>a and c>b and c>d:
            print("C is greatest.")
        else:
            if d>a and d>b and d>c:
                print("D is greatest.")

# Q4. Write a program using 'switch-case' equivalent to:
# take an operator ('+','-','*','/') as input
# perform the corresponding operation on two numbers entered by the user.
o = input("operator: ")
a = int(input("a: "))
b = int(input("b: "))
match o:
    case '+':
        c = a+b
        print("Results: ",c)
    case '-':
        c = a-b
        print("Results:",c)
    case '*':
        c = a*b
        print("Results:",c)
    case '/':
        c = a/b
        print("Results:",c)

# Q5. Write a Program in Python to create a menu-driven  fast food order 
# system using the 'match-case' feature.
# for example: 
# press 1 to order a Sandwich
# press 2 to order a Pizza
# press 3 to order a BUrger
# extend this program by adding a nested match case for each menu items's
# subtype selection by the user
# for example:
# press 1 for thin crust pizza
# press 2 for cheese burst pizza
# press 3 for fresh dough pizza

print("--- Fast-Food Order System ---")
print("1. Order a Sandwich")
print("2. Order a Pizza")
print("3. Order a Burger")
print("-----------------------------------------")
main_choice = input("Enter your choice (1-3): ")
print()
match main_choice:
    case "1":
        print("--- Sandwich Menu ---")
        print("1. Veg Grilled Sandwich")
        print("2. Cheese Corn Sandwich")
        print("3. Paneer Tikka Sandwich")
        print()
        sub_choice = input("Enter your choice (1-3): ")
        match sub_choice:
            case "1":
                print(" Veg Grill Sandwich")
            case "2":
                print("Cheese corn sandwich")
            case "3":
                print("Paneer Tikka Sandwich")
            case _:
                print("Invalid choice try again!")
                
    case "2":
        print("--- Pizza Menu ---")
        print("1. Thin Crust Pizza")
        print("2. Cheese Burst Pizza")
        print("3. Fresh Dough Pizza")
        print()
        sub_choice = input("Enter your choice(1-3): ")
        match sub_choice:
            case "1":
                print("Thin Crust Pizza")
            case "2":
                print("Cheese Burst Pizza")
            case "3":
                print("Fresh Dough Pizza")
            case _:
                print("Invalid choice try again!")
                
    case "3":
        print("--- Burger Menu ---")
        print("1. Aloo Tikki Burger")
        print("2. Veggie Supreme Burger")
        print("3. Cheese Lava Burger")
        print()
        sub_choice = input("Enter your choice (1-3): ")
        match sub_choice:
            case "1":
                print("Aloo Tikki Burger!")
            case "2":
                print("Veggie Supreme Burger!")
            case "3":
                print("Cheese Lava Burger!")
            case _:
                print("Invalid subtype choice!")

    case _:
        print("\nInvalid main menu choice! Please run the program again.")

# Q6 Write a python program to create a menu-driven telecom calling system
# using the 'match-case' feature.
# for example:
# press 1 for English
# press 2 for Hindi
# press 3 for Gujarati
# Extend this program by adding a nested match case for each menu item's
# appropriate subtype selection by the user.
print()
print("---Telecom Calling System---")
print("Press 1 for English")
print("Press 2 for Hindi")
print("Press 3 for Gujarati")
a = input("Please enter a number of your choice(1-3): ")
match a:
    case "1":
        print("English Language")
        print("1. Prepaid Recharge")
        print("2. New Connection")
        print("3. Talk to customer executive")
        sub_choice = input("enter a number(1-3): ")
        match sub_choice:
            case "1":
                print("Prepaid Recharge Portal")
            case "2":
                print("Request for new connection!")
            case "3":
                print("Connecting your call to our customer executive!")
    case "2":
        print("\n--- Hindi Menu ---")
        print("1. prepaid Recharge ke liye")
        print("2. Naye Connection ke liye")
        print("3. Customer Executive se baat karne ke liye")
        
        sub_choice = input("Enter your choice (1-3): ")
        match sub_choice:
            case "1":
                print("Prepaid Recharge portal bhej diya.")
            case "2":
                print("Naye Connection ka request register ho gaya hai!")
            case "3":
                print("Humari customer executive se baat karne ke liye pratiksha karein")
            case _:
                print("Galat vikalp chuna gaya hai!")

    case "3":
        print("--- Gujarati Menu ---")
        print("1. Prepaid Recharge mate")
        print("2. Nava Connection mate")
        print("3. Customer Executive sathe vaat karva mate")
        
        sub_choice = input("Enter your choice (1-3): ")
        match sub_choice:
            case "1":
                print("Prepaid Recharge portal par mokalva ma aavi rahyu che.")
            case "2":
                print("Nava Connection ni request register thai gayi che!")
            case "3":
                print("Customer executive sathe vaat karva mate raah juo")
            case _:
                print("Khotu option pasand karyu che!")

    case _:
        print("Invalid language choice! Please try again.")
        