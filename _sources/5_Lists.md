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

# 5: Lists

+++

## Learning goals
- Create a list in Python
- Do common operations on lists (e.g., appending, indexing, slicing, sorting)
- Explain difference between mutable and immutable data structures
- Recognize potential application opportunities for collection methods and functions (e.g., len, max, min)
- Explain difference between functions and methods
- Appropriately apply collection methods and functions to lists

+++ {"id": "g-lkfdphxbR0"}

## What are lists and why should we care about them?

+++ {"id": "X8Q343PRGhMR"}

### A list is a kind of collection data structure

So far we’ve mostly used a “non-collection” data structures. Most of our variables have one value in them - when we put a new value in the variable, the old value is overwritten

A list is a kind of **collection** data structure. A collection allows us to put many values into a single "variable"

A collection is nice because we can carry many values around in one convenient package

```{code-cell} ipython3
:id: cTjXSIqNGs85

friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'shirt', 'perfume']
scores = [1, 50, 32]
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 34
executionInfo:
  elapsed: 368
  status: ok
  timestamp: 1601909194385
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 240
id: 7QPrKhoiOlvV
outputId: 89bce3f9-bf52-45f2-a864-3ff480b44ff6
---
carryon
```

+++ {"id": "rt-d9q-YGx3F"}

### Why do we need more data structures than strings, numbers and Boolean values?

Recall that computational thinking is a key component of programming skill. **Algorithms** --- sets of rules or steps used to solve a problem --- are an important way to model and instruct computers to solve problems. In computer science, it is well known that some algorithms need special **data structures** --- particular ways of organizing data in a computer.

Consider this problem: Find the smallest number amongst a set of N numbers.

Can you think of a structured set of rules (algorithms) for solving this problem in a reusable way *without* using a collection / list?

```{code-cell} ipython3
:id: 1EjL-gGYPA6k

# find the smallest number amongst five numbers
a = 1
b = 5
c = 7
d = 10
e = 2  
```

```{code-cell} ipython3
# what if we have six numbers?
```

```{code-cell} ipython3
# or just 3?
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 313
  status: ok
  timestamp: 1614608840766
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: ojgv4-M_PYY9
outputId: 7ccffee1-0191-4553-e648-cdd808e6d15a
---
# with lists
```

+++ {"id": "XMfeWgyvG3W7"}

Could in principle do these with separate variables for each item. But very clunky! And error prone! And basically impossible to generalize (contra core goal of developing **abstractions over classes of problems**, from CompT).

The point to note here is that your ability to model (and therefore solve) problems with programming is dependent on your knowledge of data structures (since they constrain the set of algorithms you can recognize and apply to problems). So as you expand your knowledge of data structures, try to note down also the common situations in which they apply, and what algorithms they tend to "work well with".

You will learn a few more data structures this semester (dive more into strings this module, then files and dictionaries next module, and dataframes for data analysis in the final module). And of course many more as you advance in your career.

+++

Lists in context of our example problem from last week:

```{code-cell} ipython3
# key variables:
# the input LIST of strings
inputs = [
    "hello sarah@umd.edu",
    "from: joelchan@umd.edu",
    "some other text that doesn't have an email"
]
# a LIST to store the email addresses
emails = []

# Loop over every text input
for text_input in inputs:
    
    # extract an email address
    # split the text into subsets
    chunks = text_input.split()
    
    # check every chunk
    for chunk in chunks:
        # check if it has @ and .
        if "@" in chunk and "." in chunk:
            # put the chunk in the email list
            emails.append(chunk)
# give the email address back to the user
print(emails)
```

How would you solve this without lists? Or some kind of collection?

+++ {"id": "ifBcaTKuA2jN"}

## Anatomy of a list in Python

List constants or "literals":
1. Are surrounded by square brackets
2. Contain at least one element in the list; multiple items are separated by commas.

```{code-cell} ipython3
:id: JG-iNe0ZHJVn

"1, 2, 3" # string
1 # int
1.0 # float

basic_list = [1, 2, 3] # list
another_list = [11,32,53] # the spaces don't matter for Python, only the commas; spaces are for readability for us

# can also show up like this if you want to see the contents more explicitly
# python knows where the list starts or stops based on the brackets
basic_list_2 = [
    1,
    2,
    3
]

# handy for large items in a list
sentences = [
    "something",
    "she sells sea shells by the sea here",
    "she sells sea shells by the sea there",
]
#sentences = ["she sells sea shells by the sea shore", "she sells sea shells by the sea here", "she sells sea shells by the sea there"]
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 461
  status: ok
  timestamp: 1614609615503
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: NCGZJbFoOfES
outputId: 5f2c0a1e-c30b-4e2d-9185-335f8ed35abd
---
sentences
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 34
executionInfo:
  elapsed: 479
  status: ok
  timestamp: 1601909922316
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 240
id: ly58xGlvRYH3
outputId: b1f1b382-935c-4c83-8c4a-55faa56484ae
---
basic_list
```

