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
"""
# 34///
