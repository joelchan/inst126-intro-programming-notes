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

## Learning goals
- Create a list in Python
- Do common operations on lists (e.g., appending, indexing, slicing, sorting)
- Explain difference between mutable and immutable data structures
- Recognize potential application opportunities for collection methods and functions (e.g., len, max, min)
- Explain difference between functions and methods
- Appropriately apply collection methods and functions to lists

## What are lists and why should we care about them?

### A list is a kind of collection data structure

So far we’ve mostly used a “non-collection” data structures. Most of our variables have one value in them - when we put a new value in the variable, the old value is overwritten

A list is a kind of **collection** data structure. A collection allows us to put many values into a single "variable"

A collection is nice because we can carry many values around in one convenient package

```{code-cell} ipython3
a_list = []
s = ""
friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'shirt', 'perfume']
scores = [1, 50, 32]
```

```{code-cell} ipython3
friends
```

### Why do we need more data structures than strings, numbers and Boolean values?

Recall that computational thinking is a key component of programming skill. **Algorithms** --- sets of rules or steps used to solve a problem --- are an important way to model and instruct computers to solve problems. In computer science, it is well known that some algorithms need special **data structures** --- particular ways of organizing data in a computer.

Consider this problem: Find the smallest number amongst a set of N numbers.

Can you think of a structured set of rules (algorithms) for solving this problem in a reusable way *without* using a collection / list?

```{code-cell} ipython3
# find the smallest number amongst five numbers
a = 1
b = 5
c = 7
d = 10
e = 2  

def find_smallest_among_5(a, b, c, d, e):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    if d < smallest:
        smallest = d
    if e < smallest:
        smallest = e
    return smallest
```
What if we have six numbers? We can't reuse our function, need to modify to add more parameters and "switches" in our chained conditional.
```{code-cell} ipython3
def find_smallest_among_6(a, b, c, d, e, f):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    if d < smallest:
        smallest = d
    if e < smallest:
        smallest = e
    if f < smallest:
        smallest = f
    return smallest
```

What if we have three numbers? Again, can't reuse our function, need to modify to remove parameters and "switches" in our chained conditional.
```{code-cell} ipython3
# or just 3?
def find_smallest_among_3(a, b, c):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    return smallest
```

In contrast, check out what we can do if we have lists as a data structure! This is an elegant function that covers the class of "find smallest among N numbers" problems and can be reused and composed.
```{code-cell} ipython3
# with lists
def find_smallest(l):
    # sort the list
    l.sort()
    # get the first item
    return l[0]    
```

```{code-cell} ipython3
l = [4, 5, 7, 10, 2, 10, 15]
find_smallest(l)
```

Again, as you can see, we could in principle solve each variant of the "find smallest" problem with separate variables for each item. But it's very clunky! And error prone! And basically impossible to generalize (contra core goal of developing **abstractions over classes of problems**, from CompT).

The point to note here is that your ability to model (and therefore solve) problems with programming is dependent on your knowledge of data structures (since they constrain the set of algorithms you can recognize and apply to problems). So as you expand your knowledge of data structures, try to note down also the common situations in which they apply, and what algorithms they tend to "work well with".

You will learn a few more data structures this semester (dive more into strings this module, then files and dictionaries next module, and dataframes for data analysis in the final module). And of course many more as you advance in your career.

Here are lists in context of our example problem from last week:

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

## Anatomy of a list in Python

List constants or "literals":
1. Are surrounded by square brackets
2. Contain zero or more elements; multiple items are separated by commas.

```{code-cell} ipython3
"1, 2, 3" # string
1 # int
1.0 # float

basic_list = [1, 2, 3] # list
another_list = [11,32,53] # the spaces don't matter for Python, only the commas; spaces are for readability for us
another_list = [
    "a really long item in the list", 
    2,
    3
]
matrix = [
    [0, 1, 2],
    [0, 0, 1],
    [0, 1, 0]
]

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
sentences
```

```{code-cell} ipython3
basic_list
```

You can assign lists to variables, just like other values, with a variable assignment statement.

```{code-cell} ipython3
a = [1, 2, 3]
b = [1, "2", 3.0]
c = [a, b] # list of lists
print(a)
print(b)
print(c)
d = {"a": 1}
e = [d, a]
e
```

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

Let's demonstrate these properties by "dissecting" a few lists together.

### Can hold multiple types of data, including other lists

```{code-cell} ipython3
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
basic_list_3 = [
  "red", # psn 0
  "green", # psn 1
  "blue", # psn 2
  "yellow", # psn 3
  "white", # psn 4
    "black", # psn 5
]

# get the first item
basic_list_3[0]

# get the sixth item
basic_list_3[5]
```

Here it is in pictures.

```{image} assets/positive-indexes.png
:alt: typeError
:class: bg-primary mb-1
:width: 800px
:align: center
```

You can also index in reverse! Handy for getting the last item in a list.

```{image} assets/negative-indexes.png
:alt: typeError
:class: bg-primary mb-1
:width: 800px
:align: center
```

