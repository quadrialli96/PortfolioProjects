# CHAPTER 1 (STATEMENT)
x = 1
# This is called assignment statement because you're referencing 1 as variable X with the = to operator
print(x)  # This line of code is called a print statement
# This gives you a result of 1, because the X was assigned the "1" integer
x = x + 1  # This line of code is also called assignment with expression
print(x)
# These are called sequential steps in programming language because they collect information from each other to produce
# an output.
B = 6
if B > 4:
    print('bigger')
if B < 4:
    print('smaller')
# These are called Conditional statement because they do run your output based on the condition given, the second line
# of code is then skipped due to the conditions not being met.
n = 5
while n > 0:
    print(n)
    n = n - 1
print('blast!')
# This is referred to as a "LOOP"(repeated steps), they have iteration variables that change each time through a loop.
# Infinite loops run forever. An example is if you replace (-) with a (+), it will create an infinite loop that gives
# variables that are bigger than 0.

# CHAPTER 2 (EXPRESSIONS)
# Fixed Values such as numbers, letters, strings, are called "CONSTANT" because their value doesn't change
# Numeric constant - >>> print(123) or print(98.6)
# String Constant use single quotes (') or double (") - >>> print('Hello World')
# Variable is a named place in the memory where data can be stored and later retrieved using the variable name. You
# get to choose your own variable name and the contents of a variable can be changed in a later statement.
x: float = 12.2
y = 14
x = 100  # In this case "X" was changed at a later statement from 12.2 to 100
# Python variable name rules- MUST start with a letter or underscore, Must consist of letters, numbers, and underscores
# & is case sensitive. E.G. spam, eggs, spam23, _speed.
# Numeric expressions +(addition), -(subtraction), *(multiplication),/(division), **(power), %(remainder/ modulo).
# process goes first when doing calculation, then the remaining calculation goes from left to right.
_hi = 'hello' + ' there'
print(_hi)
# This called CONCATENATE because it adds 2 different strings together.
type(_hi)
# This tells you what type of variable or constant that's been looked for.
# stings are characterized as letters, whole digit number is an integer and decimal points numbers are considered float.

# TYPE CONVERSION. - When integer and float are added together in the same expression, the integer is implicitly
# converted to a float.
print(float(99) + 100)
# 99 is converted into a float from 99 to 99.0 then added to 100 gives 199.0

# STRING CONVERSIONS - int() and float() can be used to convert between strings and integers
# EXAMPLE
# okay = '123'
# type(okay) will output string
# print(okay + 1) will output error since you cant concatenate a string and an integer
# nice = int(okay) is going to convert okay which consist of 123 to an integer
# type(nice) this will then result to the output type being an integer

# CONVERTING USER INPUT EXAMPLE
# inp = input('europe floor?')
# usf = int(inp) + 1
# print('US floor:', usf)
# this is supposed to print out "europe floor? 0, US floor 1" but it's not working on pycharm because i don't have
# the data that instructor was working with

# CONDITION STEPS (TWO WAY DECISION) - One of the statements is going to run based on the information given.
h = 5
if h < 10:
    print('smaller')
else:
    print('bigger')
# It's referred to as conditional statement because the output runs based on if the condition.
# You can indent a line of code by typing 4 spaces before the line of codes needed.
# COMPARISON OPERATOR - Less than(<), Less than or Equal to(<=), Equal to (==), Greater than or Equal to (>=),Greater(>)
# Not equal (!=)
# Boolean expressions ask a question and produce a Yes or No or True/False result.
# Comparison Operators look at variables but do not change the variable.

# ONE-WAY DECISION - Prints all the information that are in the indentation.
k = 5
print('before 5')
if k == 5:
    print('is 5')
    print('is still 5')
    print('another 5')
print('afterwards 5')

# NESTED DECISIONS is when an if() statement is indented in another
x = 42
if x > 1:
    print('more than one')
    if x < 100:
        print('less than 100')
print('All done')

# MULTI-WAY
j = 1
if j < 2:
    print('small')
