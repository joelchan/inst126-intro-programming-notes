---
jupytext:
  formats: md:myst
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

# Debugging and Help-Seeking

<!-- ## What are bugs and debugging and why should we care about them? -->

Fun fact: in computing, there is [lore](https://en.wikipedia.org/wiki/Software_bug) that says the term "bug" can be traced to Grace Hopper finding a moth in the computer that caused a system error!

```{image} assets/First_Computer_Bug,_1945.jpg
:class: bg-primary mb-1
:width: 800px
:align: center
```

Bugs are basically problems in our code that make the program **do something different than what we want**.

Bugs are a fact of life. We all make mistakes. Basically nobody writes perfect code the first time for any real problem. One estimate is that professional programmers spend about 35-50 percent of their time validating and debugging software.

So debugging is actually a fundamental computational thinking skill.

## Types of errors: syntax, runtime, and semantic/logic errors

It's useful to think about three kinds of problems or errors in our code:

1. **Syntax errors**: Python can't even *read* your code — it doesn't follow the rules of the language, so Python refuses to run it at all. Examples: forgetting a colon, mismatched parentheses, using `=` when you meant `==`. These produce a `SyntaxError` or `IndentationError` *before* your program even starts running. These kinds of errors are common when you're first learning to program, but with practice (and linters and IDEs!) will be a very small part of what you need to debug.

2. **Runtime errors**: Your code is syntactically valid — Python can read it — but it crashes *during* execution when it tries to do something that doesn't work. Examples: using a variable that doesn't exist (`NameError`), trying to add a string and a number (`TypeError`), or accessing an index that's out of range (`IndexError`). These errors mean Python understood your instructions, but the instructions asked it to do something impossible. 

3. **Semantic (logic) errors**: Your code runs without crashing, but it produces the **wrong result**. These are the trickiest because Python gives you *no error message* — as far as Python is concerned, everything went fine. The problem is that what you told the computer to do isn't what you actually *wanted* it to do. These kinds of errors account for basically all of debugging in real-world programming. 

## How NOT to debug

The biggest mistake I see beginners make: keep changing things to make errors go away. 

Example conversation:
Q: "Why did you do that?" 
A: "No idea... I just wanted to tinker to see if it works

Why is this not productive/effective?

Randomly changing your code so that it "runs" or the error goes away may --- in the case of semantic/logic errors -- not actually fix the problem! 

Also there are often more than one error in your code. We want to keep track of what's happening and under what conditions so our "fixes" don't create new problems (this happens more often than you’d think!)!

So trial and error eventually stops working when you’re attacking problems of realistic scale (e.g., towards the end of this class, or in INST 326).

In fact, it may have already stopped working for you!

## How to debug: Learn to read error messages

For syntax errors and runtime errors, Python gives you an error message. These are actually really useful — they're Python's way of telling you *what* went wrong and roughly *where*. Let's review how to read them!

```{image} assets/annotated-error-msg-generic.png
:alt: typeError
:class: bg-primary mb-1
:width: 800px
:align: center
```

**Error code and message**: tells you the *type* of problem, which points you toward common fixes. It also reveals mismatches between your assumptions and what's actually happening:
- `SyntaxError` / `IndentationError`: Python couldn't even read your code — something about the structure is wrong
- `NameError`: you're using a variable that doesn't exist (maybe a typo, or you forgot to define it)
- `TypeError`: you're trying to do something with the wrong type of data (e.g., adding a string and a number)
- `IndexError`: you're trying to access a position in a list that doesn't exist

**Traceback**: roughly where in the program Python noticed that there was a problem.
- NOTE! This is not necessarily where the problem *is*! Often the root cause (and fix) is located upstream
- But it is still a useful place to start looking

## How to debug: Model your intent and the code, and make sure the two models are aligned!

```{admonition} Tip
The fundamental art of debugging semantic/logic errors: make a clear model of your *intent* and a model of your *code*, note where they don't align, and systematically changing things so that they do align.
```

Error messages only show up for syntax errors and runtime errors. For semantic (logic) errors — where your code runs fine but produces the wrong result — Python won't give you an error message. So you can't know if you've fixed the bug by making an error message go away!

The fundamental art of debugging these kinds of errors is 1) interrogating and refining a model of your **intent** (what do i actually want the program to do?), 2) making a model of what your **code** is *actually* doing, 3) noticing where your model of your intent and your code don't align, and 4) changing things systematically so that the two models do align.

