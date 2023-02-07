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

+++ {"id": "IUP5mKyTxbRy"}

# 3: Functions

+++ {"id": "TB-Kg9GExbRz"}

## Learning goals:
- Explain why we need functions in our programs
- Identify key components of a function in Python
- Construct a function block, from scratch
- Convert existing code to a function
- Use a function
- Identify common errors with functions

+++ {"id": "g-lkfdphxbR0"}

## What are functions and why do we care about them?
Functions are basically machines that take some __input(s)__, do some __operations__ on the input(s), and then produce an __output__.

Why we need functions:    
- Model your problem so that it can be solved by a computer well aka Computational Thinking
- Make fewer errors (reduce points of failure from copy/paste, etc.)

Motivating example: simple data analysis pipeline to compute percent change in revenue from last year.

We have two sales numbers
- `last_year = "$150,000"`
- `this_year = "$230,000"`

How can we analyze them? What are the subproblems here that we'll need to solve?

Keep this in mind, we'll come back to this.

```{code-cell} ipython3
:id: gQbQMwfWNJJN

# to be filled out in class together
```

Also, pragmatically: I'm explaining functions now so the PCEs are a little less confusing.

You'll really start to feel a practical need for functions once your programs start to approach a regular level fo complexity, starting in Module 2 or so.

+++

## The basic pattern: DEFINE a function, use (CALL) a function

```{code-cell} ipython3
# DEFINE a function that takes an input string and adds a specified number of characters to it
def longer(inputString, howMany):
    # what to add; create a string that is 
    # howMany characters long (by multiplying)
    toAdd = "a"*howMany
    # add that long character to the input string
    # and store result
    result = inputString + toAdd
    # return the result
    return result
```

```{code-cell} ipython3
s = "huzzah"
# this is how the string is rn
print("S is originally", len(s), "characters long. Here it is:", s)
# now CALL the longer() function to make s 3 characters longer
howMany = 3
longer_s = longer(s, howMany)
# this is how long the string is now
print("S is now", len(longer_s), "characters long after adding", howMany, "characters. Here it is:", longer_s)
```

Here's another example.

```{code-cell} ipython3
def minutes_to_hours(minutes):
    result = minutes/60
    return result
```

```{code-cell} ipython3
minutes = 150
hours = minutes_to_hours(minutes)
print(minutes, "minutes is", hours, "hours")
```

The first cell is the function definition. The second cell *calls* the function on the 2nd line (`minutes_to_hours(minutes)`).

Let's practice! Look at the following two cells. Which one is the function definition and which one is the function call?

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

Q: Which line in the function call cell is actually calling the function?

A: 

+++

This define-call sequence should look similar to our PCE structure! 

In later more complex programs, you often define a few functions at once, or borrow them from other bits of code, and then use them in a single program. 

As we talked about, you can also compose functions into larger functions!

Here's an example sequence of functions from our motivating example.

```{code-cell} ipython3
# DEFINE the two sub-functions we need

def clean_sale_number(saleNumStr): 
    # make the input numbers actually numbers
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
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 327
  status: ok
  timestamp: 1612796182560
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: ddTI4mlzDX3f
outputId: b20d9edd-74c2-41e7-dcf8-f989fd05d8ee
---
# actually use (CALL) the functions.

lastYear = "$500,000.35"
thisYear = "$1,256,000.21"
percentChange = compute_percent_change(lastYear, thisYear)
print(percentChange)
```

Q: Where are the function definitions?

A: 

Q: Where are the function calls?

A: 

+++ {"id": "ifBcaTKuA2jN"}

## Anatomy of a Python function definition and function call

Let's take a closer look at what a function actually is in Python.

### Function definition

In Python, a function consist of three main components:
1. **Parameters**: what are the main __input__ variables your function will be manipulating?
2. **Body of the function:** what __operations__ will your function be performing on/with the input variables?
3. **Return value**: what will your function's __output __be (i.e., what will come out of the function to the code that is calling the function)?

Let's go back to our example of a function to convert minutes to hours. The following function `minutes_to_hours()` has input __parameter__ `minutes`, a __body __of code that divides `minutes` by 60 and stores it in the variable `result`, and a `return value` that is the value of the variable `result`

