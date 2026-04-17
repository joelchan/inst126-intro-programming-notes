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

# 8: Dictionaries

## What are dictionaries and why should we care about them?

Dictionaries are for **associating data** and **quick lookup**

Motivating example: I am making an index for a book, because I want to know which concepts show up on which pages, to make it easier to jump back to the right spots.

```{code-cell} ipython3
# how to know which chapters talk about strings? or debugging?
book = [
  "Chapter 1: talks about strings and how they have the property of immutability also some basic debugging",
  "Chapter 2: continues talking about advanced methods for strings and also introduces the concept of functions",
  "Chapter 3: discusses iteration and lists and also debugging",
]
```

Here's what it might look like *without* dictionaries.

```{code-cell} ipython3
concepts = ['strings', 'debugging', 'immutability']
index = []

for chapter in book:
    # split into elements based on the colon
    elements = chapter.split(":")
    # first element is the chapter
    chapter = elements[0]
    # second element is the text
    text = elements[1]

    # parse the text
    words = text.split()
    for keyconcept in concepts:
        if keyconcept in words:
            index.append([keyconcept, chapter])
index
```

```{code-cell} ipython3
# given this data structure, how to find
# all the chapters that have strings in them?
query = "strings"
results = []
# go through every item in the index
for item in index:
    concept, chapter = item
    # if the concept matches the query
    if query == concept:
        results.append(chapter)

print(results)
```

And here is what it might look like *with* dictionaries.

```{code-cell} ipython3
# now consider if the concept index is in a dictionary (much more like what you might see in a book!)
index_d = {
    'strings': ['Chapter 1', 'Chapter 2'],
    'debugging': ['Chapter 1', 'Chapter 3']
}
```

```{code-cell} ipython3
# given this data structure, how to find
# all the chapters that have strings in them?
query = "strings"
index_d.get("strings")
```

Another common use case: attributes of data entries. For instance, attributes of a class, like credit hours, pre-reqs, instructor, location, hours, and so on.

```{code-cell} ipython3
# without dictionaries
courses = [
    ["INST126", 3, "no", "Chan", "hybrid", "MWF"],
    ["INST256", 4, "yes", "Kanishka", "in-person", "TR"]
]

# look up INST126 and check whether it has prereqs
for course in courses:
    if course[0] == "INST126":
        print(course[2])
```

Rather than trying to remember which position we happened to have decided to use to store a particular attribute (if we used lists), we can use **semantically meaningful indices for values**, i.e., keys!

```{code-cell} ipython3
# with dictionaries
courses = {
    "INST126": {
      "credit hours": 3, "prereqs": "no", "instructor": "Chan", "location": "hybrid", "hours": "MWF"
      },
    "INST256": {
      "credit hours": 4, "prereqs": "yes", "instructor": "Rony", "location": "in-person", "hours": "TR"
      },
}

# look up INST126 and check whether it has prereqs
courses.get("INST256").get("instructor")
```

It's a lot easier to remember keys (if we name them useful things) compared to just indices. And Python can help us remember too!

If you're interested, there are also formal technical reasons to prefer dictionaries over lists if you care about speed/efficiency and your computational task is **checking** if an item exists in a collection *and* you're dealing with very large scale data. The short version: looking up a key in a dictionary is O(1) (constant time: just 1 operation, no matter how big the dictionary is), while checking if an item is in a list is O(n) (grows with the size of the list: even though computers are pretty fast, when you get to quite large database sizes, you'll notice a difference!). See https://www.geeksforgeeks.org/python/difference-between-list-and-dictionary-in-python/ for a beginner-friendly explanation, or https://wiki.python.org/moin/TimeComplexity for the official reference.

In the future, you may learn the `pandas` library (and the `dataframe` data structure, which is sort of a hybrid of `lists` and `dictionaries`): you can do really fast lookup, but also sort stuff!

## Anatomy of a dictionary

Dictionaries are not so different from... our dictionaries in real life. :) Basically *map* a bunch of **keys** (e.g., a word) to corresponding **values** (e.g., a definition). Another example is indices in the back of print books that map key terms to pages where that term shows up, or tags on websites, that map tags to webpages that include those tags.

The key parts of a dictionary `literal` are:
1. The `{ }` curly braces, which tell you and Python that it's a dictionary (similar to `""` for strings, or `[]` for lists)
2. At least one **entry** (but usually several), that maps a **value** on the right of a  `:` --- which functions like the `=` expression --- to a **key** on the left. For example, our first entry maps the value "apple" to the key "a".
3. Similar to lists, we include `,` to separate multiple entries in the dictionary.

Let's look at a simple example that maps letters to an example word that starts with the letter

```{code-cell} ipython3
d = {
   'a': 'apple', # an entry that maps the value apple to the letter a
   'b': 'ball', # another entry that maps the value ball to the letter b
   'c': 'crayon'
}
d
```

Style note: the indentation inside the dictionary is more for readability. Python doesn't care, as long as there are commas between the dictionary entries.

You can also write it out like this, but I find it harder to read:

```{code-cell} ipython3
d = {'a': 'apple', 'b': 'ball', 'c': 'crayon'}
d
```

Here are some other examples.

```{code-cell} ipython3
# map letters to numbers
another = {
    'a': 1,
    'b': 2,
    'c': 3
}

# map letter grades to list of scores
grades = {
    'A': [93, 100],
    'B': [87, 93]
}
```

### Properties of a dictionary

Here are some key properties of a dictionary in Python:

#### Dictionaries have length

Similar to lists, dictionaries have **length**.

```{code-cell} ipython3
d = {
   'a': 'apple', # an entry that maps the value apple to the letter a
   'b': 'ball', # another entry that maps the value ball to the letter b
   'c': 'crayon'
}
len(d)
```

#### Dictionaries do not have an order or indexing by position

Different from lists, dictionaries **do not have an order**. So you can't really sort a dictionary, or grab things by position. You grab things by... key!

```{code-cell} ipython3
:tags: [raises-exception]

# can't get things by position
d[0]
```

```{code-cell} ipython3
:tags: [raises-exception]

# can't sort either
d.sort()
```

```{code-cell} ipython3
sorted(d) # this does *not* sort the dictionary; it returns a sorted list of the keys
```

Though as we will see next week, you can sneakily get some order, because Python now allows you to actually iterate through a dictionary in the order that stuff was put into it. It's not reliable though! If you need your collection to have an actual sequence to it, don't use dictionaries!

#### All keys in a dictionary are unique

Also, all keys in a dictionary have to be **unique**. This makes dictionaries handy for keeping track of unique items (in contrast to say, lists, where you can have duplicate entries).

Values in the dictionary do *not* have to be unique, though: you can have different keys point to the same value, but not multiple values point to duplicate keys. There is a related data structure that has a similar property called `sets` if you're interested.

```{code-cell} ipython3
d = {
   'a': 'apple', # an entry that maps the value apple to the letter a
   'b': 'ball', # another entry that maps the value ball to the letter b
   'c': 'crayon',
   'a': 'animal',
   'd': 'ball'
}
print(d) # oops, where did apple go? overwritten by the last a:animal entry since we can't have duplicate keys. d:ball is fine though, even though we already have b:ball.
```