You can assign lists to variables, just like other values, with a variable assignment statement.

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 586
  status: ok
  timestamp: 1614609731424
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: RuCD-LNiRaJU
outputId: af9e62a4-2c36-4c19-b31e-105f04470f26
---
a = [1, 2, 3]
b = [1, "2", 3.0]
c = [a, b] # list of lists
print(a)
print(b)
print(c)
```

```{code-cell} ipython3
:id: UEMh-KDiPqm3

a = [
  1, # position 0 
  2, # position 1
  3  # position 2
]
```

+++ {"id": "0EsxtmnxHQNC"}

## Some properties of lists

Some properties of lists:
- Can hold **more than one value**
    - What can go in a list?
        - Any Python object: even another list!
        - Mixed objects: doesn't all have to be the same type of object
    - But you can also have lists with just one item, or no items! Rarely will this be useful (except to initialize the variable).
- Is **indexed** positionally, and therefore has a notion of position / order
    - Some other data structures, like dictionaries, don't have this property
        - This allows you to do things like sort, find by position (e.g., "first" or "last")
    - NOTE: the index starts at 0, not 1! So the first item is at index / position 0, the second at index / position 1, and so on...
        - Very important to remember this as you work with getting things in and out of lists
- Is **mutable**: you can change the data held by the variable directly. Some other data structures (like strings!) are immutable - you can never directly modify the value held by the variable, you can only create a new modified value that you must then assign to the same or different variable to keep around. Hold this thought to compare/contrast when we discuss strings in a couple weeks.

+++ {"id": "TlIgLzthHfcr"}

Let's demonstrate these properties by "dissecting" a few lists together.

+++

### Can hold multiple types of data, including other lists

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 52
executionInfo:
  elapsed: 501
  status: ok
  timestamp: 1601910267131
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 240
id: s_4Oo2sWRwNh
outputId: 2351b06d-2f2d-46cd-8997-43e2cc0829aa
---
basic_list = [1, 2, 3] # list
x = [1, "1", basic_list] # mixed
y = [basic_list, basic_list, basic_list] # list of lists
empty_list = [] # empty list, often used for initialization
list_w_one = [1]
print(x)
print(y)
```

```{code-cell} ipython3
y
```

### Indexing

REMEMBER: indexing starts at 0

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 344
  status: ok
  timestamp: 1614610102228
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: vnfv4Qw_Sp_X
outputId: 7ec010d7-ba3b-4390-84cd-de65f79605b6
---
basic_list_3 = [
  "red", # psn 0
  "green", # psn 1
  "blue", # psn 2
  "yellow", # psn 3
  "white", # psn 4
    "black", # psn 5
]
print(basic_list_3[1]) # actualyl gets you the 2nd item, at position 1
print(basic_list_3[0]) # actualyl gets you the 1st item, at position 0

# get the 5th item
basic_list_3[2]
```

Here it is in pictures.

<!-- <img src="https://railsware.com/blog/wp-content/uploads/2018/10/positive-indexes.png" height=500 width=700></img> -->

```{image} assets/positive-indexes.png
:alt: typeError
:class: bg-primary mb-1
:width: 800px
:align: center
```

+++

You can also index in reverse! Handy for getting the last item in a list.

<!-- <img src="https://railsware.com/blog/wp-content/uploads/2018/10/negative-indexes.png" height=500 width=700></img> -->

```{image} assets/negative-indexes.png
:alt: typeError
:class: bg-primary mb-1
:width: 800px
:align: center
```

+++

Yes, the alert reader will notice that this reverse indexing starts at... 1. So why does the indexing start at 0? I'm afraid I don't have a good answer. [Maybe it came from the design of the C programming language](https://albertkoz.com/why-does-array-start-with-index-0-65ffc07cbce8), and most languages (but not all!! R starts indexing at 1), followed suit.

```{code-cell} ipython3
print(basic_list_3[-1]) # gets you the last item, at position -1
print(basic_list_3[-2]) # gets you the 2nd last item, at position -2
```

### Mutating (changing) list values directly

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 34
executionInfo:
  elapsed: 409
  status: ok
  timestamp: 1601910603890
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 240
id: dyoXYqimT6Zl
outputId: ced1570f-c180-4e4a-85c1-2170cdca7fa4
---
basic_list_4 = [4, 6, 7, 10, 5]
print(basic_list_4)
basic_list_4[1] = 7 # can mutate the list (i.e., modify it directly)
print(basic_list_4)
```