elif j < 10:
    print('Medium')
else:
    print('LARGE')
print('im done')
# Although 1 is less than both 2 & 10, "small" was printed out because the first function gets triggered first.
# The "try:" and "except:" statement are used whenever you have a risky code.
astr = '123'
try:
    lam = int(astr)
except:
    lam = -1
print('second', lam)


# In this case, the input statement was converted from a string to an integer easily because it contains numbers.
# If 'astr" contained letters, it would print out the except statement as an alternative.

# USING FUNCTIONS
# STORED AND REUSED STEPS. it stores functions in order to avoid repeated steps.
def thing():
    print('hello')
    print('fun')
thing()
print('zip')
thing()
# MAX FUNCTION
big = max('hello world')
print(big)
# W is the answer that the execution of the program gives us since "w" is the max when we look at alphabetical order
# TYPE CONVERSIONS - examples
print(float(99) / 100)
f = 42
type(f)
n = float(f)
print(n)

# STRING CONVERSIONS - examples
soke = '123'
type(soke)
noke = int(soke)
print(noke)
coke = noke + 1
print(coke)

# BUILDING YOUR OWN FUNCTION
# New function is created using "def" keyword
# We indent the body of the function
# This defines the function but does not execute the body of the function.
def print_lyrics():
    print('i need you right now')
    print('ill never snitch on you daddy')
    print("you're the best")
print_lyrics()

# ARGUMENTS - Is a value we pass into the function as its input when we call the function.
# we use arguments so we can direct the function to do different kinds of work when we call it at different times.
# we put the arguments in parenthesis after the name of the function
big = max('hello worlx')
print(big)
# In this case x was the output since x is the max
# PARAMETERS - is a variable which we use in the function definition
# It is the handle that allows the code in the function to access the arguments for a particular invocation.
def greet(lang):
    if lang == 'es':
        print('hola')
    elif lang == 'fr':
        print('bonjour')
    else:
        print('hello')
greet('en')
greet('es')
greet("fr")

# RETURN VALUES - often a function will take its arguments, do some computation and return a value to be used as the
# value of the function call in the calling expression.
def greet():
    return "hello"
print(greet(), "glenn")
print(greet(), "quadri")

# MULTIPLE PARAMETERS AND ARGUMENTS
def addtwo(a, b):
    added = a + b
    return added
l = addtwo(3, 5)
print(l)

# BREAKING OUT OF A LOOP
# The  break statement ends the current loop and jumps to the statement immediately following the loop.
# The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration

# A SIMPLE DEFINITE LOOP
#for k in [5, 4, 3, 2, 1]
#    print(k)
#print('blastoff')
# A DEFINITE LOOP WITH STRINGS
friends = ['joseph', 'glenn']
for friend in friends:
    print('happy new year', friend)
print('done')
# FINDING THE LARGEST VALUE
largest_so_far = -1
print('before', largest_so_far)
for the_num in [9, 41, 12, 3, 74,15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('after', largest_so_far)

# COUNTING IN A LOOP
cork = 0
print('before', cork)
for thing in [9, 41, 12, 3, 74, 15] :
    cork = cork + 1
    print(cork, thing)
print('after', cork)

# ADDITION IN A LOOP
cork = 0
print('before', cork)
for thing in [9, 41, 12, 3, 74, 15] :
    cork = cork + thing
    print(cork, thing)
print('after', cork)

# FINDING AVERAGE IN A LOOP
count = 0
sum = 0
print('before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)

# FILTERING IN A LOOP - if statement is used to filter in a loop.
print('before')
for thing in [9, 41, 12, 3, 74, 15] :
    if thing > 20 :
        print('large number', thing)
print('after')

# BOOLEAN VARIABLE - only has a true or false value.
# Lets look for "3" in this loop. Once 3 is found other value shows true even though its not true
found = False
print('before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
    print(found, value)
print('after', found)

# FINDING THE SMALLEST VALUE
smallest = None
print('before', smallest)
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('after', smallest)