#### Dictionaries are mutable

Like lists, dictionaries are also **mutable**: you can modify them directly (in contrast to strings, where you never modify them directly, but only ever create a new modified version of the string).

```{code-cell} ipython3
print(f"d before modification: {d}")
print("modifying d, by adding an entry mapping the key f to the value friend")
d.update({"f": "friend"})
print(f"d after modification: {d}")
```

### What kinds of data can we put in a dictionary?

#### Anything goes for values

Basically anything goes for **values**. You can even nest a dictionary inside another dictionary, by mapping a dictionary value to some key.

```{code-cell} ipython3
def hello():
    print("hello world!")

d = {
   'a': ['apple', "animal"], # an entry that maps a list to the letter a
   'b': 'ball', # another entry that maps the value ball to the letter b
   'c': 2,
   'd': [1, 3, "denizen"],
   'e': hello # even a function is fine!
}
d
```

```{code-cell} ipython3
students = {
    'joel': {
        'major': 'info sci',
        'year': 'senior',
        'interests': ['programming', 'football', 'dancing']
    },
}
students
```

#### Keys must be hashable

But **keys** need to be *hashable*.

What does this mean?

From the [Python glossary](https://docs.python.org/3/glossary.html):

> An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method), and can be compared to other objects (it needs an __eq__() or __cmp__() method). Hashable objects which compare equal must have the same hash value. Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.

> All of Python's immutable built-in objects are hashable, while no mutable containers (such as lists or dictionaries) are. Objects which are instances of user-defined classes are hashable by default; they all compare unequal, and their hash value is their id().

More info here: https://stackoverflow.com/questions/14535730/what-does-hashable-mean-in-python

```{code-cell} ipython3
:tags: [raises-exception]

d = {['3']: 'apple'}
```

I mention this because a common error when first working with dictionaries is to try to use an unhashable data structure as a key.

Understanding hashes is not something to worry about *for now*. We can focus on a basic rule of thumb for now: strings and numbers are ok as keys; everything else (that you'll learn now) is not.

## Working with dictionaries: basics

### Create a dictionary

```{code-cell} ipython3
d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon',
}
```

You can also start with an empty dictionary, and then add stuff later, programmatically or with other functions.

```{code-cell} ipython3
emptyd = {} # dictionary with nothing in it
emptyd = dict() # same thing
print(emptyd)
len(emptyd)
```

**PRACTICE**: make a dictionary e that has the following entries: smith:A, chan:B, abuye:A+

```{code-cell} ipython3
# your code here
```

### Get the value associated with a key from a dictionary

```{code-cell} ipython3
d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon'
}
d['c'] # put a key inside square brackets associated with a dictionary
```

This is called the "old style" or "indexing" pattern. Looks a little bit like lists.

```{code-cell} ipython3
d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon'
}
d.get('c') # use the get function to get the value for the key that we give it
```

This is the newer pattern that I prefer for clarity.

It also has the advantage of not breaking your program if you try to access a key that doesn't exist.

```{code-cell} ipython3
:tags: [raises-exception]

d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon'
}
d['d'] # will crash the program with key error
```

`.get()` lets you specify a default value that should come back if the key doesn't exist. This is very useful for writing clean and understandable dictionary patterns, such as indexing, which we'll dig into next week.

```{code-cell} ipython3
d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon'
}
result = d.get('d', "Key not found") # will return "Key not found" as the default
print(result)
```

**PRACTICE**: how do you get the value associated with the key `a`?

```{code-cell} ipython3
# your code here
```

### Adding entries to a dictionary (or updating entries)

Classic style, using indexing and assignment

```{code-cell} ipython3
d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon'
}
print(d)
# add a new entry for e
d['e'] = 'egg' # map the value egg to the key e
print(d)
# update the entry for b
d['b'] = 'bread' # map the value bread to the key b (which happens to already exist, so we update it)
print(d)
# update the entries for a and c
d['a'] = 'ashes'
d['c'] = 'charming'
print(d)
```

Newer style, using `.update()`

```{code-cell} ipython3
d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon'
}
print(d)
# add a new entry for e
d.update({'e': 'egg'}) # map the value egg to the key e
print(d)
# update the entry for b
d.update({'b': 'bread'}) # map the value bread to the key b (which happens to already exist, so we update it)
print(d)
# update the entries for a and c
new_for_a = "ashes"
d.update({'a': new_for_a, 'c': 'charming'})
print(d)
```

**PRACTICE**: how do you update d with new entry `h:hello`?

```{code-cell} ipython3
# your code here
```

**PRACTICE**: how do you update d so that `a` maps to the value `asteroid`?

```{code-cell} ipython3
# your code here
```

`.update()` has the advantage of being able to add multiple key-value pairs at once.

```{code-cell} ipython3
d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon'
}
print(d)
d.update({'a': 'ashes', 'b':'bread', 'c':'charming', 'e': 'egg'})
print(d)
```

**PRACTICE**: how do you update d with new entries `f:friend` and `g:grapes` in a single operation?

```{code-cell} ipython3
# your code here
```

**PRACTICE**: how do you update d so that `f` now points to `funny` and `b` points to `bundle`, in a single operation?

```{code-cell} ipython3
# your code here
```

You can use the pattern that is comfortable for you, but I prefer `.get()` and `.update()` for now because it's more readable and robust.

### List keys and values

`.keys()` gives you all the keys in the dictionary

`.values()` gives you all the values in the dictionary

`.items()` gives you all the entries in the dictionary

Each of these is iterable.

```{code-cell} ipython3
d
```

```{code-cell} ipython3
# list all the keys in the dictionary
d.keys()
```

```{code-cell} ipython3
# list all the values in the dictionary
d.values()
```

```{code-cell} ipython3
# list all the key-value pairs in the dictionary
d.items()
```

```{code-cell} ipython3
# this means you can iterate through the keys/values
for key in d.keys():
    print(key, d.get(key))
```

```{code-cell} ipython3
# iterate through the items
for key, value in d.items():
    print(f'{key} is associated with the value {value}')
```

### Check if a key is in a dictionary

```{code-cell} ipython3
d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon'
}
print('h' in d)
```

Can only use `in` operator with keys.

You can also do this with `.get()`!

```{code-cell} ipython3
# retrieve value for h, if it's not found, return False
d.get("h", False)
```

**PRACTICE**: how do you check if the key "c" is in the dictionary `d`?

```{code-cell} ipython3
# your code here
```

### Reverse look up keys from values: YOU CAN'T! Not really...

Dictionaries are very powerful transformations of your data that make it REALLY easy to do a specific kind of operation, but lock you out of doing other things. So design the structure of the dictionary carefully. For example, if you make an index, and find that you actually care a lot about grabbing the top N words, you probably want to map counts (as keys) to words (as values), not words to counts.

```{code-cell} ipython3
s = "she sells sea shells by the sea shore in the sea and the shells and the sea sea sea"

d = {} # define a dictionary to hold the index
# go through word by word
for word in s.split():
  # get the current count for the word, default to 0 if we haven't seen it
  current_count = d.get(word, 0)
  # update the count
  new_count = current_count + 1
  # update the dictionary with the word and count
  d.update({word: new_count})

d
```

Could try to invert it, but....

```{code-cell} ipython3
def reverse_dictionary(d):
    return {v: k for k, v in d.items()}
```

You actually lose information, because remember: keys are unique! No duplicates! So we lose one of our "2" entries.

```{code-cell} ipython3
d_invert = reverse_dictionary(d)
d_invert
```

```{code-cell} ipython3
d_invert = {}
for word, count in d.items():
    words = d_invert.get(count, []) # get the current list of words associated with this count
    words.append(word)
    d_invert.update({count: words})
d_invert
```

### Practice: Code Tracing with Dictionaries

Predict the output of each code snippet before running the cell!

#### Trace 1

```{code-cell} ipython3
:tags: [remove-output]

d = {"x": 10, "y": 20, "z": 30}
print(d["y"])
```

- A) `20`
- B) `"y"`
- C) `10`
- D) `1`

