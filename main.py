print('How old are you')
age = input('Enter your age:')
print("you are", age, "years old")
print(type(age))
print('-----------------------------------------------------------')

changeToFloat = float(age)  # in the other data types same thing ,we can convert it to another type
print(changeToFloat)
print('-----------------------------------------------------------')

names = ['Ahmad', 'Mohammed', 'Ali', 'Anas']  # define a List
print(names[3])  # print specific index in the list
names[2] = 'Abdullah'  # to change the index
print(names)
names.append('Ryan')  # append is built-in function to add another value or index (in the end of list)
print(names)
names.insert(1, 'Khaled')  # insert is built-in function to add another value in any index you want in the list
print(names)
names.remove('Mohammed')  # remove is built-in function to remove any value you mention inside the list - there is
# there is another function called clear() used to remove all values inside the list and make it empty
print(names)
print('-----------------------------------------------------------')

child_one = ('Ahmad', 'Riydah', '1-1-2000')  # define a tuple (you can't change anything in the tuple after created)
# we can define the tuple without braces like this:  child_one = 'Ahmad', 'Riydah', '1-1-2000'
print(child_one)
print('-----------------------------------------------------------')

# define dictionary consist of two parts (key and value) , dictionary used for big multable data in one sequince
child_two = {'name': 'Mohammad', 'birth_city': 'Buryidah', 'birth_date': '7-7-2005'}
print(child_two['name'])  # access in dictionary via the key
print(child_two.values())  # to show all value inside the dictionary
print(child_two.keys())  # to show all keys inside the dictionary
print('-----------------------------------------------------------')

# if and else and elif statements
print("Enter your gender:")
gender = input()
if gender == "male":
    print("Your are a man")
else:
    print("Your are a girl")

print("Enter your path")
path = input()
if path == "web development":
    print("javascript")
elif path == "ios":
    print("swift")
elif path == "android":
    print("java")
else:
    print("something else")
print('-----------------------------------------------------------')

# Loops

# while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# for loop
students = ["Ahmad", "Mohammad", "Ali"]
for s in students:
    print(s)
# to split the characters individually
for l in "Welcome to Python":
    print(l)

# for loop with range
for n in range(5, 10):
    print(n)
print('-----------------------------------------------------------')


# Functions
def greet():
    name = input("Please enter your name:")
    time = input("Please enter the time ")
    print("Good" + time + "," + name + "!")


# function with parameter
def print_numbers(to):
    for j in range(to):
        print(j)


# function with two parameters
def add(f_num, s_num):
    print(f_num + s_num)


# function with return and multiple call in line 108
def sub(f_n, s_n):
    return f_n - s_n


greet()
print_numbers(2)
print_numbers(5)
add(5, 7)
add("Welcome to ", "python")

value = sub(9, 4) - sub(3, 2)
print(value)

# passing output of function to be input to another function
print_numbers(sub(5, 1))
