---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# 3: Functions

## Learning goals:
- Explain why we need functions in our programs
- Identify key components of a function in Python
- Construct a function block, from scratch
- Convert existing code to a function
- Use a function
- Identify common errors with functions

## What are functions and why do we care about them?
Functions are basically machines that take some __input(s)__, do some __operations__ on the input(s), and then produce an __output__.

Why we need functions:    
- Model your problem so that it can be solved by a computer well aka Computational Thinking
- Make fewer errors (reduce points of failure from copy/paste, etc.)

Motivating example: simple data analysis pipeline to compute percent change in revenue from last year.

We have two sales numbers
- `last_year = "$150,000"`
- `this_year = "$230,000"`

Q: How can we analyze them? What are the subproblems here that we'll need to solve?

```{admonition} A:
:class: toggle
Two main substeps:
1. CONVERT strings to integers
2. COMPUTE the percent change
```

Here's an example program that could solve this problem:

```{code-cell} ipython3
# DEFINE the two sub-functions we need

def clean_sale_number(saleNumStr): 
    
    # 1: remove dollar signs
    saleNumStr = saleNumStr.replace("$", "")
    
    # 2: remove the comma
    saleNumStr = saleNumStr.replace(",", "")
    
    # 3: convert to float
    result = float(saleNumStr)
    
    return result 

def compute_percent_change(lastYear, thisYear):
    
    # first make the input numbers actually numbers
    lastYear = clean_sale_number(lastYear)
    thisYear = clean_sale_number(thisYear)

    # then compute the percent change
    result = ((thisYear - lastYear)/lastYear)*100
    return result

# actually use (CALL) the functions.

lastYear = "$500,000.35"
thisYear = "$1,256,000.21"
percentChange = compute_percent_change(lastYear, thisYear)
print(percentChange)
```

Without functions, we would need to copy/paste the clean sales operation. This is both annoying and increases the likelihood of errors!

```{code-cell} ipython3
def compute_percent_change(lastYear, thisYear):
    
    # make the input lastYear actually a number

    # 1: remove dollar signs
    lastYear = lastYear.replace("$", "")
    
    # 2: remove the comma
    lastYear = lastYear.replace(",", "")
    
    # 3: convert to float
    lastYear = float(lastYear)
    
    # make the input thisYear actually a number
    
    # 1: remove dollar signs
    thisYear = thisYear.replace("$", "")
    
    # 2: remove the comma
    thisYear = thisYear.replace(",", "")
    
    # 3: convert to float
    thisYear = float(thisYear)

    # then compute the percent change
    result = ((thisYear - lastYear)/lastYear)*100
    return result
```

You'll really start to feel a practical need for functions once your programs start to approach a regular level of complexity, starting in Module 2 or so.

But it's a fundamental concept for computational thinking (specifically problem decomposition), so it's worth encountering it early, so we can start drilling that way of thinking. It also makes the PCEs a little less confusing!

Let's take a closer look at what a function actually is in Python.

### Function definition

In Python, a function consists of three main components:
1. **Parameters**: what are the main __input__ variables your function will be manipulating?
2. **Body of the function:** what __operations__ will your function be performing on/with the input variables?
3. **Return value**: what will your function's __output__ be (i.e., what will come out of the function to the code that is calling the function)?

Let's consider an example of a function to convert minutes to hours. 

```{code-cell} ipython3
def minutes_to_hours(minutes):
    result = minutes/60
    return result
```

The function `minutes_to_hours()` has input __parameter__ `minutes`, a __body__ of code that divides `minutes` by 60 and stores it in the variable `result`, and a `return value` that is the value of the variable `result`

So that's the conceptual bits of a function. There's also the syntax bits that make up a function definition. To see what they are, let's compare the function definition to two other function definitions.

```{code-cell} ipython3
def greet_user(username):
    msg = "Hello " + username + "!"
    return msg
```

```{code-cell} ipython3
def longer(inputString, howMany):
    toAdd = "a"*howMany
    result = inputString + toAdd
    return result
```

There's a fair bit to notice here. 

Q: What do you see here that you think is important?
```{admonition} A:
:class: toggle
1. def 
2. return, indented under the function name
3. name of the function
4. parentheses after the function name
5. one or more parameters inside the parentheses
6. colon
7. indented code as the body of the function (everything between the colon and the return statement)
```