````{admonition} Answer:
:class: toggle

**A) `20`**

`d["y"]` retrieves the value associated with the key `"y"`, which is `20`.
````

#### Trace 2

```{code-cell} ipython3
:tags: [remove-output]

d = {"a": 1, "b": 2}
d["c"] = 3
d["a"] = 99
print(d)
print(len(d))
```

- A) `{'a': 1, 'b': 2, 'c': 3}` then `3`
- B) `{'a': 99, 'b': 2, 'c': 3}` then `3`
- C) `{'a': 99, 'b': 2}` then `2`
- D) `{'a': 1, 'a': 99, 'b': 2, 'c': 3}` then `4`

````{admonition} Answer:
:class: toggle

**B) `{'a': 99, 'b': 2, 'c': 3}` then `3`**

`d["c"] = 3` adds a new entry. `d["a"] = 99` *updates* the existing key `"a"` (keys are unique — you can't have two `"a"` entries). So the dict has 3 entries.
````

#### Trace 3

```{code-cell} ipython3
:tags: [remove-output]

d = {"name": "Joel", "age": 30}
result = d.get("email", "not found")
print(result)
print(len(d))
```

- A) `None` then `2`
- B) `"not found"` then `2`
- C) `"not found"` then `3`
- D) KeyError

````{admonition} Answer:
:class: toggle

**B) `"not found"` then `2`**

`"email"` is not a key in `d`, so `.get()` returns the default value `"not found"`. Importantly, `.get()` does **not** add the key to the dictionary — `d` still has only 2 entries.
````

<!-- #### Trace 4

```{code-cell} ipython3
:tags: [remove-output]

d = {"a": 1, "b": 2, "c": 3}
keys = []
for k in d.keys():
    keys.append(k)
print(keys)
```

- A) `[1, 2, 3]`
- B) `['a', 'b', 'c']`
- C) `[('a', 1), ('b', 2), ('c', 3)]`
- D) `{'a', 'b', 'c'}`

````{admonition} Answer:
:class: toggle

**B) `['a', 'b', 'c']`**

`.keys()` gives you the keys (not the values). The loop appends each key to the list. A is what you'd get from `.values()`, and C is what you'd get from `.items()`.
````

#### Trace 5

```{code-cell} ipython3
:tags: [remove-output]

d = {}
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
for word in words:
    count = d.get(word, 0)
    d[word] = count + 1
print(d)
print(d.get("cat"))
```

- A) `{'cat': 1, 'dog': 1, 'bird': 1}` then `1`
- B) `{'cat': 3, 'dog': 2, 'bird': 1}` then `3`
- C) `{'cat': 3, 'dog': 2, 'cat': 3, 'bird': 1, 'dog': 2, 'cat': 3}` then `3`
- D) `{'cat': 2, 'dog': 1, 'bird': 1}` then `2`

````{admonition} Answer:
:class: toggle

**B) `{'cat': 3, 'dog': 2, 'bird': 1}` then `3`**

This is the **word count / indexing pattern**. Each time we see a word, we get its current count (defaulting to 0), add 1, and update. "cat" appears 3 times, "dog" 2 times, "bird" 1 time. Keys are unique so there's only one entry per word.
```` -->

#### Trace 4

```{code-cell} ipython3
:tags: [remove-output]

d = {"a": [1, 2], "b": [3]}
d["a"].append(3)
d["c"] = []
d["c"].append(7)
print(d)
```

- A) `{'a': [1, 2], 'b': [3], 'c': [7]}`
- B) `{'a': [1, 2, 3], 'b': [3], 'c': [7]}`
- C) `{'a': [3], 'b': [3], 'c': [7]}`
- D) `{'a': [1, 2, 3], 'b': [3], 'c': []}`

````{admonition} Answer:
:class: toggle

**B) `{'a': [1, 2, 3], 'b': [3], 'c': [7]}`**

Dictionary values can be lists (or any other type). `d["a"].append(3)` gets the list `[1, 2]` and appends `3` to it — lists are mutable, so this modifies the list in place. `d["c"] = []` creates a new key with an empty list, then `.append(7)` adds to it.
````

#### Trace 5

```{code-cell} ipython3
:tags: [remove-output]

d = {"x": 10, "y": 20}
d.update({"y": 50, "z": 30})
print(d)
print("z" in d)
print(30 in d)
```

- A) `{'x': 10, 'y': 50, 'z': 30}` then `True` then `True`
- B) `{'x': 10, 'y': 50, 'z': 30}` then `True` then `False`
- C) `{'x': 10, 'y': 20, 'z': 30}` then `True` then `False`
- D) `{'x': 10, 'y': 20, 'y': 50, 'z': 30}` then `True` then `True`

````{admonition} Answer:
:class: toggle

**B) `{'x': 10, 'y': 50, 'z': 30}` then `True` then `False`**

`.update()` adds `"z": 30` and updates `"y"` from 20 to 50. `"z" in d` checks if `"z"` is a **key** → `True`. `30 in d` checks if `30` is a **key** → `False` (30 is a *value*, not a key). The `in` operator only checks keys!
````

<!-- #### Trace 6

```{code-cell} ipython3
:tags: [remove-output]

inventory = {"apples": 5, "bananas": 0, "oranges": 3}
in_stock = []
for item, qty in inventory.items():
    if qty > 0:
        in_stock.append(item)
print(in_stock)
```

- A) `['apples', 'oranges']`
- B) `['apples', 'bananas', 'oranges']`
- C) `[5, 3]`
- D) `[('apples', 5), ('oranges', 3)]`

````{admonition} Answer:
:class: toggle

**A) `['apples', 'oranges']`**

`.items()` gives key-value pairs. The loop unpacks each pair into `item` and `qty`. Only items with `qty > 0` are appended — so bananas (qty 0) is skipped. We append `item` (the key/name), not `qty`.
```` -->

