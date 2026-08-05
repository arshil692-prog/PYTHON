"""
# 1///
# ANSWER > : oprators are special symbol to perform oprations on(on oneo two operands) variables and therir values. 

#2///
# ANSWER > : there are 7 types of operators in python 
# 1. arithamatic operators
# 2. assignment operators 
# 3. comparison operators 
# 4. logical operators 
# 5. identity operators 
# 6. membership operators
# 7. bitwise opertors

# 3///
a = 10 
b = 20 
print(a+b)

# 4////
a = 10 
b = 5
print(a-b)

# 5////
a = 5 
b = 3
print(a*b)

# 6///
a = 10 
b = 3 
print(a/b)

#7////
a = 10
b = 3
print(a%b)

# 8////
a = 10
b = 1
print(a//b)

# 9///
base = float(input("Enter the base:"))
exponent = float(input("Enter the exponent:"))
result = base**exponent
print("result:", (result))

# 10///
print(10 + 5 * 2)
# ANSWER > : 20 

# 11////
print(20 // 3)
# ANSWER > : 6

# 12///
print(20 % 3)
# ANSWER > : 2

# 13//
num = int(input("Enter a num:"))
squre = num ** 2 
print("squre=",squre)

# 14////
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

print("additions:",num1 + num2)
print("subtraction:",num1 - num2)
print("multiplication:",num1 * num2)
print("division:",num1 / num2)
print("modulus:",num1 % num2)
print("floor division:",num1 // num2)
print("exponent:",num1 ** num2)

# 15////
a = "20"
b = 5
#print(a - b)
# answer>:
print(int(a))
print(int(a)-b)

# 16////
a = 10
b = 20
print(a / b)
# ANSWER > the operator is performs the normal division and returns the float value.

a = 10
b = 20
print(a // b) 
# ANSWER > the operator is performs the floor division and returns the integer value.

# 17//////
= (Assignment Operator)
The = operator is used to assign (store) a value in a variable. 

==(Comparison Operator)
The == operator is used to compare two values. It returns True if the values are equal, otherwise it returns False.

# 18/////
num = int(input("Enter a number:"))
if num % 2 == 0:
    print(num,"is even")
else:
    print(num,"is odd")

# 19////
num = int(input("Enter a number:"))
if num % 5 == 0 and num % 7 == 0:
    print(num,"is divisible by both 5 and 7")
else:
    print(num,"is not divisible by both 5 and 7")

# 20////
num = int(input("Enter a number:"))
last_digit = num % 10
print("Last digit:",last_digit)

# 21////
a = 10
b = 22
print("a =", b, "b =", a)

a = 20
b = 10
a = a + b
b = a - b
a = a - b
print(a)
print(b)

# 22///
num = int(input("Enter the number:"))
cube = num **3
print("cube=",cube)

# 23///
print(5 > 2)

# 24///
print(5 != 5)

# 24///
print(5 <= 5)

# 25///
print(5 <= 5)

# 26///
#(==)Equal
#(!=)NOt equal
#(>)grether then
#(<)less then
#(>=)grether then equal
#(<=)less then equal

print("equal:,",10==10)
print("Not equal:",10 != 3)
print("greter then:",10>1)
print("less then:",5<10)
print("greter then equal:",11>=10)
print("less then equal:",1<=33)

# 27///
# their are 3 types of logical operators 
1.and
2.or
3.not
# ANSWER 1 
age = 19 
print(age>18 and age<30)

# ANSWER 2
age = 22
print(age>11 or age<17)

# ANSWER 3
age = 19
print(not age)

# 28////
print(True and False)

# 29///
print(True or False)

# 30////
print(not True)

# 31////
marks = float(input("Enter your marks:"))
attendence = float(input("Enter your attendence:"))

if marks >= 35.00 and attendence >= 75.00:
    print("pass:","marks of student",marks,"attendece",attendence)
else:
    print("unknow student")

# ones agian but in diffrent way

marks = int(input("Enter your marks:"))
attendence = int(input("Enter your attendence:"))

if marks >=35 and attendence >=75:
    print("student is pass:",marks,"student is regular",attendence)
elif marks >=35 and attendence <=75:
    print("student is pass:",marks,"but not regular:",attendence) 
elif marks <=35 and attendence >=75:
    print("student is not pass:",marks,"but student is regular:",attendence)
elif marks <=35 and attendence <=75:
    print("student is not pass:",marks,"student is also not regular:",attendence)
else:
    print("not eligible")

# 32////
age = int(input("Enter your age:"))
citizen = input("citizen (yes/no):")

if age >=18 and citizen == "yes":
    print("you can vote")
elif age>=18 and citizen == "no":
    print("can not vote : adult ","not citizen")
elif age<=18 and citizen == "yes":
    print("can not vote : minior","but citizen")
elif age<=18 and citizen == "no":
    print("cannot vote , minior:","not a citizen")
else:
    print("unknow id")

# 33////
num = 20

print("Original:", num)

num += 5
print("After += :", num)

num -= 3
print("After -= :", num)

num *= 2
print("After *= :", num)

num /= 4
print("After /= :", num)

num //= 2
print("After //= :", num)

num %= 3
print("After %= :", num)

num **= 2
print("After **= :", num)

# 34///
num = int(input("Enter the number:"))
print("orignal num:",num)

num += 5
print("after add 5:", num)

num -=2
print("after subtract 2:",num)

num *=3
print("after ,multiple by3:",num)

num /= 2
print("after the divide:",num)

# 35///
x = 10
x += 5
print(x)

# 36///
age = int(input("Enter your age:"))
citizen = input("citizen (yes/no):")

if age >=18 and citizen == "yes":
    print("you can vote")
elif age>=18 or citizen == "no":
    print("can not vote : adult ","not citizen")
elif age<=18 and citizen == "no":
    print("cannot vote , minior:","not a citizen")
else:
    print("unknow id")

# 37////
a = ["hello","hi"]
b = a
print(a is b)

# 38////
a = [1,2]
b = a
print(a is b)
# ANSWER >: True

# 39////
# >: the membership operato use to check the value present or not like in or ,not in 

city = ["nashik","niphad","bombay"]
print("bombay" in city)
print("pune" not in city)

# 40///
#Check whether a character exists in a string using in.

words = ["charecters","hello","hi","heyyy"]
print("charecters" in words)

# 41//
# check whether a student name exists in a list.

student_names = ["arshil","rohan","rehan","fazal","sana"]
print("rehan" in student_names)

# 42////
# BITWISE AND (&)
a = 6
b = 7
print(a & b)
# BITWISE OR (|)
a = 3
b = 4
print(a|b)
#BITWISE XOR (^)
a = 2
b = 3
print(a^b)
#BITWISE RIGHT SHIFT >>
a = 11
b = 12
print(a>>b)
# BITWISE LEFT SHIFT <<
a = 4
b = 5
print(a<<b)

# 43///
num1 = int(input("Enter the num1 :"))
num2 = int(input("Enter the num2 :"))
print("Entered numbers :",num1,":",num2)
print(num1 & num2)

# 44////
num1 = int(input("Enter the num1 :"))
num2 = int(input("Enter the num2 :"))
print("Entered numbers :",num1,":",num2)
print(num1 | num2)

# 45////
num1 = int(input("Enter the num1 :"))
num2 = int(input("Enter the num2 :"))
print("Entered numbers :",num1,":",num2)
print(num1 ^ num2)

# 46///
num1 = int(input("Enter the num1 :"))
num2 = int(input("Enter the num2 :"))
print("Entered numbers :",num1,":",num2)
print(num1 >> num2)
print(num1 << num2)

# 47///
a = 5
b = 3
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
# GUESS THE O/P
# 1
# 6
# 7
"""
# 48////
# CREATE THE CALCLUTER PROGRAM 

print("====CALCULATER====")
print("choise1:","ADDITION")
print("choise2:","SUBTRACTION")
print("choise3:","MULTIPLICATION")
print("choise4:","DIVISON")
print("choise5:","FLOOR DIVISION")
print("choise6:","MODULES")
print("choise7:","EXPONENT")
print("EXIT")

choise = int(input("Enter your choise"))

num1 = int(input("Enter your num1"))
num2 = int(input("Enter your num2"))

if choise == 1:
    print("ADDITION = ",num1+num2)
elif choise ==2:
    print("SUBTRACTION =",num1-num2)
elif choise ==3:
    print("MULTIPLICATION =",num1*num2)
elif choice == 4:
    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")
elif choise ==5:
    if num2 !=0:
        print("")