Let's practice with another function definition.

```{code-cell} ipython3
def greet_user(username):
    msg = "Hello " + username + "!"
    return msg
```

Q: What are the parameters, function body, and return value(s) here?
```{admonition} A:
:class: toggle
1. Parameter(s): username
2. Function body: `msg = "Hello " + username + "!"`
3. Return value: msg
```

And another example:

```{code-cell} ipython3
def longer(inputString, howMany):
    toAdd = "a"*howMany
    result = inputString + toAdd
    return result
```

Q: What are the parameters, function body, and return value(s) here?
```{admonition} A:
:class: toggle
1. Parameter(s): inputString, howMany
2. Function body: lines 2 and 3
3. Return value: result
```

NOTE: when you run a function definition, there should be no output. The same thing is happening as with a variable assignment statement, like `a = 3`. Python is storing the code in the function body (and its associated parameters and return values) to be used later, just like with `a = 3`, Python is storing the value of `3` in the variable `a` to be used later.

So. When you write a colon after a function name, and indent code after it, it's equivalent to an assignment statement (you're assigning the code body and return statement to the function name).

### Function call

In Python, function calls consist of at least:
1. A reference to the **function name**
2. One or more **arguments** (inside **parentheses**) to pass as input to the function (how many and what type is determined by the parameters in the function definition)
Alongside other code

Let's look at an example.

Suppose we have defined a function `minutes_to_hours`.

```{code-cell} ipython3
def minutes_to_hours(minutes):
    result = minutes/60
    return result
```

As we've noted, when we run this code by itself, the code in the function definition doesn't actually run: instead, Python is saving the function to memory and associating it with the label `minutes_to_hours`.

To run the code and use the function, we need to write code that *calls* (i.e., uses) the function, like this:

```{code-cell} ipython3
mins = 150
# call the minutes_to_hours function
# with mins as an argument
# and store the return value in the variable hours
hours = minutes_to_hours(mins)
print(hours)
```

Here, we have the function name (`minutes_to_hours`), and the argument `mins` being passed as input to the function, and code that takes the return value from the function and prints it out.

Here it is in pictures

```{image} assets/function-definition-annotated.png
:alt: typeError
:class: bg-primary mb-1
:width: 800px
:align: center
```

```{image} assets/function-call-annotated.png
:alt: typeError
:class: bg-primary mb-1
:width: 500px
:align: center
```

What's happening under the hood at this function call is:
1. Define the variable `mins` and put the value 150 in it
2. Retrieve the code associated with the function name `minutes_to_hours` and give it `mins` as an input argument
3. Run the code associated with the function name `minutes_to_hours` with `mins` as input, and return the result
4. Pass that result to the `print` function (yes, this is a function also!) as an input argument.