<!-- #### Trace 9

```{code-cell} ipython3
:tags: [remove-output]

d = {"a": "hello", "b": "world"}
for key in d:
    d[key] = d[key].upper()
print(d)
```

- A) `{'a': 'hello', 'b': 'world'}`
- B) `{'A': 'HELLO', 'B': 'WORLD'}`
- C) `{'a': 'HELLO', 'b': 'WORLD'}`
- D) `{'a': 'Hello', 'b': 'World'}`

````{admonition} Answer:
:class: toggle

**C) `{'a': 'HELLO', 'b': 'WORLD'}`**

Iterating `for key in d` loops through the **keys**. Each iteration updates the *value* with its uppercase version. The keys themselves are not changed — only the values are reassigned. (Note: since strings are immutable, `d[key].upper()` returns a new string, which we then assign back to `d[key]`.)
```` -->

<!-- #### Trace 10

```{code-cell} ipython3
:tags: [remove-output]

grades = {}
entries = ["Joel:A", "Sarah:B", "Joel:A+", "Rony:A"]
for entry in entries:
    name, grade = entry.split(":")
    grades[name] = grade
print(grades)
print(len(grades))
```

- A) `{'Joel': 'A', 'Sarah': 'B', 'Rony': 'A'}` then `3`
- B) `{'Joel': 'A+', 'Sarah': 'B', 'Rony': 'A'}` then `3`
- C) `{'Joel': 'A', 'Sarah': 'B', 'Joel': 'A+', 'Rony': 'A'}` then `4`
- D) `{'Joel': ['A', 'A+'], 'Sarah': ['B'], 'Rony': ['A']}` then `3`

````{admonition} Answer:
:class: toggle

**B) `{'Joel': 'A+', 'Sarah': 'B', 'Rony': 'A'}` then `3`**

Joel appears twice. The second assignment `grades["Joel"] = "A+"` *overwrites* the first (`"A"`). Keys are unique — the last value wins. If you wanted to keep both grades, you'd need to use a list as the value (like in option D), but that requires the `.get()` + append pattern.
```` -->

<!-- ### Practice: Dictionary Operations

#### P1: Create a dictionary from two lists

Given a list of student names and a list of their scores, create a dictionary that maps each name to their score.

```{code-cell} ipython3
names = ["Joel", "Sarah", "Rony", "Kacie"]
scores = [81, 95, 98, 88]
grades = {}

# your code here
```

`````{admonition} Answer:
:class: toggle

```python
names = ["Joel", "Sarah", "Rony", "Kacie"]
scores = [81, 95, 98, 88]
grades = {}
for i in range(len(names)):
    grades[names[i]] = scores[i]
grades  # {'Joel': 81, 'Sarah': 95, 'Rony': 98, 'Kacie': 88}
```
`````

#### P2: Look up and format

Given a dictionary of course codes to course names, print a formatted line for each: `"{code}: {name}"`.

```{code-cell} ipython3
courses = {
    "INST126": "Intro to Programming",
    "INST201": "Intro to Information Science",
    "INST326": "Object-Oriented Programming"
}

# your code here
```

`````{admonition} Answer:
:class: toggle

```python
courses = {
    "INST126": "Intro to Programming",
    "INST201": "Intro to Information Science",
    "INST326": "Object-Oriented Programming"
}
for code, name in courses.items():
    print(f"{code}: {name}")
```
`````

#### P3: Count occurrences

Given a list of colors, build a dictionary that counts how many times each color appears.

```{code-cell} ipython3
colors = ["red", "blue", "red", "green", "blue", "red", "green", "green", "blue", "red"]
color_counts = {}

# your code here
```

`````{admonition} Answer:
:class: toggle

```python
colors = ["red", "blue", "red", "green", "blue", "red", "green", "green", "blue", "red"]
color_counts = {}
for color in colors:
    color_counts[color] = color_counts.get(color, 0) + 1
color_counts  # {'red': 4, 'blue': 3, 'green': 3}
```
`````

#### P4: Safe lookup with default

Given a dictionary of stock prices and a list of ticker symbols to look up, print the price for each. If the ticker isn't in the dictionary, print `"TICKER: not available"`.

```{code-cell} ipython3
prices = {"AAPL": 175.50, "GOOG": 140.25, "MSFT": 380.00}
lookups = ["AAPL", "TSLA", "GOOG", "AMZN"]

# your code here
```

`````{admonition} Answer:
:class: toggle

```python
prices = {"AAPL": 175.50, "GOOG": 140.25, "MSFT": 380.00}
lookups = ["AAPL", "TSLA", "GOOG", "AMZN"]
for ticker in lookups:
    price = prices.get(ticker, "not available")
    print(f"{ticker}: {price}")
```
`````

#### P5: Update inventory

You have a current inventory and a shipment of new items. Update the inventory by adding the shipment quantities to the existing quantities. If an item in the shipment isn't in the inventory yet, add it.

```{code-cell} ipython3
inventory = {"apples": 10, "bananas": 5, "oranges": 8}
shipment = {"bananas": 12, "grapes": 20, "apples": 5}

# your code here
```

`````{admonition} Answer:
:class: toggle

```python
inventory = {"apples": 10, "bananas": 5, "oranges": 8}
shipment = {"bananas": 12, "grapes": 20, "apples": 5}
for item, qty in shipment.items():
    current = inventory.get(item, 0)
    inventory[item] = current + qty
inventory  # {'apples': 15, 'bananas': 17, 'oranges': 8, 'grapes': 20}
```
`````

#### P6: Filter a dictionary

Given a dictionary of student names to scores, build a new dictionary containing only the students who scored 90 or above.

```{code-cell} ipython3
all_scores = {"Joel": 81, "Sarah": 95, "Rony": 98, "Kacie": 88, "Pat": 92, "Miles": 73}
high_scores = {}

# your code here
```

`````{admonition} Answer:
:class: toggle

```python
all_scores = {"Joel": 81, "Sarah": 95, "Rony": 98, "Kacie": 88, "Pat": 92, "Miles": 73}
high_scores = {}
for name, score in all_scores.items():
    if score >= 90:
        high_scores[name] = score
high_scores  # {'Sarah': 95, 'Rony': 98, 'Pat': 92}
```
`````

#### P7: Group items by category

Given a list of strings in the format `"item:category"`, build a dictionary that maps each category to a list of items in that category.

```{code-cell} ipython3
items = ["apple:fruit", "carrot:vegetable", "banana:fruit", "broccoli:vegetable", "grape:fruit", "spinach:vegetable"]
groups = {}

# your code here
```

`````{admonition} Answer:
:class: toggle

```python
items = ["apple:fruit", "carrot:vegetable", "banana:fruit", "broccoli:vegetable", "grape:fruit", "spinach:vegetable"]
groups = {}
for item_str in items:
    item, category = item_str.split(":")
    current = groups.get(category, [])
    current.append(item)
    groups[category] = current
