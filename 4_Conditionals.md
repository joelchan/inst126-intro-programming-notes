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

<!-- +++ {"id": "IUP5mKyTxbRy"} -->

# 4: Conditionals

<!-- +++ {"id": "TB-Kg9GExbRz"} -->

## Learning goals:
- Write Boolean expressions based on English requirements
- Explain different meta-patterns of conditional blocks (nested, chained, with alternative vs. without)
- Construct various types of conditional blocks in Python

<!-- +++ {"id": "g-lkfdphxbR0"} -->

## What are conditionals and why do we care about them?

Conditionals are an example of the fundamental computational thinking concept of **control flow**: setting up structures in our program to control what happens when. You can think of conditionals as "forks in the road" that control what happens *depending on* whether some conditions are true or false.

A set of pictures might help to give the intuition:

```{image} assets/conditional-pictures.png
:class: bg-primary mb-1
:width: 1000px
:align: center
```

Basically anytime you find yourself at a problem step or part of your problem where you say something like "`do something` *based on / depending on / looking at / if* `some condition`", that is a signal that you need a conditional.

Here are some examples:
- decide what to wear: check temperature, check if i'm going to a dress code location
- shopping: check how much money i have, check quality level of the thing, what i need; decide what to buy
- decide what to eat: spiciness, taste, price

What are some other real-world examples of this sort of situation that you can think of? 

## Anatomy of a basic conditional block in Python

Here's a rough diagram of a basic conditional block in Python:

```{image} assets/conditional-logic-generic.png
:class: bg-primary mb-1
:width: 600px
:align: center
```

And here's what it looks like in code

```
# basic conditional block
if BooleanExpression:
    # do something
    # maybe also something more
else:
    # do something else
    # and maybe even more something else
```

- The **if statement**
    - The if keyword signals that a conditional block is starting.
    - The Boolean expression determine where to go in the conditional block
        - `True` goes to the if branch; `False` goes to the else branch
    - The statement needs to end in a colon to signal that the statement has ended. This is the same as with function definitions, and as we will see, with iteration loops also.
- The "if" (`True`) **branch code**: what should happen if the Boolean expression evaluates to `True`?
    - Needs to be indented because of scope (same with functions; also will be true of loops)
- The **else statement**: 
    - Signals that an else branch will be specified next
    - Just the else keyword and a colon
- The "else" (false) **branch code**: what should happen if the Boolean expression evaluates to `False`?
    - Also needs to be indented

### Aside: indentation and branch code

Notice the idea of branch code: it's code that "belongs" to the branch. We only run it if we go into the branch.

In Python, we control what belongs to what with **indentation**. In other languages, you use things like curly braces (e.g., Java, Javascript).

**Note:** Unlike functions, `if`/`else` blocks do **not** create a new scope in Python. Variables assigned inside an `if` block are still accessible after the block finishes. The key thing indentation controls here is *which code runs in which branch*.

As an example, consider the following code: how many times do you think we will print the message "hello world"? Why?

```{code-cell} ipython3
# if i have passed all the requirements for graduation, print graduate! otherwise, print need to do more
# did i accumulate at least 25 credits AND earn at least a 3.0 GPA?
n_credits = 30
gpa = 3.95
hello = "hello world!"
if n_credits >= 25 and gpa >= 3.0:
    print("Go ahead")
    print(hello)
else:
    print("Take more classes")
    print(hello)
```

The answer: only once! Because both print statements are indented inside a conditional branch, only one branch executes: either the `if` branch or the `else` branch, but never both.

### Examples of conditionals

Let's look at some examples!

The following program checks if a number is even (and prints "It's even!" if so, and "It's odd!" if not).

```{code-cell} ipython3
num = 3
if num % 2 == 0: 
    print("It's even!") 
else: 
    print("It's odd!") 
```

The following program checks if a password is correct (and prints "Come in" if so, and "Go away" if not).

```{code-cell} ipython3
user_input = "hello"
password = "bunny"
# if the user input matches the password
if user_input == password:
    print("Come in")
else:
    print("Go away")
```

The following program implements a Waiter checking your age on your ID, and then shows beer/alcohol menu or says "have some water"

```{code-cell} ipython3
age = 23
drinking_age = 21
if age >= drinking_age: 
    print("Here's the alcohol menu")
else:
    print("Have some water")
```

## A closer look at Boolean expressions