```{code-cell} ipython3
---
executionInfo:
  elapsed: 501
  status: ok
  timestamp: 1612794869144
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: Fu2eYI2iBrBg
---
def minutes_to_hours(minutes):
    result = minutes/60
    return result
```

There's also the syntax bits that make up a function definition. There's a fair bit to notice here. What do you see here that you think is important?
1. 

+++

Let's practice with another function definition.

```{code-cell} ipython3
def greet_user(username):
    msg = "Hello " + username + "!"
    return msg
```

What are the parts here?
1. Parameter(s):
2. Function body:
3. Return value: 

+++

And another example:

```{code-cell} ipython3
def longer(inputString, howMany):
    toAdd = "a"*howMany
    result = inputString + toAdd
    return result
```

What are the parts here?
1. Parameter(s):
2. Function body:
3. Return value: 

+++

NOTE: when you run a function definition, there should be no output. The same thing is happening as with a variable assignment statement, like `a = 3`. Python is storing the code in the function body (and its associated parameters and return values) to be used later, just like with `a = 3`, Python is storing the value of `3` in the variable `a` to be used later.

So. When you write a colon after a variable name, and indent code after it, it's equivalent to an assignment statement (you're assigning the code body and return statement to the function name).

+++

### Function call

In Python, function calls consist of at least:
1. A reference to the **function name**
2. One or more **arguments** to pass as input to the function (how many and what type is determined by the parameters in the function definition)
Alongside other code

Let's look at an example.

```{code-cell} ipython3
mins = 150
print(minutes_to_hours(mins))
```

Here, we have the function name (`minutes_to_hours`), and the argument `mins` being passed as input to the function, and code that takes the return value from the function and prints it out.

+++

Here it is in pictures

+++

```{image} assets/Function definition (annotated).png
:alt: typeError
:class: bg-primary mb-1
:width: 800px
:align: center
```
<!-- <img src="assets/Function definition (annotated).png" height=600 width=800></img> -->

+++

```{image} assets/Function call (annotated).png
:alt: typeError
:class: bg-primary mb-1
:width: 800px
:align: center
```
<!-- <img src="assets/Function call (annotated).png" height=300 width=500></img> -->

+++

What's happening under the hood at this function call is:
1. Define the variable `mins` and put the value 150 in it
2. Retrieve the code associated with the function name `minutes_to_hours` and give it `mins` as an input argument
3. Run the code associated with the function name `minutes_to_hours` with `mins` as input, and return the result
4. Pass that result to the `print` function (yes, this is a function also!) as an input argument.

Let's look at another example pair. Where are the arguments and parameters?

```{code-cell} ipython3
---
executionInfo:
  elapsed: 553
  status: ok
  timestamp: 1612794865821
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: _h3Kq36sDt8u
---
def bouncer(age):
    result = age >= 21
    return result
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 358
  status: ok
  timestamp: 1612795108919
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: MXSU469VEdn-
outputId: 918bfa03-e68c-42de-f17f-c0144ac3e82f
---
your_age = 24
come_in = bouncer(your_age)
print(come_in)
```

+++ {"id": "ffHIlz8iDDLM"}

### Key idea: Arguments vs. parameters

Parameters and arguments are easy to confuse. They both go in the parentheses after the function name. What's the difference?

It helps me to think of them as two sides of a special kind of variable assignment statement.