groups  # {'fruit': ['apple', 'banana', 'grape'], 'vegetable': ['carrot', 'broccoli', 'spinach']}
```
`````

#### P8: Invert a dictionary (values become keys)

Given a dictionary mapping student names to their assigned lab section (A, B, or C), build a new dictionary that maps each section to a list of student names.

```{code-cell} ipython3
assignments = {"Joel": "A", "Sarah": "B", "Rony": "A", "Kacie": "C", "Pat": "B", "Miles": "A"}
sections = {}

# your code here
```

`````{admonition} Answer:
:class: toggle

```python
assignments = {"Joel": "A", "Sarah": "B", "Rony": "A", "Kacie": "C", "Pat": "B", "Miles": "A"}
sections = {}
for name, section in assignments.items():
    students = sections.get(section, [])
    students.append(name)
    sections[section] = students
sections  # {'A': ['Joel', 'Rony', 'Miles'], 'B': ['Sarah', 'Pat'], 'C': ['Kacie']}
```
`````

#### P9: Parse and index email domains

Given a list of email addresses, build a dictionary that maps each domain (the part after `@`) to a list of usernames (the part before `@`).

```{code-cell} ipython3
emails = ["joel@umd.edu", "sarah@gmail.com", "rony@umd.edu", "pat@gmail.com", "kacie@umd.edu"]
domain_index = {}

# your code here
```

`````{admonition} Answer:
:class: toggle

```python
emails = ["joel@umd.edu", "sarah@gmail.com", "rony@umd.edu", "pat@gmail.com", "kacie@umd.edu"]
domain_index = {}
for email in emails:
    username, domain = email.split("@")
    users = domain_index.get(domain, [])
    users.append(username)
    domain_index[domain] = users
domain_index  # {'umd.edu': ['joel', 'rony', 'kacie'], 'gmail.com': ['sarah', 'pat']}
```
`````

#### P10: Build a report from nested data

Given a dictionary of students where each value is another dictionary with `"score"` and `"section"`, print a report line for each student: `"{name} (Section {section}): {score}/100"` and compute the overall average score.

```{code-cell} ipython3
students = {
    "Joel": {"score": 81, "section": "A"},
    "Sarah": {"score": 95, "section": "B"},
    "Rony": {"score": 98, "section": "A"},
    "Kacie": {"score": 88, "section": "C"}
}

# your code here
```

`````{admonition} Answer:
:class: toggle

```python
students = {
    "Joel": {"score": 81, "section": "A"},
    "Sarah": {"score": 95, "section": "B"},
    "Rony": {"score": 98, "section": "A"},
    "Kacie": {"score": 88, "section": "C"}
}
total = 0
count = 0
for name, info in students.items():
    score = info["score"]
    section = info["section"]
    print(f"{name} (Section {section}): {score}/100")
    total += score
    count += 1
print(f"Average: {total / count:.1f}/100")
```
````` -->

## Working with nested dictionaries

So far, most of our dictionary values have been simple: a string, a number, a boolean. But one of the most powerful things about dictionaries is that **values can be dictionaries too**. This lets us model structured data — things with multiple attributes — in a very natural way.

### Why nest?

Think about a student record. You could try to cram everything into a flat dictionary:

```{code-cell} ipython3
# flat: one key per piece of info
student_joel_name = "Joel"
student_joel_major = "Info Sci"
student_joel_year = "Senior"
# this gets messy fast with multiple students...
```

Or you could use a nested dictionary where each student maps to a dictionary of their attributes:

```{code-cell} ipython3
students = {
    "joel": {
        "major": "Info Sci",
        "year": "Senior",
        "gpa": 3.5
    },
    "sarah": {
        "major": "Computer Science",
        "year": "Junior",
        "gpa": 3.8
    }
}
```

This is much cleaner. Each student has a "record" of attributes, and we can look up any attribute for any student.

### Reading nested values: chain the lookups

To get a value from a nested dictionary, you **chain** two lookups — first the outer key, then the inner key.

```{code-cell} ipython3
# get Joel's major
print(students["joel"]["major"])
```

#### Chaining: a familiar idea

This idea of chaining should feel familiar from strings! Remember how we could chain string methods like `.strip().lower().replace("#", "")`? That worked because each method returned a string, so you could immediately call another method on it.

The same principle is at work here: **each operation returns something, and you can immediately do another operation on that result**.

- `"  Hello ".strip()` → returns a string → `.lower()` works on it
- `email.split("@")[0]` → `.split()` returns a list → `[0]` indexes into it
- `students["joel"]["major"]` → `students["joel"]` returns a dictionary → `["major"]` looks up a key in it

It's the same pattern every time: **the result of one operation becomes the input to the next**.

#### Breaking it into steps

If chaining feels confusing, you can always break it into separate steps — it does the exact same thing:

```{code-cell} ipython3
# step 1: get Joel's record (this gives us a dictionary)
joel_record = students["joel"]
print(type(joel_record))
print(joel_record)

# step 2: get the major from that dictionary
print(joel_record["major"])
```

The one-liner `students["joel"]["major"]` just combines both steps. Think of it as reading left to right: "from `students`, get `"joel"`, then from *that*, get `"major"`."

#### Safe chaining with `.get()`

You can also chain `.get()` calls for safer access:

```{code-cell} ipython3
# safe access with .get()
print(students.get("joel", {}).get("major", "unknown"))

# if the outer key doesn't exist, .get() returns {},
# and then .get("major") on {} returns "unknown"
print(students.get("pat", {}).get("major", "unknown"))
```

This works because `.get("pat", {})` returns an empty dictionary `{}` when `"pat"` isn't found, and then `.get("major", "unknown")` on that empty dictionary returns `"unknown"`. Each step produces something the next step can work with.

### Updating nested values

To update a value inside a nested dictionary, chain the lookups on the left side of the assignment:

```{code-cell} ipython3
# Joel's GPA went up
students["joel"]["gpa"] = 3.6
print(students["joel"])
```

```{code-cell} ipython3
# Sarah changed her major
students["sarah"]["major"] = "Data Science"
print(students["sarah"])
```

### Adding a new entry to the outer dictionary

To add a whole new record, assign a new dictionary to a new outer key:

```{code-cell} ipython3
# add a new student
students["rony"] = {
    "major": "Info Sci",
    "year": "Senior",
    "gpa": 3.9
}
print(students["rony"])
```

### Adding a new field to an existing inner dictionary

You can also add new keys to an inner dictionary — it's just a regular dictionary, after all:

```{code-cell} ipython3
# add an email field to Joel's record
students["joel"]["email"] = "joel@umd.edu"
print(students["joel"])
```

### A real-world example: course catalog

Let's put this together with a more realistic example. Here's a course catalog where each course has multiple attributes:

```{code-cell} ipython3
catalog = {
    "INST126": {
        "title": "Intro to Programming",
        "instructor": "Joel",
        "credits": 3,
        "prereqs": []
    },
    "INST326": {
        "title": "OO Programming",
        "instructor": "Pat",
        "credits": 3,
        "prereqs": ["INST126"]
    },
    "INST414": {
        "title": "Data Science",
        "instructor": "Sarah",
        "credits": 3,
        "prereqs": ["INST126", "INST201"]
    }
}
```