Yes, the alert reader will notice that this reverse indexing starts at... 1. So why does the indexing start at 0? I'm afraid I don't have a good answer. [Maybe it came from the design of the C programming language](https://albertkoz.com/why-does-array-start-with-index-0-65ffc07cbce8), and most languages (but not all!! R starts indexing at 1), followed suit.

```{code-cell} ipython3
print(basic_list_3[-1]) # gets you the last item, at position -1
print(basic_list_3[-2]) # gets you the 2nd last item, at position -2
```

### Mutating (changing) list values directly

```{code-cell} ipython3
basic_list_4 = [4, 6, 7, 10, 5]
print(basic_list_4)
basic_list_4[1] = 7 # can mutate the list (i.e., modify it directly)
print(basic_list_4)
```

## Working with lists

### Make a list
Can use the assignment statement to initialize to an empty list, or manually specify what's in a list

```{code-cell} ipython3

x = [1, 2, 3] # list with numbers 1 2 and 3
y = [] # empty list
z = [4, 7]
```

Can create from existing lists, using **concatenation** (adding two existing lists together)

```{code-cell} ipython3
new_list = x + z
new_list
```

```{code-cell} ipython3
# another way that some people create lists
some_list = list()
some_list
```

```{code-cell} ipython3
int("3")
```

### Get one thing out of a list: Indexing

Lists are composed of a sequence of slots, each of which has an index. Indexing is a way to get something out of a list at a specific index position. In English, we might say, "get me the 1st item in the list", or "get me the 3rd item in the list". In Python, it's a little bit different, since indices start at 0. So "the first item in the list" in Python would be "the item at index position 0 in the list".

Here are some examples:

```{code-cell} ipython3
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
another_list = [3, 4, 5, 6, 7] # 5 items in this list
print(another_list[3]) # how to get the 4th item?
print(another_list[-1]) # get the last item
print(another_list[-2]) # get the 2nd-to-last item
```

This reverse indexing can be handy for getting smallest/largest after sorting a list, especially if there are lots of items in the list.

```{code-cell} ipython3
a = [4, 6, 1, 8, 20, 13]
a.sort()
a[-1]
```

Let's practice some more!

```{code-cell} ipython3
# get the 3rd item
x = [1, 2, 3]
y = ["one", "two", "three"]
print(x[2])
print(y[2])
```

```{code-cell} ipython3
# get the first item
print(x[0])
print(y[0])
```

### Get multiple (contiguous) things out of a list: Slicing
**Slicing** is a variation of indexing that grabs more than one value. The colon specifies that you're slicing.

The first number is where you start.
The second number is the upper limit, i.e., up to but *not including*.

```{code-cell} ipython3
x = [
  4, # 0
  6, # 1
  8, # 2
  1, # 3
  2, # 4
  5  # 5
]
# get the first two items
# print(x[0:2])
# # get the last two items
# print(x[-2:])
# # get the items from the 3rd position onwards (i want to ignore the first two)
print(x[2:])
# # get everything up to the 3rd position (i.e., index 2)
# print(x[:3])
```

Let's practice some more!

```{code-cell} ipython3
# get everything up to the 4th item
x[:4]
```

### Modify values ("mutate") in a list

Use the index to specify which part of the list you want to modify, and assign it a (new) value

```{code-cell} ipython3
x = [4,6,8,1,2,5]
print(x)
print("first item", x[0])
# change the first item to 10
x[0] = 10 # notice how this looks like an assignment statement
print(x)
print("new first item", x[0])
```

```{code-cell} ipython3
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

### Check what's in a list

Python provides the `in` operator that lets you check if an item is in a list.

It's a logical operator that returns True or False, so you can use it as a logical / Boolean expression, for use with conditionals and so on. You'll find this to be quite handy: we often want to be lazy and only do something if a list contains a thing we care about!

```{code-cell} ipython3
names = ["joe", "harry", "rachel", "kelly"]
"joel" not in names
# if "joel" in names:
#     print("Found!")
# else:
#     print("Not found!")
```

## Practice: Code Tracing with Lists

For each problem below, **predict what the code will print** before running the cell. Then run the cell to check your answer!

### Trace 1

```{code-cell} ipython3
:tags: [remove-output]
colors = ["red", "blue", "green", "yellow"]
print(colors[1])
```

What does this print?
- A) `red`
- B) `blue`
- C) `green`
- D) Error

```{admonition} Answer:
:class: toggle
**B)** `blue`

Indexing starts at 0, so index 1 is the second item. If you picked A, you're thinking of index 1 as the "first" item — remember, that's index 0!
```

### Trace 2

```{code-cell} ipython3
:tags: [remove-output]
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[-1])
print(fruits[-3])
```

What does this print?
- A) `elderberry` and `date`
- B) `date` and `cherry`
- C) `elderberry` and `cherry`
- D) `elderberry` and `banana`

```{admonition} Answer:
:class: toggle
**C)** `elderberry` and `cherry`

Negative indexing starts from the end: -1 is the last item (`elderberry`), -3 is the third from the end (`cherry`). If you picked A, you may have counted -3 as third from the end starting at -1 (i.e., going -1, -2, -3 = `cherry`, `date`... but -3 lands on `cherry`, not `date`).
```

### Trace 3

```{code-cell} ipython3
:tags: [remove-output]
nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[2])
print(nums[4])
```

What does this print?
- A) `10`, `20`, `30`
- B) `10`, `30`, `50`
- C) `20`, `40`, `50`
- D) `20`, `40`, and then an Error

```{admonition} Answer:
:class: toggle
**B)** `10`, `30`, and `50`

Index 0 is the first item (`10`), index 2 is the third (`30`), and index 4 is the fifth and last (`50`). If you picked C or D, you may be thinking indices start at 1.
```

### Trace 4

```{code-cell} ipython3
:tags: [remove-output]
animals = ["cat", "dog", "fish", "bird"]
animals[2] = "hamster"
print(animals)
```

What does this print?
- A) `['cat', 'hamster', 'fish', 'bird']`
- B) `['cat', 'dog', 'hamster', 'bird']`
- C) `['cat', 'dog', 'fish', 'hamster']`
- D) `['cat', 'dog', 'fish', 'bird', 'hamster']`

```{admonition} Answer:
:class: toggle
**B)** `['cat', 'dog', 'hamster', 'bird']`