This is because the root cause of these errors is a mismatch between what you want to happen, and what you're telling the computer to make happen (which is what will actually happen when the code runs without syntax and runtime errors).

This is why **debugging is tightly related to problem formulation** — the better and more explicit your model of what the program should do, the better you'll be able to pinpoint where your code is not in alignment with your model, and set you up to systematically change things so that it is aligned. 

<!-- ## Practical Strategies and Principles for Debugging -->

Here are some practical strategies and principles for doing this:

### Explicitly articulate your model of your intent

Be explicit about your model of your intent: what do you want your code to do?

This is the job of our problem formulation!

And our [help-seeking template](../Help-Seeking-Template.md)

This is also probably what you believe you told your code to do! But it may not be what you actually told your code to do. Systematically comparing your intent against your code is, again, the key art of debugging, and is not possible if you don't have a clear model of your intent!

### Compare actual output against your specifications

The most common thing I hear when students ask for help with buggy code is, *"It's not working"*. 

A massive bang-for-your-buck habit change is to shift from "it's not working", to *"I expected x, and i got y"*. This requires something more specific than "i expected it to work, and it didn't!"

If you have a clear problem formulation, you have powerful ingredients to do this systematically, because you can now look carefully at what your program actually produces, and compare it against what you expected from your specifications!

So, whenever you see an error or wrong answer, resist the urge to immediately start trying to change the code to make errors or wrong answers go away. Instead, slow down and ask:

1. **What did I expect to happen?** (This is your specification — the input/output examples from your problem formulation)
2. **What actually happened?** (Run the program and look carefully at the output)
3. **Where exactly is the mismatch?** (Is the output completely wrong? Partially right? Right for some inputs but wrong for others?)

The mismatch tells you *what kind* of bug you have, which tells you *where* to look.

For example, imagine you wrote a function to check if someone qualifies for a discount (students or seniors 65+). You have these specification examples:

| Input | Expected Output |
|---|---|
| `is_student=True, age=20` | `"Discount applied"` |
| `is_student=False, age=70` | `"Discount applied"` |
| `is_student=False, age=30` | `"No discount"` |
| `is_student=True, age=70` | `"Discount applied"` |

If your program prints `"No discount"` for *every* input, that's a different kind of bug than if it works for students but fails for seniors. The first suggests your condition is fundamentally broken (maybe always evaluating to `False`); the second suggests a more specific problem with how you're checking age.

This example illustrates how **specification examples can be a very powerful debugging tool**: Run your program with each example input, write down what you actually get, and find the pattern in what's wrong. That pattern points you toward potential root causes of your bug, or at least where you might need to check the code to make sure it's actually aligned with what you want to happen (your intent), or what you think is true (your assumptions about data, etc.). If your specification examples are thorough, you can then also systematically run your modified code against these example test cases to verify that your program is fixed!

I like to actually "preserve the crime scene" and note down the mismatches in the test cases, with screenshots, or notes - e.g., "ran x with inputs a, b, c; expected y, but got z instead" and actually save the program x so you can look at it carefully and return to it!

