"""
# 1///
# DATA TYPE TELLS TO PYTHON WHAT KIND OF VALUE STORE 

# 2///

1. STRING
2. INTGER
3. FLOAT
4. FLOAT
5. BOOLEAN
6. SET 
7. DICTINARY
8. LIST
9. TUPLE


# 3///
name = "arshil"
age = 19
marks = 89.90
good_student = True
compelx = 12j

print(name)
print(age)
print(good_student)
print(compelx)
print(marks)

# 4///
a = 25 
print(type(a))

# 5///
a = 25j
print(type(a))

# 6///
a = "name"
print(type(a))

# 7///
a = True
print(type(a))

# 8////
a = 3+4j
print(type(a))

# 9///
student_age = 22
student_marks = 88.00
student_think = 12j

print(student_age)
print(student_marks)
print(student_think)

# 10////
age = int(input("enter your num"))
print(type(age))

# 11////
marks = float(input("enter your marks"))
print(type(marks))

# 12////
empolyee_name = "arshil shaikh"
empolyee_salery =  20,0000 
empolyee_imajin = 12j
empolyee_is_adult = True
empolyee_post = ["maneger","HR","devloper"]

print(empolyee_imajin)
print(empolyee_is_adult)
print(empolyee_post)
print(empolyee_salery)
print(empolyee_name)

# 13///
num = 20
print(type num)

find the error

answer > invalid synatx

num = 20
print(type(num))

# 14/////
Which of the following is a Boolean value?

A. "True"

B. True

C. TRUE

D. true

answer >  A. True : because its only True value of santax 


# 15////
#Read the code and identify the data type of each variable.

#a = 50
#b = 5.5
#c = "Hello"
#d = False
#e = 5+2j


answer > 
int
float
string
boolean
complex

# 16////
name = "arshil"
numbers = 12
compellx = 12j 
marks = 99.99
good = True 
l1 = [1,2,3]
s1 = {11,33,54,33}
student_info = {
    "name":"arshil shaikh",
    "age" : 19,
    "address":"niphad"
}
t1 = ("hello","hii")

print(name)
print(numbers)
print(compellx)
print(marks)
print(s1)
print(l1)
print(t1)
print(student_info)

# 17////
                   Feature	Mutable Data Types	               Immutable Data Types
Meaning:	    Can be changed after creation.      	Cannot be changed after creation.
Memory:	        Same object is modified.	            A new object is created when modified.
Modification:	Allowed.	                            Not allowed.
Performance:    Faster for frequent updates.	        Safer because values cannot change accidentally.
Examples:	    list, dict, set, bytearray	            int, float, bool, str, tuple, frozenset,betys


# 18////
num = 20
if isinstance(num,int):
    print("num is intger")
else:
    print("not intger")

# 19///
age = int (input("enter the number"))
print(type(age),"before conversion")
age = float(age)
print(type(age))
print(type(age),"after conversion")

# 20///
a = "25"
b = int(a)
print(type(b))
# answer > string : because we convert into string

# 21///
a = 25
b = float(a)
print(type(b))
# answer > float : we convert into float

# 22///
print(bool(""))
# answer > false : because threr is no value
 
# 23///
print(bool("python"))
# answer > true : because its value is true

# 24///
print(bool(0))
# answer > false : because its zero and its value is false

# 25///
print(bool(100))
#answer > true : because 100 is true value

# 26///
age = 20
print(type(age),"before convert")
age = int(age)
print(type(age),"after convert")

# 27////
age = 33
print(type(age))
age = str(age)
print(type(age))

# 28////
correct the following program.
age = "20"
print(age + 5)

# answer > 
age = 20
print(age + 5)

# 29///
marks = float("abc")
# answer > value error : because wrong data type and also wrong value

# 30////
price_1 = (input("enter your item price1:"))
price_2 = (input("enter your item price2:"))
price_3 = (input("enter your item price3:"))
print(price_1)
print(price_2)
print(price_3)
price_1 = int(price_1)
price_2 = int(price_2)
price_3 = int(price_3)

total = price_1+price_2+price_3
print("total item price:",total)

# 31///
l1 = [1,2,3,4]
if type (l1) in (list,dict,set,bytearray,):
    print("the variable is mutable")
elif type (l1) in (bool,str,frozenset,int,complex,float,tuple,bytes):
    print("the variable is immutables")
else:
    print("unknown data type")

# 32///
print(int(5.6))
print(float(7))
print(str(True))
print(bool(1))

# 33////
a = "10"
print(type(a))
b = int(a)
print(type(b))
c = float(b)
print(type(c))
d = str(c)
print(type(d))

# 34///
list1 = [1,2,3,4]
print("its a list",list1)
tuple1 = (11,22,33,44,55)
print("its a tuple",tuple1)
# answer > list is mutable and tuple is immutable


# 35///
# answer >  list is set of coolection of data types that why python allow to store diffrent data types. 


# 36///
value = eval(input("enter any value:"))
print(value)
print(type(value))
# for any type of data had to know use eval 

# 37///
int_var = 10
float_var = 89.00
complex_var = 12j
bool_var = True
str_var = "arshil"
list_var = [1,22,3]
set_var = {11,22,33}
frozenset_var = frozenset({11,22,33})
tuple_var = (1,2,3)
dict_var = {"name":"arshil","age":19}
bytes_var = b"hello"
bytearray_var = bytearray(b"hello")
None_var = None
memoryview_var = memoryview(b"hello")
range_var = range(10)

print(type(int_var))
print(type(float_var))
print(type(complex_var))
print(type(bool_var))
print(type(str_var))
print(type(list_var))
print(type(set_var))
print(type(frozenset_var))
print(type(tuple_var))
print(type(dict_var))
print(type(bytes_var))
print(type(bytearray_var))
print(type(None_var))
print(type(memoryview_var))
print(type(range_var))

# 38////
# fix the error
#a = "25"
#b = 10
#c = a + b
#print(type(c))

# answer > 
a = 25
b = 10
c = a + b
print(type(c))

# 39///
name = "rahul sharma"
age = 26
salery = 20000.00
marrieds_status = True

print("name:",name,type(name))
print("age:",age,type(age))
print("salery:",salery,type(salery))
print("married status:",marrieds_status,type(marrieds_status))


# 40///
value = eval(input("Enter any value:"))
print("value:",value,type(value))

# 1, print(value)
# 2, print("type:",type(value))

# 41////

print("=======MENU=======")
print("1. convert to integer")
print("2. convert to float")
print("3. convert to string")
print("4. convert to boolean")
print("5. program exited")

choise = int(input("Enter your choise:"))

if choise == 1:
    value = input("Enter your value:")
    print("converted value:",int(value))
    print("data type:",type(int(value)))

elif choise == 2:
    value = input("Enter your value:")
    print("converted value:",float(value))
    print("data type:",type(float(value)))

elif choise == 3:
    value = input("Enter your value:")
    print("converted value:",str(value))
    print("data type:",type(str(value)))

elif choise == 4:
    value = input("Enter your value:")
    print("converted value:",bool(value))
    print("data type:",type(bool(value)))

elif choise == 5:
    print("program exited")     

else:


# 42////

 1. type()

Returns the actual type.

a = 10

print(type(a))

Output

<class 'int'>


 2.isinstance()

Returns only True or False.

a = 10

print(isinstance(a, int))

Output

True

# 43////

# Program to display all immutable data types with sample values

# Immutable Data Types
int_var = 100
float_var = 99.99
complex_var = 3 + 4j
bool_var = True
str_var = "Hello Python"
tuple_var = (10, 20, 30)
range_var = range(1, 6)
frozenset_var = frozenset({1, 2, 3})
bytes_var = b"Python"
none_var = None

print("===== Immutable Data Types =====")

print("Integer     :", int_var, "|", type(int_var))
print("Float       :", float_var, "|", type(float_var))
print("Complex     :", complex_var, "|", type(complex_var))
print("Boolean     :", bool_var, "|", type(bool_var))
print("String      :", str_var, "|", type(str_var))
print("Tuple       :", tuple_var, "|", type(tuple_var))
print("Range       :", range_var, "|", type(range_var))
print("Frozen Set  :", frozenset_var, "|", type(frozenset_var))
print("Bytes       :", bytes_var, "|", type(bytes_var))
print("None        :", none_var, "|", type(none_var))

# 44///
# Mutable Data Types
list_var = [10, 20, 30]
dict_var = {"name": "Arshil", "age": 21}
set_var = {1, 2, 3}
bytearray_var = bytearray(b"Python")

print("===== Mutable Data Types =====")

print("List       :", list_var, "|", type(list_var))
print("Dictionary :", dict_var, "|", type(dict_var))
print("Set        :", set_var, "|", type(set_var))
print("Bytearray  :", bytearray_var, "|", type(bytearray_var))

# 45///
A CSV file stores all values as strings. Explain how you would convert each field to the correct data type before processing.
# ANSWER > 
A CSV (Comma Separated Values) file stores every value as text (string), regardless of whether the value represents a number, Boolean, or date. Before processing the data, each field should be converted to its appropriate data type so that calculations, comparisons, and logical operations work correctly.

Example CSV Data
Name,Age,Salary,Married
Arshil,21,45000.50,True

When Python reads this row from a CSV file, it treats every value as a string.

name = "Arshil"
age = "21"
salary = "45000.50"
married = "True"

To use these values correctly, convert them to their proper data types.

# 46///
Why is bool considered a subclass of int in Python? Explain with examples.

In Python, the bool data type is a subclass of int, which means Boolean values (True and False) behave like integers.

True is equivalent to 1
False is equivalent to 0

Because of this relationship, Boolean values can be used in arithmetic operations.

# 47///
in book 

# 48////
A Python program that accepts user input may raise a TypeError if mathematical operations are performed on incompatible data types.
Since the input() function always returns a string, values must be converted to the correct numeric data type before calculations.

# ANSWER >
1.
Wrong
age = input("Enter Age: ")
result = age + 5

Error
TypeError: can only concatenate str (not "int") to str

Correct
age = int(input("Enter Age: "))
result = age + 5

2.
Wrong
a = "10"
b = 20

print(a + b)

Error
TypeError

Correct
a = int(a)

print(a + b)
"""
# 49////