We replaced the item at index 2 (`"fish"`) with `"hamster"`. Lists are mutable! If you picked A, you're thinking index 2 is `"dog"` (off by one). If you picked D, you may be confusing mutation with `append()`.
```

### Trace 5

```{code-cell} ipython3
:tags: [remove-output]
scores = [88, 72, 95, 60, 84]
scores[3] = 75
print(scores)
print(scores[1] + scores[3])
```

What does this print?
- A) `[88, 72, 95, 75, 84]` and `147`
- B) `[88, 72, 95, 60, 84]` and `132`
- C) `[88, 72, 95, 75, 84]` and `167`
- D) `[88, 72, 95, 75, 84]` and `155`

```{admonition} Answer:
:class: toggle
**A)** `[88, 72, 95, 75, 84]` and `147`

We changed index 3 from 60 to 75. Then `scores[1] + scores[3]` is `72 + 75 = 147`. If you picked B, you missed the mutation at index 3. If you picked C, you may be grabbing the wrong indices (e.g., thinking index 1 is `88`).
```

### Trace 6

```{code-cell} ipython3
:tags: [remove-output]
vals = [10, 20, 30, 40, 50]
print(vals[1:3])
print(vals[:2])
print(vals[3:])
```

What does this print?
- A) `[20, 30]`, `[10, 20]`, `[40, 50]`
- B) `[20, 30, 40]`, `[10, 20]`, `[40, 50]`
- C) `[10, 20, 30]`, `[10, 20]`, `[30, 40, 50]`
- D) `[20, 30]`, `[10, 20, 30]`, `[40, 50]`

```{admonition} Answer:
:class: toggle
**A)** `[20, 30]`, `[10, 20]`, `[40, 50]`

Slicing: `[1:3]` gives indices 1 and 2 (up to but **not including** 3). `[:2]` gives the first 2 items. `[3:]` gives everything from index 3 onward. If you picked B, remember the upper bound is exclusive!
```

## List methods and collection functions

There are a great many other built-in operations in Python that let you do things with lists. They fall into list *methods* and also built in *functions* that take a list as an argument.

### Collection functions

Python has built in functions that operate on lists as arguments
- `len()`
- math ones: `max()`, `min()`, `sum()`
- `sorted()`
- look for the ones that have an "iterable" as as parameter type here: https://docs.python.org/3/library/functions.html

These are functions, so mechanics are just like functions - function name, pass in list as an **input** argument, plus whatever other arguments might be needed, and get back some **output** value

Let's play with a few!

```{code-cell} ipython3
# 
x = [1, 2, 3, 1, 4, 1, 5, 10, 12, 11]
x_length = len(x) # get the length of x
print(x_length)
```

```{code-cell} ipython3
# make a new list that is a sorted version of x. do this if you want to keep the original list around.
x_sorted = sorted(x) 
print(x_sorted)
```

```{code-cell} ipython3
print(min(x))
print(max(x))
print(sum(x)/len(x)) # average, using sum and len
```

NOTE: you can't use any of these math-y functions with lists of "not-numbers". For example, the following code will yield a `TypeError`:
```
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
### List methods

Python lists also have *methods*. 

in Python, methods are like functions that only certain kinds of objects (e.g., list) can do. We'll see that many of the data structures in Python are like this, including strings in 2 weeks. And you can also create your own objects! You will learn much more about this in 326 - this is "object oriented programming".

All of the list methods are listed (no pun intended!) here: https://docs.python.org/3/tutorial/datastructures.html

Here are some common examples:

```{code-cell} ipython3
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
a_list.insert(3, 22)
print("\n", a_list, "after inserting 22 at position 3")
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

Note: mutating list methods like `.sort()`, `.append()`, and `.insert()` change the list itself; they do *not* return a new value. Like your functions that lack return statements, their return value is `None`. (Other list methods like `.count()` and `.index()` do return values without modifying the list.) 

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

### Mapping methods/functions to situations

Let's practice! Keep these handy, and guess/propose situations where some of these methods/functions will be useful

```{code-cell} ipython3
# finding the smallest/biggest thing
x = [1, 2, 3, 7, 9, 11, 14]

# find the smallest?
min(x) # yes, we didn't actually even need to write our `find_smallest()` function above!

# find the biggest?
max(x)

# sort?
x.sort()

# filtering
def is_odd(n):
    return n % 2 != 0

# apply the "is_odd" function to filter all the elements in x, so that we only get items that pass the "is_odd" test
list(filter(is_odd, x))
```

Meta-points here
- Get in the habit of suspecting that something you want to do probably already has a function/method written for it that you can use (that probably does it well)
- Notice the docstrings!

+++ {"id": "-iQvhWi7KGAg"}

Try a couple more!

Remove "milk" from your grocery list, and add "butter" and "cookies" to the end of your list.
```
groceries = ["milk", "eggs", "ramen", "juice"]
# remove milk

# add butter

# add cookies
```

Complete the code for this function to add a new guest to a list of table_guests, but only if there is still room (i.e., length of table guests is under the table limit)
```
def add_to_table(table_guests, new_guest, table_limit):
    # check if the length of table_guests is current less than table_limit
    if :
        # if so, add the new_guest to the table_guests list
        
        # and return that table_guests list
        return 
    else:
        # otherwise, print a message to say that "the table is full!"
        
        # and return the table_guests list as is
        return 

add_to_table(["joel", "sara", "nehal", "christian"], "wayde", 4)
```

Complete the code for this function to keep the top n largest numbers in a list of numbers, making sure not to try to return more numbers than actually exist in the list!
```
def keep_biggest_n(nums, n):
    # sort nums
    
    # check if the length of nums is less than the desired n of items
    if :
        # if so, just return the whole nums list as is
        return 
    else:
        # otherwise, return the first n items from the sorted list
        return 