Parameters are the key *variables* in the function (what's on the left side of an assignment statement). 
Arguments are the *values* you assign to those variables when you use the function (what's on the right side of an assignment statement).

One tip I have to drive this home is to write your function calls like this, where you actually make this analogy explicit.

We'll actually see this format come back later on when we deal with more complicated functions, especially when we borrow code from other libraries!

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 34
executionInfo:
  elapsed: 321
  status: ok
  timestamp: 1600097615673
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 240
id: oeFZ9HEQP1-9
outputId: b65c174c-8f05-4287-fd22-1f10ca00c9f2
---
# if you want to make life easier for yourself when you're still learning,
# you can make this explicit in the function call code
minutes_to_hours(minutes=90)
```

```{code-cell} ipython3
# equivalently
mins = 120
minutes_to_hours(minutes=mins)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 168
executionInfo:
  elapsed: 336
  status: error
  timestamp: 1612796335820
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: 55B47lMhJkU0
outputId: 2bd6e6df-d49b-46ad-d69c-2dbfa018ed94
---
my_age = 19
bouncer(age=my_age)
```

+++ {"id": "FYVv4YjdCjfS"}

## How to define functions

+++ {"id": "LcXUfJ1qCmZD"}

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

Let's do an example together!

Let's write a function that applies a discount to a sale, given the sale amount and the percentage discount.

```{code-cell} ipython3
# we'll write this together in class
```

+++ {"colab": {"base_uri": "https://localhost:8080/"}, "executionInfo": {"elapsed": 342, "status": "ok", "timestamp": 1612796099954, "user": {"displayName": "Joel Chan", "photoUrl": "https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64", "userId": "15153559228409906865"}, "user_tz": 300}, "id": "2DKG-nQZIzH_", "outputId": "d2f5c8dc-ef18-4d0d-e2cd-2126f15f73d5"}

And another simple one: give me the area of a triangle, given its base and height.

```{code-cell} ipython3
# we'll write this together in class
```

+++ {"id": "21v9caNsEE1A"}

### Converting existing code into a function

The steps here are similar to writing from scratch, with the main difference that we:
1. Decide which of the variables in the existing code are inputs (parameters), and which ones are outputs (return values), then put those in the function definition and return statements.
2. Integrate the rest of the working code into the body of the function.

Here we've written the code for our substeps of converting the numbers into.. numbers. We know it works.

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 351
  status: ok
  timestamp: 1612796487597
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: jezPgHN1Un6v
outputId: dbef3ce5-162c-4d2e-90fa-b1bc9aec6a67
---
# test number
sale = "$600,153.25"
# make the input numbers actually numbers
# 1: remove dollar signs
sale = sale.replace("$", "")
# 2: remove the comma
sale = sale.replace(",", "")
# 3: convert to float
result = float(sale)
result # the output
```

Let's walk through this together.

```{code-cell} ipython3
# 1. decide which variables are inputs/outputs, fill out function skeleton
# 2. integrate rest of code into the body of the function
```

+++ {"id": "Q1vmmUJTE67i"}

## Common errors when using functions

+++ {"id": "yhMs4re7DgN7"}

### Order of execution and NameErrors

Remember: In a computational notebook like Jupyter, Python executes the code in the order that you run the cells. If you run the cells from top to bottom, then it behaves the same way as a script. But if you run the cells in a different order, then it's different. 

This is important because a common error is to forget to run your **function definition** code before you **call the function**. This will result in a `NameError`, which means you're saying something to Python with words it doesn't yet know. The solution is to go back and make sure you do Step 2.

If you're __updating__ your function, you'll get different kinds of errors. Sometimes it will be a silent logical or semantic error (where the code will run, but the results of the code will not be what you intend). So you always want to make sure you run a function definition cell to update it in Python's memory, before you run any code that uses the function.

```{code-cell} ipython3
---
executionInfo:
  elapsed: 292
  status: ok
  timestamp: 1612796852635
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: RlTQSduSUMIB
---
def divide(x, y):
    result = x / y
    result = int(result)
    return result
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 168
executionInfo:
  elapsed: 589
  status: error
  timestamp: 1612796754279
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: 0_yPVfFOUQka
outputId: df90e017-4707-4167-faa6-9f18d873ff33
---
divide(25, 5)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 558
  status: ok
  timestamp: 1612796855373
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: CD7bmreLLY5l
outputId: 0b4534b9-863a-4ddd-d7ae-921b3ebf8642
---
division(25, 3)
```

+++ {"id": "lwqweGQiEzWb"}

### Missing / incorrect return statements

Technically, from a syntax perspective, the return statement in a function definition is optional. Functions that don't have return values are syntactically valid (legal code); they're known as a "void functions".
- Confusingly, in Python, a void function still does return a value (i.e., `None`). 
- Honestly, void functions kind of break the model of what a function should be (subcomponents in a larger program). In my experience, they are also quite rare in practice, except as, say, a main control loop, or the "main" procedure in a script. So, if you're confused by void functions and find "regular" (also sometimes called "fruitful") functions (with return values) easier to think conceptualize, I'm happy.

For now, I want you to pretend void functions don't exist (i.e., do *not* write void functions; always have a `return` statement).

So why am I telling you this then?
- You'll see void functions in many Python tutorials. Often you'll even learn about void functions *before* fruitful (or regular) functions. I think this may be because it has fewer moving parts? I'm not really sure. 
- Practically, too, if you leave out a `return` statement, your code will still run! So the *syntax* is fine! But you'll probably have made a semantic error (you meant to give the output of the function to some other piece of code, but the code you wrote isn't actually doing that). **This is a very common error for beginning programmers.** So you if run into this, you're in good company! If you're pretty sure that the code in the body of the function is correct, but you're confused by what happens when the function is used (e.g., it's not giving you the value you expect), but the code runs, it's a good idea to check your `return` statement!

