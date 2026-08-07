# 1///
# What are Conditional Statements in Python? Explain in your own words.

# A Conditional Statement is a decision-making statement in Python that allows a,
#  program to execute different blocks of code based on whether a specified condition is True or False.

# 2///

# Imagine you want to withdraw ₹5,000 from an ATM.

# The ATM first checks:

# Condition: Is your account balance greater than or equal to ₹5,000?

# If Yes → The ATM dispenses the money.
# If No → The ATM displays "Insufficient Balance" and does not dispense cash.

# This is exactly how a conditional statement works—it checks a condition first and then decides which action to perform.

# 3////
# List all conditional statements available in Python.

# | No. | Conditional Statement | Purpose                                  |
# | --- | --------------------- | ---------------------------------------- |
# | 1   | `if`                  | Executes code when a condition is `True` |
# | 2   | `if-else`             | Chooses between two possibilities        |
# | 3   | `if-elif-else`        | Checks multiple conditions               |
# | 4   | Nested `if`           | An `if` statement inside another `if`    |

# 4////
#Write the syntax of:

# 1
if condition:
    # code to execute
# 1 EXAMPLE
age = 20

if age >= 18:
    print("You are eligible to vote")

# 2
if condition:
    # code when condition is True
else:
    # code when condition is False
    
# EXAMPLE
age = 16

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# 3
if condition1:
    # code when condition1 is True

elif condition2:
    # code when condition2 is True

elif condition3:
    # code when condition3 is True

else:
    # code when all conditions are False

# EXAMPLE
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")