I recommend that you [plug this code (and really all the other examples in this lecture) into pythontutor](https://pythontutor.com/python-compiler.html#mode=edit) to step through it line by line. It really helps to build your intuition for what is happening.

Let's look at another example pair. 


```{code-cell} ipython3
def bouncer(age):
    result = age >= 21
    return result
```

```{code-cell} ipython3
your_age = 24
come_in = bouncer(your_age)
print(come_in)
```

<!-- Q: Where are the parameters and arguments?
```{admonition} A:
:class: toggle
Parameter: age
Argument: your_age
``` -->

### Key idea: Arguments vs. parameters

Parameters and arguments are easy to confuse. They both go in the parentheses after the function name. So what's the difference?

It helps me to think of them as two sides of a special kind of variable assignment statement.

Parameters are the key *variables* in the function (what's on the left side of an assignment statement). 
Arguments are the *values* you assign to those variables when you use the function (what's on the right side of an assignment statement).

As a beginner, it's common to wonder when you look at a function definition, "Where do the variables in the function get their value? I don't see any assignment statements?" Arguments and parameters are the answer! At least some of the function's variables are parameters, and they get their value from the *arguments* in the function call. 

Let's look at our `minutes_to_hours` example again, all together:

Here's another example.

```{code-cell} ipython3
def minutes_to_hours(minutes):
    result = minutes/60
    return result

mins = 150
hours = minutes_to_hours(mins)
print(mins, "minutes is", hours, "hours")
```

In this program, when line 6 (`hours = minutes_to_hours(mins)`) executes, Python calls the function and passes the argument `mins` into the function and gives its value to the `minutes` parameter in the `minutes_to_hours` function.

If you want to make life easier for yourself when you're still learning, you can make the mapping from arguments (on the right) to parameters (on the left) in a function call explicit in the function call code
```{code-cell} ipython3
minutes_to_hours(minutes=90)
```

Equivalently:
```{code-cell} ipython3
mins = 120
minutes_to_hours(minutes=mins)
```

And:
```{code-cell} ipython3
my_age = 19
bouncer(age=my_age)
```

We'll actually see this format (called "[keyword arguments](https://www.w3schools.com/python/gloss_python_function_keyword_arguments.asp)") come back later on when we deal with more complicated functions, especially when we borrow code from other libraries! This is in contrast to the "[positional argument](https://www.geeksforgeeks.org/python/keyword-and-positional-argument-in-python/)" approach for simpler functions, where Python gives the 1st argument's value to the 1st parameter's value, 2nd argument to the 2nd parameter, and so on.

### The basic pattern for using functions: DEFINE a function, use (CALL) a function

So we've seen that there are two main parts of using functions in programming: 1) DEFINING a function, and then 2) CALLING (using) a function.

Here's another example:

```{code-cell} ipython3
# DEFINE a function that takes an input string and adds a specified number of characters to it
def longer(inputString, howMany):
    
    # create a string that is 
    # howMany characters long (by multiplying a single character string by that length)
    toAdd = "a"*howMany
    
    # concatenate that "toAdd" string to the input string
    # and store in the result variable
    result = inputString + toAdd
    
    # return the result
    return result
```

```{code-cell} ipython3
# define a string
s = "huzzah"

# look at the current length of the string, using the len() function
print("S is originally", len(s), "characters long. Here it is:", s)

# define how much longer we want to make the string
howMany = 3

# CALL the longer() function to make a string that is that many characters longer than the string s
# and store the return value in the new variable longer_s
longer_s = longer(s, howMany)

# look at the length of the longer string, using the len() function
print("S is now", len(longer_s), "characters long after adding", howMany, "characters. Here it is:", longer_s)
```

The first chunk of code defines the function `longer()`. The second chunk of code *calls* the function on line 12 (`longer_s = longer(s, howMany)`).

This define-call sequence should look similar to our PCE structure: your solutions.py files define functions, and your tests.py files call those functions to test them with different inputs. 

In later more complex programs, you often define a few functions at once, or borrow them from other bits of code, and then use them in a single program. You can also compose functions into larger functions!

### Practice

Let's practice! Look at the following two chunks of code. 

```{code-cell} ipython3
# A
def greet_user(username):
    msg = "Hello " + username + "!"
    return msg
```

```{code-cell} ipython3
# B
username = "Joel"
greeting = greet_user(username)
print(greeting)
```

Q: Which one is the function definition and which one is the function call?
```{admonition} A:
:class: toggle
A is the function definition, and B has code that calls the function.
```

Q: Which line in the function call cell is actually calling the function?
```{admonition} A:
:class: toggle
Line 3!
```

Let's go back to our example sales cleaning program.

```{code-cell} ipython3
# DEFINE the two sub-functions we need

def clean_sale_number(saleNumStr): 
    
    # 1: remove dollar signs
    saleNumStr = saleNumStr.replace("$", "")
    
    # 2: remove the comma
    saleNumStr = saleNumStr.replace(",", "")
    
    # 3: convert to float
    result = float(saleNumStr)
    
    return result 

def compute_percent_change(lastYear, thisYear):
    
    # first make the input numbers actually numbers
    lastYear = clean_sale_number(lastYear)
    thisYear = clean_sale_number(thisYear)

    # then compute the percent change
    result = ((thisYear - lastYear)/lastYear)*100
    return result

lastYear = "$500,000.35"
thisYear = "$1,256,000.21"
percentChange = compute_percent_change(lastYear, thisYear)
print(percentChange)
```

Q: Where are the function calls?
```{admonition} A:
:class: toggle
On line 28 (`compute_percent_change(lastYear, thisYear)`), but also inside the body of the `compute_percent_change()` function definition on lines 19 and 20, calling the `clean_sale_number()` function for both `lastYear` and `thisYear` variables!
```

## How to define functions

### Writing a function from scratch

There are a few main steps to follow:
1. Write the code that goes in the function (the steps)
2. Create a function definition
    - Write the skeleton of your function (`def`, a name, parentheses, `return` statement)
3. Integrate your code into the function:
    - Fill out the parameters
    - Fill out the body of the code
    - Fill out the return statement
4. Run the function definition cell (this defines the function for Python)

Let's look at an example together!

Let's write a function that applies a discount to a sale, given the sale amount and the percentage discount.

Here is code that successfully computes a saleAmount after applying a discount
```{code-cell} ipython3
saleAmount = 10.00
percentageDiscount = 0.3

saleAmount - saleAmount*percentageDiscount
```

And here is a function definition that encapsulates that code into a function `apply_discount()`, with `saleAmount` and `percentageDiscount` as input **parameters**, the main computation from above applying the discount in the **function body**, and then defining the **return value** as the `finalAmount`.
```{code-cell} ipython3
def apply_discount(saleAmount, percentageDiscount):
    finalAmount = saleAmount - saleAmount*percentageDiscount
    return finalAmount
```

Here's an example of how we can call that function, using our explicit argument-parameter notation from before.
```{code-cell} ipython3
apply_discount(saleAmount=325.99, percentageDiscount=.2)
```

And another simple one: give me the area of a triangle, given its base and height.

Here's functioning code:
```{code-cell} ipython3
b = 3
h = 2
0.5*b*h
```

And here's a function definition for a function `triangle_area()` that has `base` and `height` (renamed here from `b` and `h` for readability, and we make sure to propagate that change to the **function body**), and `area` as the **return value**.
```{code-cell} ipython3
def triangle_area(base, height):
    area = 0.5*base*height
    return area
```

Here's an example of calling that function.
```{code-cell} ipython3
triangle_area(base=5, height=10)
```

### Converting existing code into a function

The steps here are similar to writing from scratch, with the main difference that we:
1. Decide which of the variables in the existing code are inputs (parameters), and which ones are outputs (return values), then put those in the function definition and return statements.
2. Integrate the rest of the working code into the body of the function.

Here we've written the code for our substeps of converting the numbers into.. numbers. We know it works.

```{code-cell} ipython3
# test number
rawSale = "$600,153.25"

# make the input numbers actually numbers
# 1: remove dollar signs
cleanSale = rawSale.replace("$", "")

# 2: remove the comma
cleanSale = cleanSale.replace(",", "")

# 3: convert to float
result = float(cleanSale)
result # the output
```

We can then encapsulate this into a function `clean_sale_number()`, with `rawSale` as the main input **parameter**, and the various operations cleaning the string in the **function body**, and the resulting float value as a **return value**.

```{code-cell} ipython3
# 1. decide which variables are inputs/outputs, fill out function skeleton
# 2. integrate rest of code into the body of the function

# rawSale is input variable, so it's a parameter
def clean_sale_number(rawSale):

    # 1: remove dollar signs
    cleanSale = rawSale.replace("$", "")
    
    # 2: remove the comma
    cleanSale = cleanSale.replace(",", "")
    
    # 3: convert to float
    result = float(cleanSale) 
    return result
```

We can then call the function like this:
```{code-cell} ipython3
clean_sale_number(rawSale="$2,115,000")
```

### Practice: converting code to functions

For each exercise below, you are given working code with test inputs. Your task is to:
1. Identify which variables are **inputs** (parameters) and which are **outputs** (return values)
2. Write a function definition that encapsulates the code
3. Call your function with different arguments to verify it works

#### Exercise 1: Gym discount eligibility

A gym offers a discount if you are either a student or over 65 years old. Here is working code that checks discount eligibility based on student status and age:

```{code-cell} ipython3
isStudent = False
age = 66

isEligible = isStudent == True or age > 65
print(isEligible)
```

Convert this into a function, then call it with different arguments to test it.

```{admonition} Hint
:class: toggle
- What is the key operation for the function body? The boolean expression checking isStudent and age
```
Here is some starter code (parameters and return statement are done, just fill in the body of the function!).
```{code-cell} ipython3
def check_discount(isStudent, age):
    # replace with your code
    return result

# test calls
check_discount(isStudent=True, age=35)   # True (student)
check_discount(isStudent=False, age=66)  # True (over 65)
check_discount(isStudent=False, age=30)  # False (neither)
```

#### Exercise 2: Flour for cookies

A recipe calls for 0.167 cups of flour for each cookie. Here is working code that computes the flour needed to make any given number of cookies:

```{code-cell} ipython3
numCookies = 15

numCupsFlour = numCookies * 0.167
print(numCupsFlour)
```

Convert this into a function, then call it with different arguments to test it.

```{admonition} Hint
:class: toggle
- What is the input? `num_cookies`
- What is the key operation for the function body? The math expression multiplying numCookies by the desired conversion
- What is the output? The amount of flour needed
```

Here is some starter code (fill in the right parameters, function body and return values!)

```{code-cell} ipython3
# add parameters
def flour_needed():
    # add body

    # add return statement

# test calls
flour_needed(num_cookies=45)  # 7.515
flour_needed(num_cookies=8)   # 1.336
```

#### Exercise 3: Late penalty on an assignment

Our syllabus has a late policy: 0.25% deduction per hour late. Here is working code that, given the number of hours late, the score, and the maximum score, calculates the final score after applying the late penalty:

```{code-cell} ipython3
hoursLate = 3
score = 30
maximumScore = 50

percentDeduction = hoursLate * 0.25
pointsDeduction = percentDeduction / 100 * maximumScore
finalScore = score - pointsDeduction
print(finalScore)
```

Convert this into a function, then call it with different arguments to test it.

```{admonition} Hint
:class: toggle
- What are the inputs? `hours_late`, `score`, and `maximumScore`
- What is the key operation for the function body? The lines of code computing the values for percentDeduction, pointsDeduction, and finalScore
- What is the output? The final score after the late deduction
- The body of the function should include the intermediate computation steps
```

Here is some starter code (fill in the right parameters, function body, return values, and function calls!)

```{code-cell} ipython3
# add parameters
def apply_late_penalty( ):
    # add function body

    # add return statement
    

# test calls
# add in arguments!
apply_late_penalty()
apply_late_penalty()
``` 

## Common errors when using functions

### Hard-coding parameters

As a beginner, it's common to look at a function definition, wonder why the variables don't have assigned values, and write assignment statements to give them values inside the body of the function. We call this "hard-coding" the parameters (setting them to a fixed value, so they are no longer variables, but hard-coded values). 

This is bad, because the function will no longer do its job of producing an output based on operations on the given inputs: it will only do operations on the hard-coded parameters, so it will produce the same result no matter what arguments are passed in during a function call!

As an example, the following function will always produce `2` as its output, no matter what arguments we pass in.
```{code-cell} ipython3
def minus(x, y):
    x = 3
    y = 1
    result = x - y
    return result
```

This is because we are *redefining* `x` and `y` in the body of the function and giving them *hard-coded* values of `3` and `1`. This makes the function ignore any argument values that are assigned to the parameters, and only use the hard-coded values, since the hard-coding happens after the arguments' values are passed to the parameters when the function is called. 

So this function will *only* subtract precisely `3` from `1`, rather than subtracting any number `y` from `x`. For instance, this function call will yield `2` instead of `5`, as we would expect:

```{code-cell} ipython3
result = minus(10, 5)
print(result)
```

### Mismatching arguments and parameters

Another common error is to call a function with a different number/order of arguments than the expected parameter number/order, which is a problem when you call functions in the common "[positional argument](https://www.geeksforgeeks.org/python/keyword-and-positional-argument-in-python/)" mode (just listing arguments in order of the parameters, as opposed to explicit "[keyword arguments](https://www.w3schools.com/python/gloss_python_function_keyword_arguments.asp)")
<!-- forgetting to use the parameters defined for your function -->

<!-- Make sure that the body of your function is operating on the actual input variables you're passing in via your parameters! This is a common error to make when you're converting code to functions. -->

<!-- For example, if we define a function like this, notice how the `x` and `y` parameters are never actually used in the function body!
```{code-cell} ipython3
# example
def minus(x, y):
    result = a - b
    return result
```

When we call this function with `a` and `b` arguments, the code will run and produce expected output. BUT. The function will only work in this specific function call, when `a` and `b` are defined. And it will always use the values of `a` and `b`, even if you give it different parameters.
```{code-cell} ipython3
a = 3
b = 2
diff = minus(a, b)
print(diff)
```

For example, we would expect this function call to give us the value of `10`, but it will still give `1` as the result, since the function body is ignoring the `x` and `y` input parameters, and operating directly on `a` and `b`. 
```{code-cell} ipython3
x = 12
y = 2
diff = minus(x, y)
print(diff)
```

Finally, if you define a certain number of parameters, but give it a different number of arguments, Python will fail with a TypeError. -->

For instance, if you define a function like this that expects `x` and `y` in that order:
```{code-cell} ipython3
# example
def minus(x, y):
    result = x - y
    return result
```

And call the function like this:
```{code-cell} ipython3
minus(3)
```

When you run the program, it will halt with an error message: "TypeError: minus() missing 1 required positional argument: 'y'"

The reason it fails with this TypeError in this case is because for the 2nd parameter, because it's missing a corresponding 2nd argument.

The fix is to make sure that you have the same number of arguments as parameters. Again, writing out your function calls in explicit argument-parameter mappings can help make sure that you don't make this error, like this:
```
minus(x=3, y=2)
```

But! You have to make sure you remember the name of the parameter and use that. Tradeoffs! :)

### Missing / incorrect return statements

Technically, from a syntax perspective, the return statement in a function definition is optional. Functions that don't have return values are syntactically valid (legal code); they're known as a "void functions".
- Confusingly, in Python, a void function still does return a value: a special Python value called `None` that represents "nothing".
- Honestly, void functions kind of break the model of what a function should be (subcomponents in a larger program). In my experience, they are also quite rare in practice, except as, say, a main control loop, or the "main" procedure in a script. So, if you're confused by void functions and find "regular" (also sometimes called "fruitful") functions (with return values) easier to think conceptualize, I'm happy.

For now, I want you to pretend void functions don't exist (i.e., do *not* write void functions; always have a `return` statement).

So why am I telling you this then?
- You'll see void functions in many Python tutorials. Often you'll even learn about void functions *before* fruitful (or regular) functions. I think this may be because it has fewer moving parts? I'm not really sure. 
- Practically, too, if you leave out a `return` statement, your code will still run! So the *syntax* is fine! But you'll probably have made a semantic error (you meant to give the output of the function to some other piece of code, but the code you wrote isn't actually doing that). **This is a very common error for beginning programmers.** So you if run into this, you're in good company! If you're pretty sure that the code in the body of the function is correct, but you're confused by what happens when the function is used (e.g., it's not giving you the value you expect), but the code runs, it's a good idea to check your `return` statement!

