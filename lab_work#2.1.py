# Q1. Write a Python Program to:
# take a number as input from the user.
# Use an 'if else' statement to check if the number is even or odd and print the result
a = int(input("Enter a number: "))
if a%2==0:
    print(a,"is an even number")
else: 
    print(a,"is an odd number")

# Q2. Create a program that:
# accepts a user's age as input
# uses nested 'if-else' statements to categorize the user into age groups:
#       - Child (0-12)
#       - Teenager (13-19)
#       - Adult (20-59)
#       - Senior (60+)
age = int(input("Enter your age: "))
if age <= 12:
    print("Child")
else:
    if age <= 19:
        print("Teenager")
    else:
        if age <= 59:
            print("Adult")
        else:
            print("Senior")
            
# Q3 Implement a program that: 
# takes 3 integers as input.
# uses an 'if-elif-else' statement to find and print the largest number:
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
if a>b and a>c:
    print("A is greatest number!")
elif b>a and b>c:
    print("B is greatest number")
else:
    print("C is greatest number")

# Q4. Write a Python Program to:
# take a number as input from the user and check whether it is a neutral
# number or not using a ladder if statement
num = int(input("Enter a number: "))
if num==0:
    print("Neutral")
elif num>0:
    print("Positive")
else:
    print("Negative")