```{code-cell} ipython3
:id: xAVCZEzERIPk

def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

list_of_functions = [multiply, add]
```

+++ {"id": "FYVv4YjdCjfS"}

## Working with lists

+++ {"id": "TP00ttDLHmte"}

### Make a list
Can use the assignment statement to initialize to an empty list, or manually specify what's in a list

```{code-cell} ipython3
:id: AzsUWV0-Hz6N

x = [1, 2, 3] # list with numbers 1 2 and 3
y = [] # empty list
z = [4, 7]
```

```{code-cell} ipython3
# DO NOT DO THIS
x[:2] = 5, 7
x
```

+++ {"id": "Q2HZItzZH0kv"}

Can create from existing lists, using **concatenation** (adding two existing lists together)

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 551
  status: ok
  timestamp: 1614610341416
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: E5-DLDoGH6Fz
outputId: f9cf389a-d0f5-4ca6-a860-d752f684180f
---
new_list = x + z
new_list
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 327
  status: ok
  timestamp: 1614610372758
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: An_uYNG4RtMo
outputId: d6aed30e-5a28-457e-db8b-d816128cd56a
---
# another way that some people create lists
some_list = list()
some_list
```

+++ {"id": "0c6wfPPRBHdg"}

### Get one thing out of a list: Indexing

Lists are composed of a sequence of slots, each of which has an index. Indexing is a way to get something out of a list at a specific index position. In English, we might say, "get me the 1st item in the list", or "get me the 3rd item in the list". In Python, it's a little bit different, since indices start at 0. So "the first item in the list" in Python would be "the item at index position 0 in the list".

Here are some examples:

```{code-cell} ipython3

```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 551
  status: ok
  timestamp: 1614610522269
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: mbd2VhkISFYn
outputId: c80b8581-3693-436c-dcff-dfba33cb8b6a
---
some_list = [3, 4, 5]
print(some_list[0]) # first item
print(some_list[1]) # second item
print(some_list[2]) # third item
```

A helpful trick for getting the last or nth-to-last item is to start the indexing in reverse. Confusingly, this indexing starts at 1... Sorry!
- -1 is last
- -2 is second last
- and so on...

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 626
  status: ok
  timestamp: 1614610682463
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: xwvAmA7wSWrV
outputId: f86128eb-46b2-4209-ba32-80b3886062e8
---
another_list = [3, 4, 5, 6, 7] # 5 items in this list
print(another_list[3]) # how to get the 4th item?
print(another_list[-1]) # get the last item
print(another_list[-2]) # get the 2nd-to-last item
```

This reverse indexing can be handy for getting smallest/largest after sorting a list, especially if there are lots of items in the list.

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 381
  status: ok
  timestamp: 1614610736446
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: Lw7deCzATAbr
outputId: 9f193319-40bb-4aa8-eb8c-944e6626704c
---
a = [4, 6, 1, 8, 20, 13]
a.sort()
a[-1]
```

Let's practice some more!

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 52
executionInfo:
  elapsed: 345
  status: ok
  timestamp: 1601911176562
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 240
id: dMIAR49WIUlY
outputId: f365d16e-cc9c-4c6b-944c-3378d4b25a8e
---
# get the 3rd item
x = [1, 2, 3]
y = ["one", "two", "three"]
print(x[2])
print(y[2])
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 52
executionInfo:
  elapsed: 337
  status: ok
  timestamp: 1601911183838
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 240
id: NbfXxjV1WMjU
outputId: 049638d1-6e84-4037-d28a-f7668a5e2909
---
# get the first item
print(x[0])
print(y[0])
```

+++ {"id": "fonfys6nIVpl"}

### Get multiple (contiguous) things out of a list: Slicing
**Slicing** is a variation of indexing that grabs more than one value. The colon specifies that you're slicing.

The first number is where you start.
The second number is the upper limit, i.e., up to but *not including*.

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 302
  status: ok
  timestamp: 1614610952691
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: fnwbasZjIoy4
outputId: 6a811205-8919-4941-a3ec-8f45285b2bf4
---
x = [
  4, # 0
  6, # 1
  8, # 2
  1, # 3
  2, # 4
  5  # 5
]
# get the first two items
print(x[0:2])
# get the last two items
print(x[-2:])
# get the items from the 3rd position onwards (i want to ignore the first two)
print(x[2:])
# get everything up to the 3rd position (i.e., index 2)
print(x[:3])
```

Let's practice some more!

