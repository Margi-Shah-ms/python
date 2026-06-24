# Q1 Write a program using a 'while' loop to:
# take numbers as input from the user until they enter '0'
a = int(input("enter: "))
while a!=0:
    a=int(input("enter a:"))
    
    if a!=0:
        print("you entered:{a}")
print("done")

# Q2. Create a program using a 'for loop to:
# iterate over a given range(1 to 10)
# print each digit's square, one per line
for x in range(1,11):
    print(f"{x} square is {x**2}")

# Q3. Write a program
# use a 'while' loop print all even numbers b/w 1 to 50
n = int(input("enter: "))
while n<=50:
    if n%2==0:
        print(n)
    n+=1

# Q4. Write a program to:
# use the 'range()' function to generate a sequence of numbers from 1 to 20.
# print only the odd numbers using a 'for' loop
for i in range(1,21):
    if i%2!=0:
        print(i)
        
# Q5. Implement a program that: 
# uses the range() function with three arguments (start,stop,step) to 
# print multiples of 5 from 5 to 50
for i in range(5,51,5):
    print(i)
    
# Q6. Create a program using a 'for' loop and 'range()' to:
# print a reverse countdown from 10 to 1
for i in range(10,0,-1):
    print(i)

# Q7. Write a program that: 
# - Uses a `for` loop and `range()` to iterate through numbers from 1 to 50.
#   - Checks if each number is divisible by 2, 3, or both using nested `if-elif-else`.
#   - Prints messages for each case (e.g., "Divisible by 2", "Divisible by 3", "Divisible by both").

for i in range(0,51):
    if i%2==0:
        print(f"{i}, Divisible by 2")
    elif i%3==0:
        print(f"{i}, Divisible by 3")
    elif i%2!=0 and i%3!=0:
        print(f"{i}, Not Divisble by both")
    else:
      print(f"{i}, Divisible by both")