Now we can answer questions by chaining lookups:

```{code-cell} ipython3
# who teaches INST326?
print(catalog["INST326"]["instructor"])
```

```{code-cell} ipython3
# what are the prereqs for INST414?
print(catalog["INST414"]["prereqs"])
```

```{code-cell} ipython3
# does INST126 have any prereqs?
prereqs = catalog["INST126"]["prereqs"]
if len(prereqs) == 0:
    print("INST126 has no prerequisites")
else:
    print(f"INST126 requires: {prereqs}")
```

And we can update it:

```{code-cell} ipython3
# Pat is no longer teaching INST326, Rony is
catalog["INST326"]["instructor"] = "Rony"

# INST326 added a new prereq
catalog["INST326"]["prereqs"].append("INST201")

print(catalog["INST326"])
```

Notice that last line: `catalog["INST326"]["prereqs"]` gives us a **list**, and since lists are mutable, we can `.append()` to it directly. This is the power of nesting — the inner values follow all the rules of their own type.

### Common pattern: building nested dictionaries from data

Often you'll start with raw data (like a list of strings) and need to build up a nested dictionary. The pattern is the same as building a flat dictionary, but the value you create or update is itself a dictionary (or a list inside a dictionary).

```{code-cell} ipython3
# raw roster data: "name,section,score"
roster_data = [
    "Joel,A,81",
    "Sarah,B,95",
    "Rony,A,98",
    "Kacie,C,88"
]

roster = {}
for entry in roster_data:
    name, section, score = entry.split(",")
    roster[name] = {
        "section": section,
        "score": int(score)
    }

print(roster)
```

```{code-cell} ipython3
# now we can look up any student's info
print(f"Rony is in section {roster['Rony']['section']} with score {roster['Rony']['score']}")
```

### Summary

Working with nested dictionaries follows the same rules as flat dictionaries — you just chain the operations:

| Operation | Flat | Nested |
|---|---|---|
| Read | `d["key"]` | `d["outer"]["inner"]` |
| Update | `d["key"] = val` | `d["outer"]["inner"] = val` |
| Add outer entry | `d["new_key"] = val` | `d["new_key"] = {"inner": val}` |
| Add inner field | n/a | `d["outer"]["new_field"] = val` |
| Safe read | `d.get("key", default)` | `d.get("outer", {}).get("inner", default)` |

## Practice: Dictionary Scenarios

For each scenario, start by creating the dictionary, then complete the retrieval and update operations.

### Scenario 1: Gradebook (basic)

You're building a simple gradebook that maps student names to their current grade (a single letter grade).

#### Setup

Create a dictionary called `gradebook` with the following entries:

| Student | Grade |
|---|---|
| Joel | B |
| Sarah | A |
| Rony | A+ |
| Kacie | B+ |
| Miles | C |

```{code-cell} ipython3
# create the gradebook dictionary here
```

#### Retrieve

**R1.** Print Joel's grade.

```{code-cell} ipython3
# your code here
```

**R2.** Check if "Pat" is in the gradebook. If so, print their grade; otherwise print `"Pat is not in the gradebook"`.

```{code-cell} ipython3
# your code here
```

**R3.** Use `.get()` to look up "Zara" in the gradebook. If she's not there, print `"Zara: no grade on file"`.

```{code-cell} ipython3
# your code here
```

#### Update

**U1.** Miles turned in extra credit — update his grade to `"B-"`.

```{code-cell} ipython3
# your code here
```

**U2.** A new student, Pat, joined the class with a grade of `"B"`. Add them to the gradebook.

```{code-cell} ipython3
# your code here
```

**U3.** Sarah and Rony both got final grade adjustments: Sarah is now `"A-"` and Rony is now `"A"`. Update both in a single operation.

```{code-cell} ipython3
# your code here
```

---

### Scenario 2: Restaurant menu (basic)

You're modeling a simple restaurant menu that maps dish names to their price.

#### Setup

Create a dictionary called `menu` with the following entries:

| Dish | Price |
|---|---|
| burger | 12.99 |
| salad | 9.50 |
| pasta | 14.75 |
| soup | 7.25 |
| fries | 5.00 |

```{code-cell} ipython3
# create the menu dictionary here
```

#### Retrieve

**R1.** A customer asks how much the pasta costs. Print the price formatted as: `"pasta: $14.75"`.

```{code-cell} ipython3
# your code here
```

**R2.** A customer wants to know the price of fries. Print it formatted as `"fries: $5.00"`.

```{code-cell} ipython3
# your code here
```

**R3.** A customer asks for "milkshake". Use `.get()` with a default to print `"milkshake: not on the menu"` if it doesn't exist.

```{code-cell} ipython3
# your code here
```

#### Update

**U1.** The soup price increased to `$8.50`. Update the menu.

```{code-cell} ipython3
# your code here
```

**U2.** Add a new item: `"tacos"` at `$11.25`.

```{code-cell} ipython3
# your code here
```

**U3.** The burger and pasta prices both went up by $1.00. Update both in a single `.update()` call.

```{code-cell} ipython3
# your code here
```

---

### Scenario 3: Social media profile (basic)

You're modeling a simple social media profile where each key is a profile field.

#### Setup

Create a dictionary called `profile` with the following entries:

| Field | Value |
|---|---|
| username | terp_coder |
| display_name | Joel C. |
| followers | 142 |
| bio | INST126 instructor |
| verified | False |

```{code-cell} ipython3
# create the profile dictionary here
```

#### Retrieve

**R1.** Print the display name and bio in the format: `"{display_name} — {bio}"`.

```{code-cell} ipython3
# your code here
```

**R2.** Check if the account is verified. Print `"Verified account"` or `"Not verified"` accordingly.

```{code-cell} ipython3
# your code here
```