```{code-cell} ipython3

```

+++ {"id": "yzUkh0MaIq5m"}

### Modify values ("mutate") in a list

Use the index to specify which part of the list you want to modify, and assign it a (new) value

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 266
  status: ok
  timestamp: 1614611020082
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: jJCGaIH-JEgc
outputId: 674469fa-f880-4e0a-cf07-099bb8638d78
---
x = [4,6,8,1,2,5]
print(x)
print("first item", x[0])
# change the first item to 10
x[0] = 10 # notice how this looks like an assignment statement
print(x)
print("new first item", x[0])
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 346
  status: ok
  timestamp: 1614611095437
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: AbmhTQK1UQ0Q
outputId: 648c39b7-ee3d-455d-d226-856dad80ebcc
---
x = [
  4, # 0
  6, # 1
  8, # 2
  1, # 3
  2, # 4
  5  # 5
]
# how do we modify this list so that the last item has the value 20?
x[5] = 20
# x[-1] = 20 # this is equivalent
x
```

Let's practice some more!

```{code-cell} ipython3

```

+++ {"id": "wDihMUBiI7EG"}

### Check what's in a list

Python provides the `in` operator that lets you check if an item is in a list.

It's a logical operator that returns True or False, so you can use it as a logica / Boolean expression, for use with conditionals and so on. You'll find this to be quite handy: we often want to be lazy and only do something if a list contains a thing we care about!

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 420
  status: ok
  timestamp: 1614611289236
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: 0qOxB7B8BM9O
outputId: 3fc7f987-bce4-43e8-c341-96056393e250
---
#
names = ["joe", "harry", "rachel", "kelly"]
1 in names
# if "joel" in names:
#     print("Found!")
# else:
#     print("Not found!")
```

+++ {"id": "7V0LiNCSJXRJ"}

## List methods and collection functions

There are a great many other built-in operations in Python that let you do things with lists. They fall into list *methods* and also built in *functions* that take a list as an argument.

+++ {"id": "haoFPw-RJxI0"}

### Collection functions

Python has built in functions that operate on lists as arguments
- `len()`
- math ones: `max()`, `min()`, `sum()`
- `sorted()`
- look for the ones that have an "iterable" as as parameter type here: https://docs.python.org/3/library/functions.html

These are functions, so mechanics are just like functions - function name, pass in list as an **input** argument, plus whatever other arguments might be needed, and get back some **output** value

Let's play with a few!

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 34
executionInfo:
  elapsed: 722
  status: ok
  timestamp: 1601912542470
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 240
id: 8JStG5a2Og92
outputId: 1efa4ab6-651d-4ee3-8879-6f7bd61a6639
---
# 
x = [1, 2, 3, 1, 4, 1, 5, 10, 12]
x_length = len(x) # get the length of x
print(x_length)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 34
executionInfo:
  elapsed: 506
  status: ok
  timestamp: 1601912581674
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 240
id: yHvKRjjZbZ6z
outputId: 45a21151-32e1-4c53-8d79-ccac9880e04d
---
# make a new list that is a sorted version of x. do this if you want to keep the original list around.
x_sorted = sorted(x) 
print(x_sorted)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 69
executionInfo:
  elapsed: 452
  status: ok
  timestamp: 1601912668333
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 240
id: 95EwmalVbsqr
outputId: fec77dae-3417-4ae1-c4b1-c524f4d62790
---
print(min(x))
print(max(x))
print(sum(x)/len(x)) # average, using suma nd len
```

```{code-cell} ipython3
list_of_strings = [
    "she",
    "sells",
    "seashells",
    "by",
    "the",
    "seashore"
]
sum(list_of_strings)
```

```{code-cell} ipython3
result = sorted(list_of_strings, reverse=True)
print(list_of_strings)
print(result)
```

+++ {"id": "jhnz1Dn9Jk9W"}

### List methods

Python lists also have *methods*. 

in Python, methods are like functions that only certain kinds of objects (e.g., list) can do. We'll see that many of the data structures in Python are like this, including strings in 2 weeks. And you can also create your own objects! You will learn much more about this in 326 - this is "object oriented programming".

All of the list methods are listed (no pun intended!) here: https://docs.python.org/3/tutorial/datastructures.html

Here are some common examples:

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 139
executionInfo:
  elapsed: 386
  status: ok
  timestamp: 1601912306276
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 240
id: ZHqVYGfVORJr
outputId: 5b821998-085e-41ac-d9d0-c70506b2937b
---
a_list = [1, 2, 3, 1, 4, 1, 5]
print("original list:", a_list)

# add something to the end of a list (WE'LL USE THIS A LOT)
a_list.append(4)
print("\n", a_list, "after appending 4")

# sort the list (WE'LL ALSO USE THIS A LOT)
a_list.sort()
print("\n", a_list, "after sorting")
# control how you sort
a_list.sort(reverse=True)
print("\n", a_list, "after sorting in reverse order")

# count how many times an item is in a list (handy for searching)
print("\nnumber of occurences of 1 in the list:", a_list.count(1)) # how many times does the number 1 show up in this list?

# where is 1 in the list?
print("\n1 is at position", a_list.index(1), "in the list")

# insert an item at a specific position
a_list.insert(0, 22)
print("\n", a_list, "after inserting 22 at the first position")
```