An extremely common way to make this mistake is to write a print statement in the function body to produce output to you, the user, and declare that it works, but forget to write a return statement

```{code-cell} ipython3
---
executionInfo:
  elapsed: 276
  status: ok
  timestamp: 1612797092002
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: IeGAjCnyF3dw
---
# example: if we define the functions this way, without return statements, they wil still run! 
# but we won't be able to use their results in a meaningful way, leading to an error if we try
def tip(base, percentage):
    result = base * percentage
    print(result)
    
def tax(base, tax_rate):
    result = base * tax_rate
    print(result)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 346
  status: ok
  timestamp: 1612797093648
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: f6ZZFAJbF7-y
outputId: 5dbcbd24-4e97-4fae-d993-556e3a5aa8d5
---
base = 3
tip_rate = 0.2
tax_rate = 0.08

total_check = tip(base, tip_rate) + base + tax(base, tax_rate)
print(total_check)
```

+++ {"id": "_ISyo9rIE48n"}

### Mismatching arguments and parameters

Make sure that the body of your function is operating on the actual input variables you're passing in via your parameters! This is a common error to make when you're converting code to functions.

```{code-cell} ipython3
---
executionInfo:
  elapsed: 282
  status: ok
  timestamp: 1612797269463
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: T7834g2mFwhQ
---
# example
def minus(x, y):
    result = x - y
    return result
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 372
  status: ok
  timestamp: 1612797270436
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: afTKxlcbGDLI
outputId: 7d754367-17d2-450a-f8d3-2c3e26369f4c
---
x = 7
y = 2
diff = minus(x, y)
print(diff)
```

+++ {"id": "G8JNuz9YGPJI"}

You also need to make sure the arguments and parameters match in number and value

```{code-cell} ipython3
---
executionInfo:
  elapsed: 398
  status: ok
  timestamp: 1612797325432
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: cN83vrjWGZEn
---
# example
def minus(x, y):
    result = x - y
    return result
```

```{code-cell} ipython3
x = 3
y = 2
diff = minus(x)
print(diff)
```

This can fail silently (semantic vs. syntax error!)

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 413
  status: ok
  timestamp: 1612797405430
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: re-7xC6cGZEt
outputId: d66ea777-f570-470d-f081-ea0afe6702e5
---
x = 3
y = 2
diff = minus(y, x)
print(diff)
```

This is where the explicit parameter-argument mapping function call pattern can help you.

```{code-cell} ipython3
x = 3
y = 2
diff = minus(x=x, y=y)
print(diff)
```

A related error is hard-coding the variables inside the function body instead of letting the parameter be defined and given its value from the argument

```{code-cell} ipython3
# example
# now, no matter what arguments we pass in, 
# the result will never change
# the key here is to remember that x and y are defined *when the function is called, by passing the value of the argument into the parameter, which we can then use int he body of hte function
def minus(x, y):
    x = 3
    y = 1
    result = x - y
    return result
```