**R3.** Print the follower count formatted as: `"terp_coder has 142 followers"` (use the values from the dictionary, don't hardcode them).

```{code-cell} ipython3
# your code here
```

#### Update

**U1.** The user gained 8 new followers. Update the follower count (don't just hardcode 150 — add 8 to the current value).

```{code-cell} ipython3
# your code here
```

**U2.** The user changed their bio to `"Python enthusiast | UMD"`. Update it.

```{code-cell} ipython3
# your code here
```

**U3.** The account got verified, and they also want to add a new field `"website"` with the value `"https://joelchan.me"`. Do both updates at once.

```{code-cell} ipython3
# your code here
```

---

### Scenario 4: Course directory (nested)

You're building a course directory where each course code maps to a dictionary of course details.

#### Setup

Create a dictionary called `courses` with the following structure:

```
courses = {
    "INST126": {"title": "Intro to Programming", "instructor": "Joel", "capacity": 40, "enrolled": 38},
    "INST201": {"title": "Intro to Info Science", "instructor": "Sarah", "capacity": 35, "enrolled": 35},
    "INST326": {"title": "OO Programming", "instructor": "Pat", "capacity": 30, "enrolled": 22}
}
```

```{code-cell} ipython3
# create the courses dictionary here
```

#### Retrieve

**R1.** Print the instructor for INST126.

```{code-cell} ipython3
# your code here
```

**R2.** Print how many open seats INST126 has (capacity minus enrolled), formatted as: `"INST126: {n} seats available"`.

```{code-cell} ipython3
# your code here
```

**R3.** A student wants to know the title and instructor for INST326. Print: `"INST326: OO Programming (taught by Pat)"`.

```{code-cell} ipython3
# your code here
```

#### Update

**U1.** 3 more students enrolled in INST326. Update the enrolled count.

```{code-cell} ipython3
# your code here
```

**U2.** INST201 got a new instructor: "Rony". Update it.

```{code-cell} ipython3
# your code here
```

**U3.** Add a new course: `"INST314"` with title `"Statistics"`, instructor `"Kacie"`, capacity `25`, and enrolled `0`.

```{code-cell} ipython3
# your code here
```

---

### Scenario 5: Streaming catalog (nested)

You're modeling a simple streaming catalog where each show title maps to a dictionary of details.

#### Setup

Create a dictionary called `catalog` with the following structure:

```
catalog = {
    "Stranger Things": {"genre": "sci-fi", "seasons": 4, "rating": 8.7},
    "The Office": {"genre": "comedy", "seasons": 9, "rating": 8.9},
    "Breaking Bad": {"genre": "drama", "seasons": 5, "rating": 9.5},
    "Ted Lasso": {"genre": "comedy", "seasons": 3, "rating": 8.8}
}
```

```{code-cell} ipython3
# create the catalog dictionary here
```

#### Retrieve

**R1.** Print the rating of Breaking Bad.

```{code-cell} ipython3
# your code here
```

**R2.** Print how many seasons The Office has, formatted as: `"The Office: 9 seasons"`.

```{code-cell} ipython3
# your code here
```

**R3.** Check if "Wednesday" is in the catalog. Print `"Wednesday is available"` or `"Wednesday is not in the catalog"`.

```{code-cell} ipython3
# your code here
```

#### Update

**U1.** Stranger Things released a new season. Update its season count to 5.

```{code-cell} ipython3
# your code here
```

**U2.** After the new season, the rating for Stranger Things was updated to `8.9`. Update it.

```{code-cell} ipython3
# your code here
```

**U3.** Add a new show: `"Wednesday"` with genre `"comedy"`, seasons `1`, and rating `8.1`.

```{code-cell} ipython3
# your code here
```

---

### Scenario 6: Website config (nested)

You're working with a website configuration dictionary that stores settings for different sections of the site.

#### Setup

Create a dictionary called `config` with the following structure:

```
config = {
    "homepage": {"title": "Welcome", "show_banner": True, "max_posts": 10},
    "blog": {"title": "Our Blog", "show_banner": False, "max_posts": 25},
    "about": {"title": "About Us", "show_banner": True, "max_posts": 0}
}
```

```{code-cell} ipython3
# create the config dictionary here
```

#### Retrieve

**R1.** Print the title of the blog page.

```{code-cell} ipython3
# your code here
```

**R2.** Check whether the blog page has the banner enabled. Print `"Blog banner: on"` or `"Blog banner: off"` accordingly.

```{code-cell} ipython3
# your code here
```

**R3.** Print the homepage title and max posts, formatted as: `"Homepage: 'Welcome' (max 10 posts)"`.

```{code-cell} ipython3
# your code here
```

#### Update

**U1.** Enable the banner on the blog page.

```{code-cell} ipython3
# your code here
```

**U2.** The homepage should now show a max of 15 posts instead of 10. Update it.

```{code-cell} ipython3
# your code here
```

**U3.** Add a new page: `"contact"` with title `"Contact Us"`, `show_banner` set to `False`, and `max_posts` set to `0`.

```{code-cell} ipython3
# your code here
```

## Dictionary Application: Indexing

Now that we have the dictionary data structure, we can apply it in a program that can *create* an index.

### Example

Here's an example from above that takes a list of book chapter strings and a list of key concepts, and produces an index that maps key concepts to chapters.

```{code-cell} ipython3
# how to know which chapters talk about strings? or debugging?
book = [
  "Chapter 1: talks about strings and how they have the property of immutability also some basic debugging",
  "Chapter 2: continues talking about advanced methods for strings and also introduces the concept of functions",
  "Chapter 3: discusses iteration and lists and also debugging",
]
```

```{code-cell} ipython3
# define what we want to index as keys
concepts = ['strings', 'debugging', "lists", "iteration"]

# make a dictionary to hold the index
index = {}

# go through every chapter
for chapter in book:

    # split into chapter and descr based on the colon
    chapter, descr = chapter.split(":")

    # index the concepts

    # for every concept we care about
    for keyconcept in concepts:
        # check if it's in this chapter descr
        if keyconcept in descr:
            # if so, get the current list of chapters associated with this keyconcept
            chs = index.get(keyconcept, [])
            # then update the list of chapters
            # if we haven't seen the chapter
            if chapter not in chs:
                chs.append(chapter)
            # and update the index to map the keyconcept to the updated list of assoc. chapters
            index.update({keyconcept: chs})
index
```

What dictionary concepts do you recognize?

### The indexing pattern

Here's the generic structure of an indexing pattern

```
# create an empty dictionary to hold the index

# for every item in a list of things you want to index

    # (optional: parse out the keys and values you want to index from the item)

    # get the current value associated with the key in the index

    # update the value

    # update the index with the key and its updated value
```

Let's look at a super simple example: making a **word count index**.

We'll take in a list of words, and produce an index that maps words as `keys` to counts of occurrences as `values`.

```{code-cell} ipython3
# the thing we want to index
word_list = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore', 'in', 'the', 'sea', 'and', 'the', 'shells', 'and', 'the', 'sea', 'sea', 'sea']

# create an empty dictionary to hold the index
word_counts = {}

# for every item in a list of things you want to index
for word in word_list:

    # (optional: parse out the keys and values you want to index from the item)
    # we don't need this step

    # get the current value associated with the key in the index
    # here, we use .get(), and have a default count of 0 if the key isn't yet in the index
    count = word_counts.get(word, 0)

    # update the value
    count += 1

    # update the index with the key and its updated value
    word_counts.update({word: count})

word_counts
```

### Practice: index grade counts

Practice! Test your understanding by adapting the above code to count how many times each grade was earned in a course.

```{code-cell} ipython3
grades_counts = {}
```

```{code-cell} ipython3
# your code here
```

### Practice: which words are n characters long?

Now let's extend this a bit. We'll modify the first program to index word lengths: we want an index that can tell us "what words in the list were 2 characters long, or 5 characters long?"

```{code-cell} ipython3
# the thing we want to index
word_list = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore', 'in', 'the', 'sea', 'and', 'the', 'shells', 'and', 'the', 'sea', 'sea', 'sea']

# your code here
```

### Practice: counts of email addresses from email records

Let's index how many times we got emails from which email addresses!

```{code-cell} ipython3
email_records = ['From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008',
 'From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008',
 'From zqian@umich.edu Fri Jan  4 16:10:39 2008',
 'From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008',
 'From zqian@umich.edu Fri Jan  4 15:03:18 2008',
 'From rjlowe@iupui.edu Fri Jan  4 14:50:18 2008',
 'From cwen@iupui.edu Fri Jan  4 11:37:30 2008',
 'From cwen@iupui.edu Fri Jan  4 11:35:08 2008',
 'From gsilver@umich.edu Fri Jan  4 11:12:37 2008',
 'From gsilver@umich.edu Fri Jan  4 11:11:52 2008',
 'From zqian@umich.edu Fri Jan  4 11:11:03 2008',
 'From gsilver@umich.edu Fri Jan  4 11:10:22 2008',
 'From wagnermr@iupui.edu Fri Jan  4 10:38:42 2008',
 'From zqian@umich.edu Fri Jan  4 10:17:43 2008',
 'From antranig@caret.cam.ac.uk Fri Jan  4 10:04:14 2008',
 'From gopal.ramasammycook@gmail.com Fri Jan  4 09:05:31 2008',
 'From david.horwitz@uct.ac.za Fri Jan  4 07:02:32 2008',
 'From david.horwitz@uct.ac.za Fri Jan  4 06:08:27 2008',
 'From david.horwitz@uct.ac.za Fri Jan  4 04:49:08 2008',
 'From david.horwitz@uct.ac.za Fri Jan  4 04:33:44 2008',
 'From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008',
 'From louis@media.berkeley.edu Thu Jan  3 19:51:21 2008',
 'From louis@media.berkeley.edu Thu Jan  3 17:18:23 2008',
 'From ray@media.berkeley.edu Thu Jan  3 17:07:00 2008',
 'From cwen@iupui.edu Thu Jan  3 16:34:40 2008',
 'From cwen@iupui.edu Thu Jan  3 16:29:07 2008',
 'From cwen@iupui.edu Thu Jan  3 16:23:48 2008']

# your code here
```

### Practice: map email addresses to email records

Now modify the previous program to map email **records** (as values) to email addresses (as keys). We want to ask questions like "can I see the emails I got from `cwen@iupui.edu`?"

```{code-cell} ipython3
email_records = ['From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008',
 'From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008',
 'From zqian@umich.edu Fri Jan  4 16:10:39 2008',
 'From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008',
 'From zqian@umich.edu Fri Jan  4 15:03:18 2008',
 'From rjlowe@iupui.edu Fri Jan  4 14:50:18 2008',
 'From cwen@iupui.edu Fri Jan  4 11:37:30 2008',
 'From cwen@iupui.edu Fri Jan  4 11:35:08 2008',
 'From gsilver@umich.edu Fri Jan  4 11:12:37 2008',
 'From gsilver@umich.edu Fri Jan  4 11:11:52 2008',
 'From zqian@umich.edu Fri Jan  4 11:11:03 2008',
 'From gsilver@umich.edu Fri Jan  4 11:10:22 2008',
 'From wagnermr@iupui.edu Fri Jan  4 10:38:42 2008',
 'From zqian@umich.edu Fri Jan  4 10:17:43 2008',
 'From antranig@caret.cam.ac.uk Fri Jan  4 10:04:14 2008',
 'From gopal.ramasammycook@gmail.com Fri Jan  4 09:05:31 2008',
 'From david.horwitz@uct.ac.za Fri Jan  4 07:02:32 2008',
 'From david.horwitz@uct.ac.za Fri Jan  4 06:08:27 2008',
 'From david.horwitz@uct.ac.za Fri Jan  4 04:49:08 2008',
 'From david.horwitz@uct.ac.za Fri Jan  4 04:33:44 2008',
 'From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008',
 'From louis@media.berkeley.edu Thu Jan  3 19:51:21 2008',
 'From louis@media.berkeley.edu Thu Jan  3 17:18:23 2008',
 'From ray@media.berkeley.edu Thu Jan  3 17:07:00 2008',
 'From cwen@iupui.edu Thu Jan  3 16:34:40 2008',
 'From cwen@iupui.edu Thu Jan  3 16:29:07 2008',
 'From cwen@iupui.edu Thu Jan  3 16:23:48 2008']

# your code here
```

```{code-cell} ipython3
:tags: [raises-exception]

email_occurrences.get("david.horwitz@uct.ac.za")
```

### Investigate: integrate the book chapter indexing program into our generic structure

What's the same? What needs to be modified?

```{code-cell} ipython3

```

### Practice: flag important emails

Let's say you have a list of 'starred contacts', and you want a separate index where you can ask the question "give me all the emails I got from this starred contact". You can imagine this being sort of a rudimentary back-end of your "important" tab in Gmail.

How might we modify our email indexing program to do this?

```{code-cell} ipython3
email_records = ['From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008',
 'From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008',
 'From zqian@umich.edu Fri Jan  4 16:10:39 2008',
 'From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008',
 'From zqian@umich.edu Fri Jan  4 15:03:18 2008',
 'From rjlowe@iupui.edu Fri Jan  4 14:50:18 2008',
 'From cwen@iupui.edu Fri Jan  4 11:37:30 2008',
 'From cwen@iupui.edu Fri Jan  4 11:35:08 2008',
 'From gsilver@umich.edu Fri Jan  4 11:12:37 2008',
 'From gsilver@umich.edu Fri Jan  4 11:11:52 2008',
 'From zqian@umich.edu Fri Jan  4 11:11:03 2008',
 'From gsilver@umich.edu Fri Jan  4 11:10:22 2008',
 'From wagnermr@iupui.edu Fri Jan  4 10:38:42 2008',
 'From zqian@umich.edu Fri Jan  4 10:17:43 2008',
 'From antranig@caret.cam.ac.uk Fri Jan  4 10:04:14 2008',
 'From gopal.ramasammycook@gmail.com Fri Jan  4 09:05:31 2008',
 'From david.horwitz@uct.ac.za Fri Jan  4 07:02:32 2008',
 'From david.horwitz@uct.ac.za Fri Jan  4 06:08:27 2008',
 'From david.horwitz@uct.ac.za Fri Jan  4 04:49:08 2008',
 'From david.horwitz@uct.ac.za Fri Jan  4 04:33:44 2008',
 'From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008',
 'From louis@media.berkeley.edu Thu Jan  3 19:51:21 2008',
 'From louis@media.berkeley.edu Thu Jan  3 17:18:23 2008',
 'From ray@media.berkeley.edu Thu Jan  3 17:07:00 2008',
 'From cwen@iupui.edu Thu Jan  3 16:34:40 2008',
 'From cwen@iupui.edu Thu Jan  3 16:29:07 2008',
 'From cwen@iupui.edu Thu Jan  3 16:23:48 2008']

# your code here
```
