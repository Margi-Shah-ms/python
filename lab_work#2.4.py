# Q1. Write a Python Program that:
# Uses a for loop to print numbers from 1 to 20.
# Skip numbers divisible by 4 using the continue statement.
for i in range(1,21):
    if i%4!=0:
        print(i)
        
# Q2. Implement a program using while loop to: 
# Print numbers from 1 to 10.
# Stop the loop using the break statement when the number is 7.
n = 1
while n<=10:
    if n==7:
        break
    print(n)
    n+=1

# Q3. Create a Python Program that 
# Iterates over a string (e.g., "PYTHON").
# Uses a continue statement to skip vowels and print only consonants.
a = "PYTHON"
for i in a:
    print(i)
    
a = "PYTHON".lower()
b = ["a","e","i","o","u"]
for i in a:
    if i in b:
        continue
    print(i)

# Q.4 Write a Python program to print multiplication tables using nested loops
# for up to N in this format:
# 1 x 1 = 1
# 1 x 2 = 2
# Where N is the user given number
n = int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,11):
        print(i,"X",j,"=",i*j)
    print() 

# Q.5 Write a Python program to print the following Right-angled Triangle Numeric Pattern:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
n = int(input("enter n: "))
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Q6. Write a Python Program to print the Right - angled Numeric Pattern:
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1
n = int(input("enter n: "))
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()

# Q7. Write a Python program to print the following Right-angled Triangle Numeric Pattern:
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5
n = int(input("Enter N: "))
for i in range(1,n):
    for j in range(n-i+1,n+1):
        print(j,end=" ")
    print()
    
# Q.8 Write a Python program to print the following Right-angled Triangle Numeric Pattern:
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5
n = int(input("enter: "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(j, end=" ")
    print()