#### Syntax for (list) methods

Stepping back for a second, here's how it works, basically, syntax wise.

`nameOfVariable.nameOfMethod(anyArgumentsTheMethodsNeed)`

And in pictures:

```{image} assets/python-method-example.png
:alt: typeError
:class: bg-primary mb-1
:width: 800px
:align: center
```

+++

Note: unlike functions, list methods change the list itself; they do *not* return a new value. Like your functions that lack return statements, the return value of list methods is `None`. 

```{code-cell} ipython3
result = a_list.sort()
print(result)
```

If you want to keep the original list instead of modifying it directly, you should use the collection functions (e.g., `sorted()` instead of `list.sort()`). 

```{code-cell} ipython3
a_list = [5,2,7,10,3]
result = sorted(a_list)
print(a_list)
print(result)
```

+++ {"id": "fYsK_XmDJ70s"}

### Mapping methods/functions to situations

Let's practice! Keep these handy, and guess/propose situations where some of these methods/functions will be useful

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 446
  status: ok
  timestamp: 1614612023593
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: OsO4m_5YKAFw
outputId: 7845b6a7-e032-473b-cadd-54358df28608
---
# finding the smallest/biggest thing
x = [1, 2, 3]

# find the smallest?

# find the biggest?

# sort?

# filtering
```

+++ {"id": "lbpNvToHKA2H"}

Meta-points here
- Get in the habit of suspecting that something you want to do probably already has a function/method written for it that you can use (that probably does it well)
- Notice the docstrings!

+++ {"id": "-iQvhWi7KGAg"}

## Common errors

+++ {"id": "E9kblMRYOZJR"}

### Forgetting that indices start at 0

As I noted earlier, remember that indices start at 0. A common error to make if you forget this, is to get something at the wrong position!

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 448
  status: ok
  timestamp: 1614612132459
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: u8j1JsYXOgw0
outputId: 3e7fcd31-618e-4e63-a390-16c26945c4f4
---
a = [1, 2, 3]
a[1]
```

+++ {"id": "2P-04t43Knqj"}

### IndexError

Another common error is to try to get something from an index position that doesn't yet exist in a list.

For example, the list `x = [1, 4, 5]` has 3 items (has length 3). 

But! If I want to get the 3rd item with `x[3]`, I will get an IndexError, because the item only has indices that go up to 2!

Sometimes this happens if you forget 0-indexing, and try to get the "3rd item" with index 3 (instead of the correct index 2).

We'll return to this error next week, because it often shows up with iteration 

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 181
executionInfo:
  elapsed: 382
  status: error
  timestamp: 1614612163956
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: 8l94eUXEO0lK
outputId: 3924face-82ba-461e-94eb-a3b9ed1b4c4b
---
x = [1, 4, 5]
x[3]
```

+++ {"id": "kjU1dyhRKZ9l"}

### Mixing up mutable/immutable when using methods/functions

This happens most with operations that can be done wiht methods and functions, such as sorting

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 498
  status: ok
  timestamp: 1614612215212
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: 5LDRnY23POoo
outputId: 5a79b9a0-3b4b-4c59-9d4d-fdb3a9c3a3f7
---
x = [1, 7, 4, 2]
xsort = sorted(x) # don't change x, just make a  new list that is a sorted version of x
print(x)
print(xsort)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 395
  status: ok
  timestamp: 1614612441174
  user:
    displayName: Joel Chan
    photoUrl: https://lh3.googleusercontent.com/a-/AOh14GiBPPpBf_QqgDL3pMurAsPu9WJJE_x_6UtgW13UFQ=s64
    userId: '15153559228409906865'
  user_tz: 300
id: uKu5xkzPPh49
outputId: 595a1dde-aedc-41be-f698-33fa2c9c70b4
---
x = [1, 7, 4, 2]
xsort = x.sort() # modify x directly, we don't care if it changes, so it won't return a value and xsort will have None as its value
print(x)
print(xsort)
```
