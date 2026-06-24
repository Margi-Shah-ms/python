# Q1 Write a Python Program to:
# take a user's first name and last name as input.
# Print them in the format: Hello, [Last Name], [First Name]!
first_name = input("First name: ")
last_name = input("Last Name: ")
print(f"Hello,{last_name},{first_name}!") 

# Q2 Create a program to: 
# format and display the following sentence: "The price of {item} is {price}, dollars."
# replace {item} with "apple" and {price} with 5.50 using f-strings
item = input("Enter: ")
price = float(input("Enter: "))
print(f"The price of {item} is {price:.2f} dollars.") 

# Q3 Implement a program to: 
# take a string as input
# print the string reversed and also print whether it is a palindrome
string = input("Enter string: ")
print(string[::-1])

if string==string[::-1]:
    print("It's a palindrome")
else: 
    print("It is not a palindrome")

# Q4. Create a program that: 
# takes a string input from the user
# converts the string to uppercase, lowercase, title case
string = input("enter a string: ")
print(string.upper())
print(string.lower())
print(string.title()) 

# Q5. Find the position of the word "AI" in the sentence "Machine Learning and AI are trending."
# replace AI with "Artificial Intelligence" in the above sentence.
# count how many times the word "data" appears in "data data mining and big data." 
sent = "Machine Learning and AI are trending"
print(sent[21:23])

print(sent.replace("AI","Artificial Intelligence"))

a = "data data mining and big data"
print(a.count("data")) 

# Q.6 Split "apple, banana, grapes" into a list.
# join the list ["Python","is","awesome"] into a sentence using spaces.
# split a multiline string into separate lines and print them one by one.
a = "apple","banana","grapes"
print(list(a)) 

b = ["Python","is","awesome"]
sent = " ".join(b)
print(sent)

c = '''Hello in the world of coding. Python is aswesome language.
AI and Data Science are trending'''
text = c.splitlines()
print(text)
print('\n'.join(text))

# Q.7 Check if a string start with "Hello" and ends with "World".
# remove all non-alphabetic characters from "Data123=Science!"
# reverse the string "Python"

a = "Hello World"
print(a[0:11])
b = "Data123=Science!"
s = b.replace("123="," ")
z = s.replace("!"," ")
print(z)
c = "Python"
print(c[::-1])