keep_biggest_n([5, 10, 2, 11, 60, 1000], 10)
```

<!-- ### Trace 6

```{code-cell} ipython3
:tags: [remove-output]
letters = ["a", "b", "c"]
letters.append("d")
print(letters)
print(letters[3])
print(len(letters))
```

What does this print?
- A) `['a', 'b', 'c', 'd']`, then `d`, then `4`
- B) `['a', 'b', 'c', 'd']`, then Error, then `4`
- C) `['a', 'b', 'c', 'd']`, then `d`, then `3`
- D) `['a', 'b', 'c']`, then Error, then `3`

```{admonition} Answer:
:class: toggle
**A)** `['a', 'b', 'c', 'd']`, then `d`, then `4`

`append()` adds `"d"` to the end of the list. It becomes index 3 (the 4th item), and `len()` returns `4`. If you picked C, remember that `append()` increases the length by 1. If you picked D, remember that `append()` modifies the list itself.
``` -->



<!-- ### Trace 8

```{code-cell} ipython3
:tags: [remove-output]
data = [5, 10, 15, 20, 25]
data[1] = 99
data.append(30)
print(data[1:4])
print(data[-2:])
```

What does this print?
- A) `[10, 15, 20]` and `[20, 25]`
- B) `[99, 15, 20]` and `[25, 30]`
- C) `[99, 15, 20]` and `[20, 25]`
- D) `[99, 15, 20, 25]` and `[25, 30]`

```{admonition} Answer:
:class: toggle
**B)** `[99, 15, 20]` and `[25, 30]`

After mutation, `data` is `[5, 99, 15, 20, 25, 30]` (6 items). Slice `[1:4]` gives indices 1, 2, 3 → `[99, 15, 20]`. Slice `[-2:]` gives the last two items → `[25, 30]`. If you picked A, you forgot the mutations. If you picked C, you forgot that `append(30)` added a 6th item.
```

### Trace 9

```{code-cell} ipython3
:tags: [remove-output]
result = []
result.append(10)
result.append(20)
result.append(30)
result[1] = 25
print(result)
print(result[0] + result[-1])
```

What does this print?
- A) `[10, 20, 30]` and `40`
- B) `[10, 25, 30]` and `40`
- C) `[10, 25, 30]` and `35`
- D) `[25, 20, 30]` and `55`

```{admonition} Answer:
:class: toggle
**B)** `[10, 25, 30]` and `40`

We build the list by appending: `[10, 20, 30]`. Then `result[1] = 25` changes index 1 from 20 to 25: `[10, 25, 30]`. Finally, `result[0] + result[-1]` is `10 + 30 = 40`. If you picked C, note that `result[-1]` is `30` (last item), not `25`. If you picked D, note that `result[1] = 25` changes index 1, not index 0.
```

### Trace 10

```{code-cell} ipython3
:tags: [remove-output]
a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
print(a is b)
```

What does this print?
- A) `[1, 2, 3]`, `[1, 2, 3, 4]`, `False`
- B) `[1, 2, 3, 4]`, `[1, 2, 3, 4]`, `True`
- C) `[1, 2, 3]`, `[1, 2, 3, 4]`, `True`
- D) `[1, 2, 3, 4]`, `[1, 2, 3, 4]`, `False`

```{admonition} Answer:
:class: toggle
**B)** `[1, 2, 3, 4]`, `[1, 2, 3, 4]`, `True`

This is tricky! `b = a` does **not** make a copy. Both `a` and `b` point to the *same* list in memory. So when we append to `b`, `a` also changes. This is called **aliasing**. If you picked A or C, you assumed `a` and `b` are separate lists — but they're not! If you wanted a separate copy, you'd need `b = a.copy()` or `b = list(a)`.
``` -->

## Practice: Code Tracing with List Methods and Functions

For each problem below, **predict what the code will print** before running the cell. Then run the cell to check your answer!

### Trace A

```{code-cell} ipython3
:tags: [remove-output]
nums = [4, 8, 2, 6, 1]
print(len(nums))
nums.append(10)
print(len(nums))
```

What does this print?
- A) `5` and `5`
- B) `5` and `6`
- C) `6` and `6`
- D) `4` and `5`

```{admonition} Answer:
:class: toggle
**B)** `5` and `6`

The list starts with 5 items. After `append(10)`, it has 6. If you picked A, remember that `append()` changes the list — `len()` reflects the new length.
```

### Trace B

```{code-cell} ipython3
:tags: [remove-output]
colors = ["red", "green", "blue"]
result = colors.append("yellow")
print(result)
print(colors)
```

What does this print?
- A) `['red', 'green', 'blue', 'yellow']` and `['red', 'green', 'blue', 'yellow']`
- B) `yellow` and `['red', 'green', 'blue', 'yellow']`
- C) `None` and `['red', 'green', 'blue', 'yellow']`
- D) `None` and `['red', 'green', 'blue']`

```{admonition} Answer:
:class: toggle
**C)** `None` and `['red', 'green', 'blue', 'yellow']`

`append()` is a mutating method — it modifies the list directly and returns `None`. The list itself is changed, but the return value is `None`. This is a very common trap!
```

### Trace C

```{code-cell} ipython3
:tags: [remove-output]
vals = [5, 2, 8, 1, 9]
result = vals.sort()
print(result)
print(vals)
```

What does this print?
- A) `[1, 2, 5, 8, 9]` and `[1, 2, 5, 8, 9]`
- B) `[1, 2, 5, 8, 9]` and `[5, 2, 8, 1, 9]`
- C) `None` and `[5, 2, 8, 1, 9]`
- D) `None` and `[1, 2, 5, 8, 9]`

```{admonition} Answer:
:class: toggle
**D)** `None` and `[1, 2, 5, 8, 9]`