An extremely common way to make this mistake is to write a print statement in the function body to produce output to you, the user, and declare that it works, but forget to write a return statement

Example: if we define the functions this way, without return statements, they will still run! BUT we won't be able to use their results in a meaningful way, leading to an error if we try
```{code-cell} ipython3
def tip(base, percentage):
    result = base * percentage
    print(result)
    
def tax(base, tax_rate):
    result = base * tax_rate
    print(result)
```

This code will yield a strange `TypeError` complaining about trying to do math with an `int` and a `NoneType` (because the functions produce `None` return values by default!)

```
base = 3
tip_rate = 0.2
tax_rate = 0.08

total_check = tip(base, tip_rate) + base + tax(base, tax_rate)
print(total_check)
```

When you see this kind of error, it's good practice to go back and check that your functions have return statements that produce the output you expect from the function. 

### NameErrors

Functions are like variables, in that they are a way for Python to use a label (function name, variable name) to retrieve something from memory (a function, a value) to use in a program. So, just like variables, function calls can have a similar `NameError`, which just means that you're asking Python to retrieve a function with a label, but there isn't a box in memory with that label on it.

The same principles apply for variables as functions for this: make sure that your function is defined *before* you call it, and that the function call references the correct name of the function (not a misspelled one). Again, using autocomplete is your friend!

For instance, the following program will result in a `NameError`:

```{code-cell} ipython3
def clean_sale_number(rawSale):

    cleanSale = rawSale.replace("$", "")
    cleanSale = cleanSale.replace(",", "")
    
    result = float(cleanSale) 
    return result

clean_sale(rawSale="$2,115,000")
```

Why? Because the function is defined with the label `clean_sale_number`, and we're asking Python to go look for a function with the label `clean_sale` (which doesn't exist!). Here, the fix would be to change line 9 to `clean_sale_number(rawSale="$2,115,000")`.