Test cases in your specification also enable a more powerful strategy of automated testing, including “[unit testing](https://softwaretestingfundamentals.com/unit-testing/)" in professional practice, and is a cornerstone of effective programming. Rather than manually changing inputs and checking outputs for each possible test case, you can write a program that runs these test cases (again, often this will be for substeps of your program) all at once and give you back a single "crime scene" report you can look at and use to try to identify causes of your error. Our PCE tests are a small example of this that hopefully you have been using to help debug your code!

<!-- ### Systematic testing

This a bit mo

Notice how we ask you to test your function in multiple ways? And our PCE scoring functions actually contain multiple test cases?

This is a core strategy that helps you to check your assumptions. -->
	    
### Document your code

It can also be helpful to write comments for each line in your code: what is it actually doing? Is that the same as what it should be doing? Is anything missing?

It's important that when you're documenting line by line for debugging purposes, you carefully write out what you think the code is *actually* doing, and separate it out from what you want it to do.

It's quite often that simply doing this helps me notice where I wrote valid code that runs but does not do what I want to do (or I may even wonder "wait, why di did i ask Python to do that??"), and identifying precisely how it's different from my intent suggests a bugfix.

<!-- Comments that simply restate the code (essentially) are not very useful. You should force yourself to think through what line of code is “actually” doing and whether it matches with what you want it to do. -->

### X-Ray your program!

To build a model of your code (i.e., what you actually told Python to do), you need to "see what is happening" when your code is executing.

The simplest way to do this is well-placed print statements (aka print debugging)! Print statements can help you trace things like:
- If it's a loop, am I seeing multiple runs?
- If I expect this data to be a string, can I verify that?
- If I expect my data to be changing, can I see that?

Print statements can seem simple and can also clutter your code, but is a powerful place to start. 

There are also tools:
- [Python Tutor](https://pythontutor.com/visualize.html#mode=edit), which allows you to step through your code and see what is happening at each step
- Debuggers in IDEs like VSCode: https://code.visualstudio.com/docs/python/debugging
- And in professional practice we often use logging tools (e.g., Python's [logging module](https://realpython.com/python-logging/)) to keep rich traces we can pore over to figure out what our code is actually doing when it runs.

### Explicitly check your assumptions about data

A sneaky source of bugs is when your data isn't what you *think* it is. The value might *look* right when you print it, but be the wrong type, or have unexpected properties. For example, `"5"` (a string) and `5` (an integer) look the same when you print them, but behave very differently in your code! Same with `"True"` (string) and `True` (boolean)!

So when you're x-raying your program with print statements, it can be helpful to go beyond just printing the value — also check its type and other properties:

```python
# Instead of just:
print(x)

# Also check:
print(type(x))     # Is it the type I expect?
print(len(my_list)) # Does it have as many items as I expect?
```

This habit of checking what your data *actually is* (not just what it looks like) connects to a broader idea in professional programming: being explicit about what your code *expects* to receive and produce. If you've written a specification with input/output examples, you already know what you expect — these checks help you verify that your expectations hold at each step of the program. 

In professional practice, these specific assumption checks are often done with [`assert` statements](https://code.visualstudio.com/docs/python/debugging) that can simulate the syntax/runtime error messages, in that they can stop your program with an error message if the assertion about a particular fact about your code/data is false.

## Other debugging tips

### Isolate the problem

When something is wrong and you're not sure where the bug is, **strip your code down to the smallest version that still shows the bug**. Remove parts that seem unrelated. If you have a complex Boolean expression, test each piece separately. If you have a long program with multiple steps, comment out everything except the part you're investigating and check if it works on its own.

This is powerful because it shrinks the "search space" for your bug. Instead of staring at 30 lines of code trying to figure out what's wrong, you narrow it down to 5 lines and the bug becomes much easier to spot. 

For example, if your program reads data, processes it, and then prints a result, and the result is wrong — is the data being read correctly? Add a print statement right after you read it and check. If the data looks right, the problem is downstream. If the data looks wrong, the problem is upstream. You just cut your search space in half!

You can also more easily devise a specification or set of tests for that smaller chunk of code, to help verify if your fix worked.

### Change one thing at a time

Once you've identified a suspect line or section, **only change one thing, then re-run and check**. If you change three things at once and the bug goes away, you don't know which change actually fixed it — and you may have introduced a *new* bug without realizing it.

This directly counters the "tinkering" anti-pattern: instead of frantically trying things, you're making careful, deliberate changes and observing the effect of each one. Think of it like a scientist running an experiment — you only change one variable at a time so you can draw clear conclusions.

###  Learn how to ask for help!

Last but not least, often it helps just to talk to someone or something out loud as you think through and work through the problem! Professional programmers call this "rubber duck debugging", a legendary method in software engineering practice: [https://rubberduckdebugging.com/](https://rubberduckdebugging.com/)

But there is actually a lot of commonality and inter-relatedness between debugging and help-seeking. So help-seeking strategies deserve their own discussion! Here is a short article with a step-by-step procedure that can really help you and help others help you efficiently and effectively: https://docs.google.com/document/d/1PXkXKko906a6zivJYvZQ8dMsLqFZ9RZbc5Aa4C-wWiw/edit?usp=sharing

That’s a lot of content! But this is quite effective and well worth practicing. 

## Practice!

<!-- Here: [debugging example practice](../Practice_Debugging_examples.ipynb) -->

To help you practice, your rubric for the final project deliverable for Project 3 will include the requirement that you include bug documentation, based on these help-seeking guidelines. But I recommend you start practicing this now, so I am offering an extra credit assignment to get started early with a debugging report

### Some buggy programs to practice debugging

For each program below, you're given a description of what the program is *supposed* to do, followed by buggy code. Your job:

1. **Write a specification** — before you even look closely at the code, write an input/output table with at least 3 examples (including an edge case) based on the description
2. **Run the code** with your example inputs — what does it *actually* produce?
3. **Compare** — where exactly is the mismatch between your specification and the actual output?
4. **Find and fix the bug**, using one or more of the strategies above (e.g., document the code line by line to check for mismatches between your intent and what the code is actually telling python to do, plug the code into python tutor to x-ray what is actually happening)

#### 1. Tip calculator

**Goal:** A function that takes a meal price and a tip rate, and returns the total (meal + tip).

```{code-cell} ipython3
def calculate_total(meal_price, tip_rate):
    tip = meal_price * tip_rate
    total = meal_price + tip_rate
    return total

print(calculate_total(50, 0.20))
print(calculate_total(100, 0.20))
```


```{admonition} Specification and bug description
:class: toggle
| Meal price | Tip rate | Expected return value |
|---|---|---|
| 50 | 0.20 | 60.0 |
| 100 | 0.20 | 120.0 |
| 25 | 0.20 | 30.0 |

<!-- BUG: Returns 50.2 for calculate_total(50, 0.20) instead of 60.0. Line `total = meal_price + tip_rate` adds the rate (0.20) instead of the tip amount. Should be `total = meal_price + tip`. Wrong variable used in expression. -->
```

#### 2. Temperature converter

**Goal:** A function that takes a temperature in Celsius and returns the temperature converted to Fahrenheit using the formula: F = C * 9/5 + 32.

```{code-cell} ipython3
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return celsius

print(celsius_to_fahrenheit(37))
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
```


```{admonition} Specification and bug description
:class: toggle
| Celsius | Expected return value |
|---|---|
| 0 | 32.0 |
| 100 | 212.0 |
| 37 | 98.6 |

<!-- BUG: Returns 37 for celsius_to_fahrenheit(37) instead of 98.6. The function computes the conversion correctly into `fahrenheit`, but then returns `celsius` instead of `fahrenheit`. The wrong variable is returned. Should be `return fahrenheit`. -->
```

#### 3. Full name builder

**Goal:** A function that takes a first name and last name and returns the full name with a space between them.

```{code-cell} ipython3
def make_full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    print(full_name)

result = make_full_name("Joel", "Chan")
print("The full name is:", result)
```


```{admonition} Specification and bug description
:class: toggle
| first_name | last_name | Expected return value |
|---|---|---|
| "Joel" | "Chan" | "Joel Chan" |
| "Grace" | "Hopper" | "Grace Hopper" |

<!-- BUG: Prints "Joel Chan" then "The full name is: None". The function uses `print()` instead of `return`. So `result` is `None`. The function should use `return full_name` instead of `print(full_name)`. -->
```

#### 4. Shipping cost calculator

**Goal:** A function that takes a weight (in lbs) and returns the shipping cost. Under 1 lb: $3. Between 1-5 lbs: $7. Over 5 lbs: $12.

```{code-cell} ipython3
def shipping_cost(weight):
    if weight < 1:
        shipping = 3
    if weight <= 5:
        shipping = 7
    else:
        shipping = 12
    return shipping

print(shipping_cost(0.25))
print(shipping_cost(3.0))
print(shipping_cost(10.0))
```

```{admonition} Specification and bug description
:class: toggle
| weight | Expected return value |
|---|---|
| 0.25 | 3 |
| 3.0 | 7 |
| 10.0 | 12 |
| 1.0 | 7 |

<!-- BUG: Returns 7 for shipping_cost(0.25), should be 3. Uses separate `if` blocks instead of `elif`. The second `if weight <= 5` is independent of the first, so even when weight < 1 (matching the first block), the second block also runs and overwrites `shipping` to 7. The second `if` should be `elif`. -->
```

#### 5. Grade message

**Goal:** A function that takes a score and returns an appropriate message. 90+: "Excellent!", 80-89: "Good job!", 70-79: "Not bad.", below 70: "Keep trying."

```{code-cell} ipython3
def grade_message(score):
    if score >= 70:
        return "Not bad."
    elif score >= 80:
        return "Good job!"
    elif score >= 90:
        return "Excellent!"
    else:
        return "Keep trying."

print(grade_message(95))
print(grade_message(85))
print(grade_message(75))
print(grade_message(60))
```

```{admonition} Specification and bug description
:class: toggle
| score | Expected return value |
|---|---|
| 95 | "Excellent!" |
| 85 | "Good job!" |
| 75 | "Not bad." |
| 60 | "Keep trying." |

<!-- BUG: Prints "Not bad." for score=95 and score=85, when they should be "Excellent!" and "Good job!". Conditions are checked in the wrong order — most general first. `score >= 70` is True for scores of 85 and 95, so it catches them before the more specific conditions get a chance. The `elif >= 80` and `elif >= 90` branches are unreachable. Fix: check from most specific (highest) to least specific: `>= 90` first, then `>= 80`, then `>= 70`. -->
```

#### 6. Password strength checker

**Goal:** A function that takes a password and returns a message about its strength. A password is strong if it is at least 8 characters long AND contains a digit. If it's long enough but has no digit, return "Needs a digit". If it's too short, return "Too short".

```{code-cell} ipython3
def has_digit(text):
    for char in text:
        if char.isdigit():
            return True
    return False

def check_password(password):
    if len(password) >= 8:
        return "Strong password!"
    elif has_digit(password):
        return "Needs a digit"
    else:
        return "Too short"

print(check_password("abcdefgh"))
print(check_password("abcdefg1"))
print(check_password("abc"))
print(check_password("ab1"))
```

```{admonition} Specification and bug description
:class: toggle
| password | Expected return value |
|---|---|
| "abc" | "Too short" |
| "abcdefgh" | "Needs a digit" |
| "abcdefg1" | "Strong password!" |
| "ab1" | "Too short" |

<!-- BUG: Returns "Strong password!" for "abcdefgh", but it should return "Needs a digit" (long enough but no digit). Uses chained elif when the logic requires nesting (dependent/sequential checks). The code says: if long enough → "Strong!" — but never checks for a digit. Fix: nest the digit check inside the length check: `if len >= 8: if has_digit: "Strong!" else: "Needs a digit"`. -->
```

#### 7. Discount calculator

**Goal:** A function that applies a discount to a price. Members get 20% off. If the item is on clearance, everyone gets 50% off (members included — clearance overrides the member discount). Non-members with no clearance pay full price.

```{code-cell} ipython3
def apply_discount(price, is_member, on_clearance):
    if is_member:
        price = price * 0.80
    elif on_clearance:
        price = price * 0.50
    return price

print(apply_discount(100, True, True))
```

```{admonition} Specification and bug description
:class: toggle
| price | is_member | on_clearance | Expected return value |
|---|---|---|---|
| 100 | True | False | 80.0 |
| 100 | False | False | 100 |
| 100 | True | True | 50.0 |
| 100 | False | True | 50.0 |

<!-- BUG: Prints 80.0 for apply_discount(100, True, True), but should be 50.0. Clearance should override membership, but `elif` means clearance is never checked when `is_member` is True. Fix: check `on_clearance` first (since it overrides), or use nested conditionals: `if on_clearance: price * 0.50; elif is_member: price * 0.80`. -->
```

---
## Recommended resources:

[The Debugging Mindset - ACM Queue](https://queue.acm.org/detail.cfm?id=3068754) (excellent overview of the core concept of mental model mismatches being the root cause of bugs)

[How to debug small programs](https://ericlippert.com/2014/03/05/how-to-debug-small-programs/) (has some good overall ideas, plus pointers to more advanced techniques like assertions and unit testing)

[A debugging manifesto](https://jvns.ca/blog/2022/12/08/a-debugging-manifesto/) (expands a lot more on the strategies we discussed today, including into a wonderful [zine](https://jvns.ca/blog/2022/12/21/new-zine--the-pocket-guide-to-debugging/); also a great person to follow on [Twitter](https://twitter.com/b0rk)/[Mastodon](https://social.jvns.ca/@b0rk) for learning how to program.)

```{image} assets/julia-evans-debugging-manifesto.png
:class: bg-primary mb-1
:width: 800px
:align: center
```