Just like `append()`, `.sort()` is a mutating method — it sorts the list in place and returns `None`. If you picked A, remember: mutating methods don't return the modified list. If you want a return value, use `sorted()` instead.
```

### Trace D

```{code-cell} ipython3
:tags: [remove-output]
original = [5, 2, 8, 1, 9]
new_list = sorted(original)
print(original)
print(new_list)
```

What does this print?
- A) `[1, 2, 5, 8, 9]` and `[1, 2, 5, 8, 9]`
- B) `[5, 2, 8, 1, 9]` and `None`
- C) `[5, 2, 8, 1, 9]` and `[1, 2, 5, 8, 9]`
- D) `[1, 2, 5, 8, 9]` and `[5, 2, 8, 1, 9]`

```{admonition} Answer:
:class: toggle
**C)** `[5, 2, 8, 1, 9]` and `[1, 2, 5, 8, 9]`

`sorted()` is a **function** (not a method) that returns a **new** sorted list and leaves the original unchanged. Compare this to `.sort()`, which modifies the list and returns `None`.
```

### Trace E

```{code-cell} ipython3
:tags: [remove-output]
grades = [85, 92, 78, 92, 88, 92, 71]
print(grades.count(92))
print(grades.count(100))
```

What does this print?
- A) `3` and Error
- B) `2` and `0`
- C) `3` and `0`
- D) `1` and `0`

```{admonition} Answer:
:class: toggle
**C)** `3` and `0`

`.count(92)` returns `3` because 92 appears three times. `.count(100)` returns `0` because 100 isn't in the list — no error, just 0. If you picked D, remember `count()` finds **all** occurrences, not just the first.
```

### Trace F

```{code-cell} ipython3
:tags: [remove-output]
names = ["Amy", "Beth", "Carlos", "Diana"]
print(names.index("Carlos"))
print(names.index("Amy"))
```

What does this print?
- A) `3` and `1`
- B) `2` and `0`
- C) `3` and `0`
- D) `2` and `1`

```{admonition} Answer:
:class: toggle
**B)** `2` and `0`

`.index()` returns the position (index) where the item is found. `"Carlos"` is at index 2 (third item), and `"Amy"` is at index 0 (first item). If you picked A or C, remember indices start at 0!
```

### Trace G

```{code-cell} ipython3
:tags: [remove-output]
temps = [72, 68, 85, 90, 55]
print(min(temps))
print(max(temps))
print(sum(temps))
```

What does this print?
- A) `68`, `85`, `370`
- B) `55`, `90`, `370`
- C) `55`, `90`, `74`
- D) `72`, `90`, `370`

```{admonition} Answer:
:class: toggle
**B)** `55`, `90`, and `370`

`min()` returns the smallest value (`55`), `max()` returns the largest (`90`), and `sum()` adds them all up (`72 + 68 + 85 + 90 + 55 = 370`). If you picked C, note that `sum()` gives the total, not the average — for the average you'd need `sum(temps) / len(temps)`.
```

### Trace H

```{code-cell} ipython3
:tags: [remove-output]
tasks = ["email", "homework", "laundry"]
tasks.insert(1, "gym")
print(tasks)
print(len(tasks))
```

What does this print?
- A) `['email', 'gym', 'homework', 'laundry']` and `4`
- B) `['gym', 'email', 'homework', 'laundry']` and `4`
- C) `['email', 'homework', 'gym', 'laundry']` and `4`
- D) `['email', 'gym', 'homework', 'laundry']` and `3`

```{admonition} Answer:
:class: toggle
**A)** `['email', 'gym', 'homework', 'laundry']` and `4`

`.insert(1, "gym")` places `"gym"` at index 1, pushing everything after it over by one. The list grows from 3 to 4 items. If you picked B, note that index 1 is the *second* position, not the first.
```

### Trace I

```{code-cell} ipython3
:tags: [remove-output]
items = ["apple", "banana", "apple", "cherry", "apple"]
items.remove("apple")
print(items)
print(items.count("apple"))
```

What does this print?
- A) `['banana', 'cherry']` and `0`
- B) `['banana', 'apple', 'cherry', 'apple']` and `2`
- C) `['apple', 'banana', 'cherry', 'apple']` and `2`
- D) `['banana', 'apple', 'cherry']` and `1`

```{admonition} Answer:
:class: toggle
**B)** `['banana', 'apple', 'cherry', 'apple']` and `2`

`.remove()` only removes the **first** occurrence of the value, not all of them! So only the first `"apple"` (at index 0) is removed. Two `"apple"`s remain. If you picked A, that's a common misconception — `remove()` is not "remove all".
```

### Trace J

```{code-cell} ipython3
:tags: [remove-output]
scores = [40, 100, 75, 80, 60]
scores.sort()
top_three = scores[-3:]
print(top_three)
print(sum(top_three) / len(top_three))
```

What does this print?
- A) `[75, 80, 100]` and `85.0`
- B) `[40, 60, 75]` and `58.33`
- C) `[80, 100, 75]` and `85.0`
- D) `[75, 80, 100]` and `255`

```{admonition} Answer:
:class: toggle
**A)** `[75, 80, 100]` and `85.0`

After `.sort()`, `scores` is `[40, 60, 75, 80, 100]`. The slice `[-3:]` grabs the last three items: `[75, 80, 100]`. The average is `(75 + 80 + 100) / 3 = 85.0`. If you picked B, note that `[-3:]` gets the last 3 (largest after sorting), not the first 3.
```

### Trace K

```{code-cell} ipython3
:tags: [remove-output]
inventory = ["sword", "shield", "potion", "potion", "arrow"]
inventory.remove("potion")
inventory.append("bow")
inventory.sort()
print(inventory)
print(inventory[0])
print(inventory.count("potion"))
```

What does this print?
- A) `['arrow', 'bow', 'potion', 'shield', 'sword']`, `arrow`, `1`
- B) `['arrow', 'bow', 'shield', 'sword']`, `arrow`, `0`
- C) `['arrow', 'bow', 'potion', 'potion', 'shield', 'sword']`, `arrow`, `2`
- D) `['arrow', 'bow', 'potion', 'shield', 'sword']`, `arrow`, `0`

```{admonition} Answer:
:class: toggle
**A)** `['arrow', 'bow', 'potion', 'shield', 'sword']`, `arrow`, `1`

