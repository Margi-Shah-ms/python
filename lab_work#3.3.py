# Q1. Create a set of integers {1,2,3,4,5}
# add 6, remove 3, and check if 2 is in the set
a = {1,2,3,4,5}
print(a)
a.add(6)
a.remove(3)
print(a)
print(a)
print(2 in a)

# Q2. Perfrom the following operations on the given two sets
# union, intersection, difference 
# set_a = {1,2,3,4}
# set_b = {2,4,5,6}
set_a = {1,2,3,4}
set_b = {2,4,5,6}
print()
# Union
print("Union:",set_a.union(set_b))
print()
# intersection
print("intersection:",set_a.intersection(set_b))
print()
# difference
print("Difference:",set_a.difference(set_b))

# Q3. Create a dictionary 
# print the keys and values
# add a new key: "city":"Delhi"
# update "age" to 21
# delete the "grade" key
student = {"name":"Alice","age":20,"grade":"A"}
print(student.items())
print()
student["age"]=21
print(student)
print()
student.popitem()
print(student)

# Q4. Create a dictionary from 2 lists:
keys = ['id','name','email']
values =[101,'Bob','bob@example.com']
di_ct = dict(zip(keys,values))
print(di_ct)

# Q5. Convert the following
# A string '123' to an integer
# A list [1,2,3] to a tuple
# A tuple(4,5,6) to a list
# A list of pairs [(1,'A'),(2,'B')] to a dictionary
s = "123"
n = int(s)
print(n)

l = [1,2,3]
n = tuple(l)
print(n)

a = (4,5,6)
n = list(a)
print(n)

z = [(1,'A'),(2,'B')]
n = dict(z)
print(n)

# Q6. delete a specific item from a list using del keyword
a = {"A":1,"B":2,"C":3}
del a["A"]
print(a)