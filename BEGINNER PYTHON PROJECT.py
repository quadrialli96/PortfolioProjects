# CHAPTER 1 (STATEMENT)
x = 1
# This is called assignment stamement because you're referencing 1 as variable X with the = to operator
print(x)  # This line of code is called a print statement
# This gives you a result of 1, because the X was assigned the "1" integer
x = x + 1  # This line of code is also called assignment with expression
print(x)
# These are called sequential steps in programming language because they collect information from eachother to produce an output.
B = 6
if B > 4:
    print('bigger')
if B < 4:
    print('smaller')
# These are called Conditional statement because they do run your output based on the condition given, the secodn line of code is then skipped due to the conditions not being met.
n = 5
while n > 0:
    print(n)
    n = n - 1
print('blast!')
# This is referred to as a "LOOP"(repeated steps), they have iteration variables that change each time through a loop.
# Infinite loops run forever. An example is if you replace (-) with a (+), it will create an infinite loop that gives variables that are bigger than 0.

# CHAPTER 2 (EXPRESSIONS)
# Fixed Values such as numbers, letters, strings, are called "CONSTANT" because their value doesn't change
# Numeric constant - >>> print(123) or print(98.6)
# String Constant use single quotes (') or double (") - >>> print('Hello World')
# Variable is a named place in the memory where data can be stored and later retrieved using the variable name. You get to choose your own variable name and the contents of a variable can be changed in a later statement.
x: float = 12.2
y = 14
x = 100  # In this case "X" was changed at a later statement from 12.2 to 100
# Python variable name rules- MUST start with a letter or underscore, Must consist of letters, numbers, and underscores & is case sensitive. E.G. spam, eggs, spam23, _speed.
# Numeric expressions +(addition), -(subtraction), *(mulptiplication),/(division), **(power), %(remainder/ modulo). PEMDAS process goes first when doing calculation, then the remaining calculation goes from left to right.
_hi = 'hello' + ' there'
print(_hi)
# This called CONCATENATE because it adds 2 different strings together.
type(_hi)
# This tells you what type of variable or constant thats been looked for.
# stings are characterized as letters, whole digit number is an integer and decimal points numbers are considered float.

# TYPE CONVERSION. - When integer and float are added together in the same expression, the integer is implicitly converted to a float.
print(float(99) + 100)
# 99 is converted into a flaot from 99 to 99.0 then added to 100 gives 199.0

# STRING CONVERSIONS - int() and float() can be used to convert between strings and integers
# EXAMPLE
# okay = '123'
# type(okay) will output string
# print(okay + 1) will output error since you cant concatenate a string and an integer
# nice = int(okay) is going to convert okay which consist of 123 to an integer
# type(nice) this will then result to the output type being an integer

# CONVERTING USER INPUT EXAMPLE
#inp = input('europe floor?')
#var: int = 0
#usf = int(inp) + 1
#print('US floor', usf)
# this is supposed to print out "europe floor? 0, US floor 1" but it's not working on pycharm because i don't have the data that instructor was working with
b = 1 + 2
print(b)