Step by step: `remove("potion")` removes only the *first* `"potion"` → `["sword", "shield", "potion", "arrow"]`. Then `append("bow")` → `["sword", "shield", "potion", "arrow", "bow"]`. Then `sort()` puts them in alphabetical order. One `"potion"` remains. If you picked B, remember `remove()` only takes out the first occurrence.
```

### Trace L

```{code-cell} ipython3
:tags: [remove-output]
nums = [3, 7, 1, 9, 4]
a = sorted(nums)
b = nums.sort()
print(nums == a)
print(b == a)
print(b)
```

What does this print?
- A) `True`, `True`, `[1, 3, 4, 7, 9]`
- B) `True`, `False`, `None`
- C) `False`, `False`, `None`
- D) `True`, `True`, `None`

```{admonition} Answer:
:class: toggle
**B)** `True`, `False`, `None`

`sorted(nums)` returns `[1, 3, 4, 7, 9]` and stores it in `a`, leaving `nums` as `[3, 7, 1, 9, 4]`. Then `nums.sort()` sorts `nums` in place (now `[1, 3, 4, 7, 9]`) and returns `None` (stored in `b`). So `nums == a` is `True` (both are `[1, 3, 4, 7, 9]`), but `b == a` is `False` (`None` is not equal to a list). If you picked D, remember that `None == [1, 3, 4, 7, 9]` is `False`!
```

### Trace M

```{code-cell} ipython3
:tags: [remove-output]
playlist = ["jazz", "rock", "pop"]
playlist.insert(0, "blues")
playlist.insert(2, "funk")
playlist.append("soul")
print(playlist)
print(playlist.index("pop"))
print(len(playlist))
```

What does this print?
- A) `['blues', 'jazz', 'funk', 'rock', 'pop', 'soul']`, `4`, `6`
- B) `['blues', 'funk', 'jazz', 'rock', 'pop', 'soul']`, `4`, `6`
- C) `['blues', 'jazz', 'funk', 'rock', 'pop', 'soul']`, `3`, `6`
- D) `['jazz', 'blues', 'rock', 'funk', 'pop', 'soul']`, `4`, `6`

```{admonition} Answer:
:class: toggle
**A)** `['blues', 'jazz', 'funk', 'rock', 'pop', 'soul']`, `4`, `6`

Step by step: `insert(0, "blues")` puts `"blues"` at index 0 → `["blues", "jazz", "rock", "pop"]`. Then `insert(2, "funk")` puts `"funk"` at index 2 → `["blues", "jazz", "funk", "rock", "pop"]`. Then `append("soul")` adds to the end → `["blues", "jazz", "funk", "rock", "pop", "soul"]`. `"pop"` is at index 4. If you picked B, note that the second `insert` happens *after* the first one already shifted things around.
```

### Trace N

```{code-cell} ipython3
:tags: [remove-output]
data = [10, 20, 30, 40, 50]
first_half = data[:2]
second_half = data[2:]
second_half.sort(reverse=True)
combined = first_half + second_half
print(combined)
print(data)
```

What does this print?
- A) `[10, 20, 50, 40, 30]` and `[10, 20, 50, 40, 30]`
- B) `[10, 20, 50, 40, 30]` and `[10, 20, 30, 40, 50]`
- C) `[50, 40, 30, 10, 20]` and `[10, 20, 30, 40, 50]`
- D) `[10, 20, 30, 40, 50]` and `[10, 20, 30, 40, 50]`

```{admonition} Answer:
:class: toggle
**B)** `[10, 20, 50, 40, 30]` and `[10, 20, 30, 40, 50]`

Slicing creates **new** lists, so `first_half` and `second_half` are separate from `data`. Sorting `second_half` in reverse gives `[50, 40, 30]`. Concatenating gives `[10, 20, 50, 40, 30]`. But `data` is still `[10, 20, 30, 40, 50]` — it was never modified. If you picked A, remember that slicing makes copies, unlike `b = a` (aliasing).
```

### Trace O

```{code-cell} ipython3
:tags: [remove-output]
readings = [72, 85, 90, 68, 95, 55]
readings.remove(min(readings))
readings.remove(max(readings))
print(readings)
print(sum(readings) / len(readings))
```

What does this print?
- A) `[72, 85, 90, 68]` and `78.75`
- B) `[85, 90, 68, 95]` and `84.5`
- C) `[72, 85, 90, 68]` and `315`
- D) `[72, 85, 68, 90]` and `78.75`

```{admonition} Answer:
:class: toggle
**A)** `[72, 85, 90, 68]` and `78.75`