All conditional blocks depend on well-crafted **Boolean Expressions**, which are [expressions](https://joelchan.github.io/inst126-intro-programming-notes/2a_Expressions.html) that evaluate to (i.e., result in, produce) a Boolean value (i.e., `True` or `False`). This is what really determines the logic of the conditional control of flow. So you need to make sure you're proficient with Booolean expressions.

### Boolean Operators
We use **Boolean** Operators to compare TWO pieces of data. When evaluated, they yield a Boolean value (`True` or `False`).

`data1 booleanOperator data2`

Here are the main ones:
- `==` equal to / the same as
- `!=` not equal to / different from
- `>` greater than
- `>=` greater than or equal to (at least)
- `<` less than
- `<=` less than or equal to (at most)

### Logical operators
We use **Logical** operators to *combine* basic Boolean expressions into more complex ones, like "is `a` more than 3 *and* less than 5"

Here are the main ones:
- `and` (True if *all* Boolean expressions are True)
- `or` (True if *any* Boolean expression is True)
- `not` (True if the Boolean expression is *not* True)

Full list of comparison and logical operators [here](https://www.w3schools.com/python/python_operators.asp)

## Practice: Construct Boolean expressions
Let's practice! Translate these Boolean expressions from English into Python.

### Basic Boolean expressions (only Boolean operator)

```{code-cell} ipython3
# is the driver's speed above the limit?
speed = 75
limit = 45
# boolean expression here
```

```{code-cell} ipython3
# do i have a passport?
has_passport = True # assign the value True to the passport variable
# boolean expression here
```

### Compound Boolean expressions (Boolean operators + Logical operators)

```{code-cell} ipython3
# have i passed all the requirements for graduation?
# which is operationalized as "do i have enough credits, with enough GPA?"
num_credits = 120 # threshold of 120
GPA = 1.5 # threshold of 2.0
# boolean expression here
```

```{code-cell} ipython3
# did i take the prereq for the class OR get permission from the instructor?
took_prereq = False
have_permission = True
# boolean expression here
```

```{code-cell} ipython3
# is the professor in the office and the door open more than a crack (at least 15 degrees) or there is a sign that says come on in or you have an appointment?
prof_in_office = True
door_angle = 5
sign_says = "Come in"
have_appointment = True
# boolean expression here
```

#### More practice: compound Boolean expressions

Try these on your own! Each one requires combining Boolean operators with logical operators (`and`, `or`, `not`).

#### 1. Can I ride the roller coaster?

You can ride the roller coaster if you are at least 48 inches tall AND at least 8 years old. Write a Boolean expression that checks both conditions.

```{code-cell} ipython3
height_inches = 50
age = 7
# boolean expression here

```

#### 2. Is the restaurant open?

The restaurant is open if the hour is between 11 and 14 (lunch) OR between 17 and 21 (dinner). Write a Boolean expression that checks if the restaurant is currently open. Assume the hour is in 24-hour time (e.g., 13 = 1pm).

```{code-cell} ipython3
hour = 13
# boolean expression here

```

#### 3. Can I get a discount?

You get a discount if you are a student OR a senior (65 or older). 

```{code-cell} ipython3
is_student = False
age = 70
# boolean expression here

```

#### 4. Should I bring an umbrella?

You should bring an umbrella if it is raining OR if the chance of rain is above 50% and you don't have a rain jacket.

```{code-cell} ipython3
is_raining = False
chance_of_rain = 75
has_rain_jacket = False
# boolean expression here

```

#### 5. Can I register for the class?

You can register for the class if you have taken the prerequisite AND (you are a junior or senior, based on credits: junior is at least 60, senior is at least 90).

```{code-cell} ipython3
took_prereq = True
credits = 55
# boolean expression here

```

#### 6. Is the flight delayed?

A flight is delayed if the wind speed is above 40 mph OR (visibility is below 3 miles AND it is not a clear day).

```{code-cell} ipython3
wind_speed = 25
visibility = 2
is_clear = False
# boolean expression here

```

## Practice: construct basic conditional blocks

Now let's practice constructing conditional blocks! Follow along with me to translate these English instructions into conditional blocks. We basically need to 1) decide what the condition is and translate it into a Boolean expression, then 2) decide what actions go in the `True` or `False` branches.

If my speed is above the limit, print stop; otherwise, let me pass.

```{code-cell} ipython3
# if my speed is above the limit, print stop; otherwise, let me pass
speed = 25
limit = 45
# conditional block below here

```

If i have a passport, print come on in; otherwise, print go away

```{code-cell} ipython3
# if i have a passport, print come on in; otherwise, print go away
# do i have a passport?
has_passport = False # assign the value True to the passport variable
# conditional block below here

```

if i have passed all the requirements for graduation, print graduate! otherwise, print need to do more

```{code-cell} ipython3
# if i have passed all the requirements for graduation, print graduate! otherwise, print need to do more
# did i accumulate at least 120 credits AND earn at least a 2.0 GPA?
# did i take the prereq for the class OR get permission from the instructor?
num_credits = 110 # threshold of 120
GPA = 1.9 # threshold of 2.0
# conditional block below here

```

#### More practice: basic if/else

Try these on your own! Each one needs a basic if/else block.

#### 1. Freezing check

If the temperature is below freezing (32 degrees F), print "It's freezing!"; otherwise, print "It's not freezing."

```{code-cell} ipython3
temp = 28
# conditional block below here

```

#### 2. Pass or fail

If the student's score is at least 60, print "Pass"; otherwise, print "Fail".

```{code-cell} ipython3
score = 55
# conditional block below here

```

#### 3. Number guessing game

If the user's guess matches the secret number, print "You got it!"; otherwise, print "Try again!"

```{code-cell} ipython3
guess = 7
secret_number = 4
# conditional block below here

```

#### 4. Shopping decision

If the item is on sale AND you have enough money (i.e., money is at least the price), print "Buy it!"; otherwise, print "Maybe next time."

```{code-cell} ipython3
on_sale = True
price = 25
money = 20
# conditional block below here

```

<!-- #### 5. File type checker

If the file name ends with ".pdf" or ".docx", print "Document file"; otherwise, print "Other file type". Hint: you can use the `.endswith()` method on strings, e.g., `"hello.pdf".endswith(".pdf")` returns `True`.

```{code-cell} ipython3
file_name = "report.pdf"
# conditional block below here

``` -->

## More complex conditional structures
The if / else conditional block is the most basic and easy to understand. But often your programs may require something a bit simpler, and sometimes a bit more complex.

+++ {"id": "oh3kS5FLBquN"}

### Conditional execution

The `else` branch is actually optional. Sometimes you just want to do something if it's true, otherwise you do nothing. 

The flow looks like this:

```{image} assets/conditional-logic-noelse.png
:class: bg-primary mb-1
:width: 600px
:align: center
```

Some examples:
- Only stop someone if they're above the speed limit
- Tell me if someone is coming!
- Look through the bag and only pull out the red skittles

Can you think of any others?

```
# generic
if booleanExpression:
    # do something
```

```{code-cell} ipython3
:id: ttMHXVzySS8m

speed = 25
limit = 30
if speed > limit:
    print("Stop!")
```

+++ {"id": "jszuKPe9CrGP"}

Keywords/phrases that signal that this is appropriate?
- if only one "choice" (or action) is described, then probably you don't need an else, since "doing nothing" is a default action

#### Practice: conditional execution (no else)

Try these on your own! Each one only needs an `if` — no `else` needed.

#### 1. Low battery warning

If the battery level is below 20, print "Low battery warning!"

```{code-cell} ipython3
battery_level = 15
# conditional block below here

```

#### 2. Dean's list

If the student is on the dean's list (GPA of 3.5 or above), print a congratulations message.

```{code-cell} ipython3
gpa = 3.8
# conditional block below here

```

#### 3. Password length check

If the password is less than 8 characters long, print "Warning: password is too short!" Hint: you can use `len()` to get the length of a string, e.g., `len("hello")` returns 5.

```{code-cell} ipython3
password = "abc"
# conditional block below here

```

#### 4. Free gift threshold

If the order total is at least $50, print "Free gift added to your order!"

```{code-cell} ipython3
order_total = 62
# conditional block below here

```

#### 5. Weekend check

If it's the weekend (Saturday or Sunday), print "No class today!"

```{code-cell} ipython3
day = "Saturday"
# conditional block below here

```

+++ {"id": "VZzGfpRdB6ca", "tags": []}

### Chained conditionals

Sometimes you have more than two *mutually exclusive* choices of paths (branches). In that case you need an elif. 

The difference from the basic conditional is something like this:

```{image} assets/conditional-logic-chained.png
:class: bg-primary mb-1
:width: 600px
:align: center
```

Some examples: 
- you have a fever if you're above 100, hypothermia if you're under 95; otherwise, you're all good! 
- choosing an outfit depending on where you want to go (in the Spring in Maryland!).
- choosing a football play depending on what you think the defense is showing.

Any other examples?

The key difference between this type of conditional block and the regular "if/else" blocks is that you need more than one Boolean expression; one for each `if` or `elif` statement.

+++

Here's the generic structure:

```
if someCondition:
    # then something
elif someOtherCondition:
    # then something else
else:
    # some default (this is technically optional
    # but if you leave it out, you may have some unexpected edge cases you didn't account for!
```

```{code-cell} ipython3
gpa = 3.5
gpa_threshold = 2.0
required_courses = 8
req_threshold = 10

if gpa >= gpa_threshold and required_courses >= req_threshold:
    print("graduate!")
elif gpa >= gpa_threshold and required_courses < req_threshold:
    print("take more required courses")
elif gpa < gpa_threshold and required_courses >= req_threshold:
    print("take an easy course!")
else:
    print("talk to an advisor")
```

```{code-cell} ipython3
:id: BaHh7pSfCCNm

# example
temp_f = 97
if temp_f >= 100:
    print("fever!")
elif temp_f < 95: # need another Boolean expression
    print("hypothermia!")
else:
    print("all good!")
```

+++ {"id": "7VgOXvQWCyJH"}

Keywords/phrases that signal that this is appropriate?

When you see more than two *mutually exclusive* **conditions** or **choices**


+++ {"id": "19fV3icBCCu0"}

Practice! Let's translate these English instructions into Python conditional blocks.

ticket pricing: if you're under 5 or 65 and up, price is zero; if you're theater staff, you get half price (7.50); otherwise pay normal price (15)

```{code-cell} ipython3
# ticket pricing: 
# if you're under 5 or 65 and up, price is zero; 
# if you're theater staff, you get half price (7.50); 
# otherwise pay normal price (15)
age = 65
theater_staff = True
# chained conditional block below here

```

help me write the grader for late assignments: if you submit before target date, you get full credit; if you submit after the target date, but before the last day of the period, you get 85% credit - if you submit on the last day of period, you get 70% credit

```{code-cell} ipython3
# help me write the updated grader for your PCEs:
# if you submit before target date, you get full credit;
# if you submit after the target date, but before or equal 1 week threshold, you get 85% credit
# if you submit after 1 week threshold, but before or equal to 2 week threshold, you get 70% credit
# otherwise, you get no credit

submission_date = 35
target_date = 36
one_week_threshold = target_date + 7
two_week_threshold = target_date + 14
score = 1

# chained conditional block below here

```

#### More practice: chained conditionals

Try these on your own! Each one needs an if/elif/else block.

#### 1. Letter grade converter

If the score is 90 or above, print "A". If 80-89, print "B". If 70-79, print "C". If 60-69, print "D". Otherwise, print "F".

```{code-cell} ipython3
score = 85
# chained conditional block below here

```

#### 2. Shipping cost calculator

If the order weighs less than 1 lb, shipping is $3. If it weighs 1-5 lbs, shipping is $7. If it weighs more than 5 lbs, shipping is $12. Print the shipping cost.

```{code-cell} ipython3
weight = 3.5
# chained conditional block below here

```

#### 3. Time of day greeting

Using 24-hour time (0 = midnight, 13 = 1pm, etc.): if the hour is less than 12, print "Good morning!" If 12-16, print "Good afternoon!" If 17-20, print "Good evening!" Otherwise, print "Good night!"

```{code-cell} ipython3
hour = 14
# chained conditional block below here

```

#### 4. Water state

If the temperature (Celsius) is 0 or below, print "Solid (ice)". If above 100, print "Gas (steam)". Otherwise, print "Liquid (water)".

```{code-cell} ipython3
temp_c = 105
# chained conditional block below here

```

#### 5. BMI category calculator

If BMI is below 18.5, print "Underweight". If 18.5 to 24.9, print "Normal weight". If 25.0 to 29.9, print "Overweight". If 30.0 or above, print "Obese".

```{code-cell} ipython3
bmi = 22.5
# chained conditional block below here

```

### Planning your conditionals with decision tables

As your conditional blocks get more complex (especially with chained conditionals), it gets harder to keep track of all the possible situations your code needs to handle. A **decision table** is a simple but powerful planning tool: you list out all the possible combinations of your conditions, and then decide what should happen in each case. Think of it as a spreadsheet for your logic.

#### Why bother?

Consider the ticket pricing example above. The English description says:
- under 5 or 65 and up → free
- theater staff → half price
- otherwise → full price

But what if someone is 3 years old *and* theater staff? Should they get free or half price? The English description doesn't tell us! A decision table forces you to confront these situations *before* you write code.

#### How to build a decision table

**Step 1:** Identify your conditions (the things you're checking). For ticket pricing, that's: (a) is the person under 5 or 65+? and (b) are they theater staff?

**Step 2:** List every combination of True/False for those conditions. With 2 conditions, you get 4 rows:

| under 5 or 65+ | theater staff | price |
|---|---|---|
| True | True | ??? |
| True | False | $0 |
| False | True | $7.50 |
| False | False | $15 |

**Step 3:** Fill in what should happen for each row. That `???` is exactly the kind of edge case that causes bugs! You need to make a decision: let's say young kids and seniors always get in free, even if they're also staff. Now the table becomes:

| under 5 or 65+ | theater staff | price |
|---|---|---|
| True | True | $0 |
| True | False | $0 |
| False | True | $7.50 |
| False | False | $15 |

**Step 4:** Now your conditional block almost writes itself. Looking at the table, you can see that the age condition should be checked *first*, since it applies regardless of staff status:

```{code-cell} ipython3
age = 3
theater_staff = True

if age < 5 or age >= 65:
    price = 0
elif theater_staff:
    price = 7.50
else:
    price = 15

print(f"Price: ${price}")
```

Notice how the order of the `if`/`elif` matters here! If we checked `theater_staff` first, we'd accidentally charge a 3-year-old staff member $7.50.

#### Practice: build a decision table

Try building a decision table for the late assignment grader exercise above. What are the conditions? How many rows do you need? Are there any edge cases where it's not obvious what should happen?

+++ {"id": "_1BiX-ZSCO_O", "tags": []}

### Nested conditionals

Sometimes it only makes sense to check a condition if earlier conditions are true/false. This is like a garden of forking paths or choose your own adventure. Sometimes this to save time/operations. Other times, it may make your program more readable.

I like to think of it like a choose your own adventure maze:

```{image} assets/conditional-logic-nested-cyoa.png
:class: bg-primary mb-1
:width: 600px
:align: center
```

Simple example: I want to know if x is the same, less than, or greater than y. We can represent this as a chained conditional with three conditions. But we can also group the less than or greater than conditional block by itself since that only make sense in the situation where x and y are *not* the same (i.e., `x != y`).

```{code-cell} ipython3
x = 5
y = 10

if x == y:
    print("x and y are equal")
else:
    if x < y:
        print("x is less than y")
    else:
        print("x is greater than y")
```

Another simple example: graduation requirements: if you've completed the base requirements and you have a 3.0 average, then we check: do you have sufficient electives? if yes, then great! if not, take more electives. if you don't have the core requirements done, then you need to take care of that first, we'll worry about electives later.

```{code-cell} ipython3
:id: zQ5U8v4dGHI0

n_credits = 125
credit_threshold = 120
GPA = 3.5
n_electives = 3
electives_threshold = 4

if n_credits >= credit_threshold and GPA >= 3.0:
    if n_electives >= electives_threshold:
        print("Ready to graduate!")
    else:
        print("Get more electives!")
else:
    print("Finish core requirements with sufficient GPA!")
```

+++ {"id": "za2LAdfFDHww"}

Keywords/phrases that signal that this is appropriate? Something about having more than two choices, but some choices only make sense if some earlier condition is met. In other words, we have more of multiple forks, rather than a single fork.

+++ {"id": "Nyxk2KfLIDXz"}

Practice! Let's translate these English instructions into Python conditional blocks.

Polling booth: if you don't have an id, go away and register, then come back; if you have an id come on in! then, if you need assistance, go to the assisted booth; otherwise, go to the normal booth.

```{code-cell} ipython3
:id: KCe_GVMMICZh

# polling booth: if your registration doesn't match this location, go away to the right place; if yes, then come on in! 
# then, if you need assistance, go to the assisted booth; otherwise, go to the normal booth.
registration_here = True
need_assistance = False

# nested conditional block below here

```

#### More practice: nested conditionals

Try these on your own! Each one involves a condition that only makes sense to check after an earlier condition.

#### 1. Online store checkout

If the user is logged in, check if they have items in their cart: if yes, print "Proceeding to checkout"; if no, print "Your cart is empty". If the user is not logged in, print "Please log in first".

```{code-cell} ipython3
logged_in = True
items_in_cart = 0
# nested conditional block below here

```

#### 2. Amusement park ride

If the rider is tall enough (at least 48 inches), then check their age: if they are under 12, print "You need an adult with you"; otherwise, print "Enjoy the ride!" If they are not tall enough, print "Sorry, you're too short for this ride".

```{code-cell} ipython3
height = 50
age = 10
# nested conditional block below here

```

#### 3. Job application screener

If the applicant has a degree, check their years of experience: if 3 or more years, print "Schedule an interview"; otherwise, print "Consider for junior position". If they don't have a degree, check their years of experience: if 5 or more years, print "Schedule an interview"; otherwise, print "Does not meet requirements".

```{code-cell} ipython3
has_degree = False
years_experience = 6
# nested conditional block below here

```

#### 4. Restaurant order

If the restaurant is open, check if the item is on the menu. If yes, check if the item is in stock: if yes, print "Order placed!"; if no, print "Sorry, that item is sold out". If the item is not on the menu, print "We don't serve that here". If the restaurant is closed, print "Sorry, we're closed".

```{code-cell} ipython3
is_open = True
on_menu = True
in_stock = False
# nested conditional block below here

```

#### 5. Email filter

If the email is from a known contact, print "Inbox". If the email is not from a known contact: if it contains the word "unsubscribe", print "Promotions"; otherwise, print "Unknown - review manually".

```{code-cell} ipython3
from_known_contact = False
contains_unsubscribe = True
# nested conditional block below here

```

Some people may say that sometimes this sort of code isn't great practice, because it can be hard to understand and debug. I'm not sure I completely agree. I think it depends on the structure of your problem. I like to write nested conditionals when the underlying logic is really like a garden of forking paths or choose your own adventure game.

+++

## Common errors

### Syntax and indentation errors
e.g., forgetting the colon, or forgetting to indent

Best recommendation is to use templates for now as you set them up.

### Boolean expression errors
Most commonly, using `=` (this is assigning!) instead of `==` (the Boolean operator you actually want)! 

### Semantic errors
Not covering all your bases or mapping the wrong conditions to outcomes. These are the trickiest because your code runs without errors, but it does the wrong thing!

Common examples:
- Checking conditions in the wrong order (e.g., a more general condition "catches" cases before a more specific one gets a chance)
- Forgetting an edge case (e.g., what if two conditions are both true at the same time?)
- Using `and` when you mean `or`, or vice versa

The best defense against semantic errors is to **build a decision table** before you write your conditional block (see the [decision tables section above](#planning-your-conditionals-with-decision-tables)). Listing out every combination of conditions and deciding what should happen in each case helps you spot gaps and conflicts in your logic before they become bugs.

Example decision table for Project 1: https://docs.google.com/spreadsheets/d/1-q5XXbMDoji8AMVWxgUf5GW5CUOJfiWQTTV6u0-DwF8/edit?usp=sharing

You can also use decision tables to **debug** existing code: build the table from your code by tracing through each row, and compare it to what you *intended*. If they don't match, you've found your bug.

### Using separate `if` blocks instead of `elif`

A very common mistake is writing multiple separate `if` statements when you actually need a chained conditional (`if`/`elif`/`else`). These look similar but behave very differently!

Consider this example: assign a letter grade based on a score.

**Wrong (separate `if` blocks):**

```{code-cell} ipython3
score = 85

if score >= 90:
    grade = "A"
if score >= 80:
    grade = "B"
if score >= 70:
    grade = "C"
if score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)
```

This prints `"D"`! Why? Because each `if` is a **separate** conditional block — they all run independently. So even though `score >= 90` is `False`, the program keeps going and checks every other `if`. When it gets to `score >= 80`, that's `True`, so `grade` becomes `"B"`. But then it *keeps checking*: `score >= 70` is also `True`, so `grade` gets overwritten to `"C"`. Then `score >= 60` is also `True`, so `grade` gets overwritten again to `"D"`.

**Right (chained conditional with `elif`):**

```{code-cell} ipython3
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)
```

This correctly prints `"B"`. With `elif`, once a condition is `True` and its branch runs, the rest of the chain is **skipped**. That's the whole point of chaining: the conditions are *mutually exclusive* — only one branch ever executes.

**The rule of thumb:** if your conditions are meant to be mutually exclusive (only one should "win"), use `elif` to chain them together. Use separate `if` blocks only when the conditions are truly independent and you want *each one* checked regardless of the others.
