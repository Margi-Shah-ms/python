# Q1 Create a list of 5 fruits the second and last fruit
# add "Mango" to the list. Remove first element
# sort the list alphabetically. Reverse it
a = ["Apple","Banana","Grapes","Cherry","Watermelon"]
print(a)
# # 2nd and last fruit
print(f"{a[1]}, is a second fruit in the given list.")
print(f"{a[4]}, is a last fruit in the given list.")
# # Add mango and remove first element
a[0]="Mango"
print(a)

# # Sort the list alphabetically , reverse it
a.sort()
print(a)

# # reverse
a.reverse()
print(a)

# Q2. Create a tuple of 5 numbers
# access third item in the tuple
# try to change the second value and observe the result (explain mutability)
a = (1,2,3,4,5)
print(a[2])
# changing
# a[1]=5
# print(a) 
# it will give us an error because tuple is immutable means we can't do any 
# kind of modification & changes in it
# mutability: It means something we can change or modify after a variable is created.

# Q3. Create a list and tuple both containing the same 3 items
# try changing first item of each 
# Discuss the error (in case of tuple) and explain why it happens.
li_st = ["Apple","Banana","Cherry"]
tu_ple = ("Apple","Banana","Cherry")
li_st[0]="Grapes"
print(li_st)
# tu_ple[0]="Banana"
# print(tu_ple)
# AS we can see that the tuple is showing an error because tuple is immutable which means we can't change or modifiy it. 
# if we try to do changes in it it show an error to us as an output

# Q4. Create a list of squares of numbers from 1-10 using list comprehension
# create a new list that only contains even numbers from a given list [1,2,3,...,20]
# Convert all strings in a list["hello","WORLD","PyThOn"] to lowercase using list comprehension.

a = [x for x in range(1,11)]
print(a)
print()
b = [x**2 for x in range(1,21)]
print(b)
print()
li_st = ["hello","WORLD","PyThOn"]
c = [l.lower() for l in li_st]
print(c)