`min(readings)` is `55`, so `remove(55)` gives `[72, 85, 90, 68, 95]`. Then `max(readings)` is now `95`, so `remove(95)` gives `[72, 85, 90, 68]`. The average is `(72 + 85 + 90 + 68) / 4 = 78.75`. Note that `max()` is recalculated on the list *after* the first removal — order of operations matters! If you picked B, you may have removed the original max/min simultaneously rather than sequentially.
```

## Practice: List Operations

For each problem below, **write code** in the empty cell to solve the problem. Check the toggle for a sample solution.

### P1 - Count items with `len()`

You have a list of grocery items. Use `len()` to print how many items are on the list.

```{code-cell} ipython3
groceries = ["milk", "eggs", "bread", "butter", "cheese", "apples"]
# Your code here: print the number of items in the list
```

````{admonition} Answer:
:class: toggle
```python
print(len(groceries))
```
Output: `6`
````

### P2 - Build a list with `append()`

Start with an empty list called `evens`. Use `append()` to add the numbers 2, 4, 6, 8, and 10 to it. Then print the list.

```{code-cell} ipython3
# Your code here
```

````{admonition} Answer:
:class: toggle
```python
evens = []
evens.append(2)
evens.append(4)
evens.append(6)
evens.append(8)
evens.append(10)
print(evens)
```
Output: `[2, 4, 6, 8, 10]`
````

### P3 - Sort in place with `sort()` and get smallest/largest

You have a list of test scores. Sort the list in place, then print the smallest score (first item) and the largest score (last item).

```{code-cell} ipython3
test_scores = [78, 92, 65, 88, 71, 95, 83]
# Your code here
```

````{admonition} Answer:
:class: toggle
```python
test_scores.sort()
print("Smallest:", test_scores[0])
print("Largest:", test_scores[-1])
```
Output: `Smallest: 65` and `Largest: 95`
````

### P4 - Make a sorted copy with `sorted()`

You have a list of names. Use `sorted()` to create a new alphabetically sorted list, without changing the original. Print both lists to verify.

```{code-cell} ipython3
names = ["Zara", "Amy", "Marcus", "Beth"]
# Your code here
```

````{admonition} Answer:
:class: toggle
```python
names_sorted = sorted(names)
print("Original:", names)
print("Sorted:", names_sorted)
```
The original list stays the same because `sorted()` returns a new list.
````

### P5 - Compute stats with `min()`, `max()`, `sum()`

You have a list of daily temperatures. Print the minimum, maximum, and average temperature.

```{code-cell} ipython3
temps = [72, 68, 75, 80, 73, 69, 77]
# Your code here
```

````{admonition} Answer:
:class: toggle
```python
print("Min:", min(temps))
print("Max:", max(temps))
print("Average:", sum(temps) / len(temps))
```
````

### P6 - Count occurrences with `count()`

You have a list of colors. Use `count()` to print how many times `"blue"` appears in the list.

```{code-cell} ipython3
colors = ["red", "blue", "green", "blue", "yellow", "blue", "red"]
# Your code here
```

````{admonition} Answer:
:class: toggle
```python
print(colors.count("blue"))
```
Output: `3`
````

### P7 - Find position with `index()`

You have a list of students. Use `index()` to find and print the position of `"Marcus"` in the list.

```{code-cell} ipython3
students = ["Amy", "Beth", "Carlos", "Marcus", "Zara"]
# Your code here
```

````{admonition} Answer:
:class: toggle
```python
print(students.index("Marcus"))
```
Output: `3`
````

### P8 - Check membership with `in`

You have a list of approved users. Write code that checks if `"joel"` is in the list. If yes, print `"Access granted"`. If not, print `"Access denied"`.

```{code-cell} ipython3
approved = ["sara", "nehal", "christian", "wayde"]
# Your code here
```

````{admonition} Answer:
:class: toggle
```python
if "joel" in approved:
    print("Access granted")
else:
    print("Access denied")
```
Output: `Access denied`
````

### P9 - Insert at a position with `insert()`

You have a to-do list. Use `insert()` to add `"buy groceries"` as the second item (index 1) in the list. Print the list before and after.

```{code-cell} ipython3
todos = ["wake up", "go to class", "do homework", "sleep"]
# Your code here
```

````{admonition} Answer:
:class: toggle
```python
print("Before:", todos)
todos.insert(1, "buy groceries")
print("After:", todos)
```
Output: `['wake up', 'buy groceries', 'go to class', 'do homework', 'sleep']`
````

### P10 - Remove by value with `remove()`

You have a list of ingredients but realize you don't need `"salt"`. Use `remove()` to take it out, then print the updated list.

```{code-cell} ipython3
ingredients = ["flour", "sugar", "salt", "eggs", "milk"]
# Your code here
```

````{admonition} Answer:
:class: toggle
```python
ingredients.remove("salt")
print(ingredients)
```
Output: `['flour', 'sugar', 'eggs', 'milk']`
````

### P11 - Combine operations

Write a function `get_top_3(numbers)` that takes a list of numbers and returns a new list containing only the 3 largest numbers, sorted from largest to smallest. Use `sorted()` and slicing.

```{code-cell} ipython3
# Your code here

# Test it:
# print(get_top_3([10, 45, 23, 78, 5, 67, 34]))
```

````{admonition} Answer:
:class: toggle
```python
def get_top_3(numbers):
    sorted_nums = sorted(numbers, reverse=True)
    return sorted_nums[:3]

print(get_top_3([10, 45, 23, 78, 5, 67, 34]))
```
Output: `[78, 67, 45]`
````

### P12 - `sort()` vs `sorted()`: predict the output

This is a tracing problem! **Predict the output** before running the cell.

```{code-cell} ipython3
:tags: [remove-output]
x = [3, 1, 4, 1, 5]
y = sorted(x)
z = x.sort()
print("x:", x)
print("y:", y)
print("z:", z)
```

````{admonition} Answer:
:class: toggle
`x: [1, 1, 3, 4, 5]`, `y: [1, 1, 3, 4, 5]`, `z: None`

`sorted(x)` returns a new sorted list (assigned to `y`) and leaves `x` unchanged at that point. Then `x.sort()` sorts `x` in place and returns `None` (assigned to `z`). The key lesson: **mutating methods** like `.sort()` change the list directly and return `None`.
````

### P13 - Remove the outliers

Write a function `remove_outliers(readings)` that takes a list of numbers, removes the single smallest and single largest values, and returns the remaining list. Don't modify the original list.

```{code-cell} ipython3
# Your code here

# Test it:
# data = [72, 85, 90, 68, 95, 55]
# print(remove_outliers(data))  # should print [68, 72, 85, 90]
# print(data)  # should still be [72, 85, 90, 68, 95, 55]
```

````{admonition} Answer:
:class: toggle
```python
def remove_outliers(readings):
    cleaned = sorted(readings)
    cleaned.remove(min(cleaned))
    cleaned.remove(max(cleaned))
    return cleaned

data = [72, 85, 90, 68, 95, 55]
print(remove_outliers(data))
print(data)
```
Using `sorted()` creates a new list, so the original is safe. Then `remove()` takes out the min and max from the copy. Output: `[68, 72, 85, 90]` and `[72, 85, 90, 68, 95, 55]`.
````

### P14 - Build a roster

Write a function `build_roster(names)` that takes a list of names and returns a new list that is:
1. Sorted alphabetically
2. Has no duplicates (each name appears only once)

Hint: use `count()` or `in` to check for duplicates as you build the new list.

```{code-cell} ipython3
# Your code here

# Test it:
# print(build_roster(["Zara", "Amy", "Marcus", "Amy", "Zara", "Beth"]))
# should print ['Amy', 'Beth', 'Marcus', 'Zara']
```

````{admonition} Answer:
:class: toggle
```python
def build_roster(names):
    roster = []
    for name in names:
        if name not in roster:
            roster.append(name)
    roster.sort()
    return roster

print(build_roster(["Zara", "Amy", "Marcus", "Amy", "Zara", "Beth"]))
```
We loop through the names and only `append()` if the name isn't already in the roster. Then we `sort()` at the end. Output: `['Amy', 'Beth', 'Marcus', 'Zara']`.
````

### P15 - Move an item to the front

Write a function `move_to_front(items, value)` that takes a list and a value, and moves that value to the front of the list (index 0). If the value isn't in the list, print `"Not found"` and return the list unchanged. Modify the list in place and return it.

```{code-cell} ipython3
# Your code here

# Test it:
# print(move_to_front(["a", "b", "c", "d"], "c"))  # ['c', 'a', 'b', 'd']
# print(move_to_front(["a", "b", "c"], "z"))  # Not found \n ['a', 'b', 'c']
```

````{admonition} Answer:
:class: toggle
```python
def move_to_front(items, value):
    if value in items:
        items.remove(value)
        items.insert(0, value)
    else:
        print("Not found")
    return items

print(move_to_front(["a", "b", "c", "d"], "c"))
print(move_to_front(["a", "b", "c"], "z"))
```
First check membership with `in`. If found, `remove()` takes it out, then `insert(0, ...)` puts it at the front. This combines `in`, `remove()`, and `insert()`.
````

### P16 - Compute a trimmed average

Write a function `trimmed_average(scores, n)` that:
1. Sorts the scores
2. Removes the `n` lowest and `n` highest scores
3. Returns the average of the remaining scores

If removing `n` from each end would leave fewer than 1 score, print `"Not enough scores"` and return `None`.

```{code-cell} ipython3
# Your code here

# Test it:
# print(trimmed_average([100, 55, 85, 90, 72, 68, 95], 2))  # should be 82.33...
# print(trimmed_average([10, 20, 30], 2))  # Not enough scores \n None
```

````{admonition} Answer:
:class: toggle
```python
def trimmed_average(scores, n):
    if len(scores) - 2 * n < 1:
        print("Not enough scores")
        return None
    trimmed = sorted(scores)
    trimmed = trimmed[n:len(trimmed) - n]
    return sum(trimmed) / len(trimmed)

print(trimmed_average([100, 55, 85, 90, 72, 68, 95], 2))
print(trimmed_average([10, 20, 30], 2))
```
We use `sorted()` to avoid modifying the original, then slice off `n` from each end with `[n:len(trimmed) - n]`. This combines `sorted()`, slicing, `len()`, `sum()`, and a conditional guard.
````

### P17 - Find the runner-up

Write a function `runner_up(scores)` that takes a list of scores and returns the second-highest score. The list may contain duplicates — if the highest score appears more than once, the runner-up should be a *different* value, not another copy of the highest.

If there is no runner-up (all scores are the same, or the list has fewer than 2 items), return `None`.

```{code-cell} ipython3
# Your code here

# Test it:
# print(runner_up([88, 95, 95, 72, 88]))  # should be 88
# print(runner_up([100, 100, 100]))  # should be None
# print(runner_up([42]))  # should be None
```

````{admonition} Answer:
:class: toggle
```python
def runner_up(scores):
    unique = []
    for s in scores:
        if s not in unique:
            unique.append(s)
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

print(runner_up([88, 95, 95, 72, 88]))
print(runner_up([100, 100, 100]))
print(runner_up([42]))
```
We first build a list of unique values (like P14), then sort and grab the second-to-last item with `[-2]`. This combines `in`, `append()`, `len()`, `sort()`, and negative indexing. Output: `88`, `None`, `None`.
````


## Common errors

### Forgetting that indices start at 0

As I noted earlier, remember that indices start at 0. A common error to make if you forget this, is to get something at the wrong position!

```{code-cell} ipython3
a = [1, 2, 3]
a[1]
```

### IndexError

Another common error is to try to get something from an index position that doesn't yet exist in a list.

For example, the list `x = [1, 4, 5]` has 3 items (has length 3). 

But! If I want to get the 3rd item with `x[3]`, I will get an IndexError, because the item only has indices that go up to 2!

Sometimes this happens if you forget 0-indexing, and try to get the "3rd item" with index 3 (instead of the correct index 2).

We'll return to this error next week, because it often shows up with iteration 

```{code-cell} ipython3
x = [1, 4, 5]
x[3]
```

### Mixing up mutable/immutable when using methods/functions

This happens most with operations that can be done with methods and functions, such as sorting

```{code-cell} ipython3
x = [1, 7, 4, 2]
xsort = sorted(x) # don't change x, just make a  new list that is a sorted version of x
print(x)
print(xsort)
```

```{code-cell} ipython3
x = [1, 7, 4, 2]
xsort = x.sort() # modify x directly, we don't care if it changes, so it won't return a value and xsort will have None as its value
print(x)
print(xsort)
```
