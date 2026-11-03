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

# 7: Strings

## What are strings and why should we care about them?

### Strings are everywhere

We need to learn to work with strings because a lot of data we want to do things with live in the world as mixed data
- Email addresses
- Webpage URLs
- Names
- Documents, words
- Sales records
- Etc.

Strings are the ultimate "lingua franca" between systems
- Data is often passed as "serialized" forms (e.g., JSON: Javascript **Object** Notation)
- We assume strings coming in, and we parse it appropriately. This can include data (numbers/records), as we see in one of the Projects for this module!
- This also includes the "human system" (i.e., the user)!

Let's see what comes back from the `input()` function we introduced in Iteration.

```python
age = input('What is your age?')
```

*Note: `input()` requires interactive input. If you run this in your own Python environment, you'll be prompted to type your age.*

If you type `37`, the value stored in `age` is the **string** `'37'`, not the integer `37`:

```python
age
```
```
'37'
```

What data type is in `age`?

### Strings are sequences of characters

But what *is* a string? It's fundamentally a sequence of characters.

And that's exactly what a string is in Python too: it's a sequence of characters, much like (though not *exactly* like) a `list`. This means we can *iterate* through a string in a similar way that we can iterate through any other list.

```{code-cell} ipython3
s = "banana"
for char in s:
    print(char)
```

```{code-cell} ipython3
sentence = "she sells seashells by the seashore, except when she doesn't want to sell seashells"
for char in sentence:
    print(char)
```

### Characters don't have to be visible/letters!

Notice that even the "blank space" is a character! A string that includes an empty space character is **NOT** the same as an empty string (i.e., a list of characters of length zero), even though they print out the same. This distinction is very important to remember as you work with real world data.

```{code-cell} ipython3
a = "" # a blank/empty string
b = " " # a string with one blank space *character*
print("Printing out the value of a")
print(a)
print("Printing out the value of b")
print(b)
print(len(a), len(b))
print(a == b)
```

This means that whitespace at the beginning or end of strings define completely different strings! For example:

```{code-cell} ipython3
a = "James"
b = " James"
c = "James "
print(a == b)
print(b == c)
print(a == c)
```

```{code-cell} ipython3
clean = ""
for char in b:
    if char != " ":
        clean = clean + char
clean
```

Other kinds of characters that don't look like "letters":
- `\t` for tabs
- `\n` for newlines

```{code-cell} ipython3
# tab is \t
s = "a\ttab\nand a newline"
print(s)
for i in range(len(s)):
    print(i, s[i])
```

Again, even though they may look similar to our eyes ("blank"), they are not the same!

```{code-cell} ipython3
a = " "
b = "\t"
c = "\n"
print("a is ", a, "with length", len(a))
print("b is ", b, "with length", len(b))
print("c is ", c, "with length", len(c))
print("is a the same as b?", a == b)
print("is b the same as c?", b == c)
print("is a the same as c?", a == c)
```

We'll see in the next module how text data often comes in with a mix of various whitespace characters, which we can use to parse the data into structured records.

For example, the following string may look ridiculous, but the `\t` and `\n` characters in the string actually break it up quite nicely into a structured format that is readable by both humans and Python.

```{code-cell} ipython3
records = "NAME\tSCORE\tGRADE\nJoel\t81\tB-\nRony\t98\tA+\nSravya\t99\tA+"
print(records)
```

## Properties of strings

Like lists, strings are **sequences**: ordered collections of items that support indexing, slicing, `len()`, and the `in` operator. But strings are *not* lists — you can't use list methods like `.append()` on a string. And there is one other important difference: **strings are immutable**. You can never modify a string directly, only create a *new* string that you must then assign to a variable (or reassign to the same variable) if you want to preserve that change. More on this when we talk about working with strings.

### Strings are **ordered** (and therefore can be sorted and indexed and sliced like lists)

```{code-cell} ipython3
a_string = "hello world Hi"
print(sorted(a_string))
```

```{code-cell} ipython3
# can be indexed
a_string[0]
```

```{code-cell} ipython3
# and sliced
a_string[:5]
```

### Strings have length

```{code-cell} ipython3
# has length
print(len(a_string))
```

### Strings are IMMUTABLE (you can't modify them directly)

```{code-cell} ipython3
a_string = "hello"
a_string.upper()  # this does NOT change a_string
print(a_string)    # still "hello"

# to preserve the change, you must reassign
a_string = a_string.upper()
print(a_string)    # now "HELLO"
```

This property of strings has **one critical implication for how you work with them (vs. other data types):** anytime you modify a string, you must have some kind of variable assignment statement (even if it is back to itself) to preserve the change.

This is a really important point we'll drive home later when we dig into ways of working with strings.

### Aside: string encoding

The previous observation about blank spaces illustrates a larger point: we deliberately say strings are sequences of *characters*, not letters. This is because strings can include numbers, as we've seen (think usernames like joelchan86, or your uids), but also all sorts of other characters, including various kinds of blank spaces --- like tabs, spaces, and newlines --- and even emoji!

Check this resource for an overview and initial guide: https://realpython.com/python-encodings-guide/

This is something I want to show you to give you a better intuition for what strings *are*, but there is also an important practical implication: you need to be very careful to transform or normalize your strings when you want to sort or compare them. What's the same or different to your human eye will often *not* be the same or different to the computer's eye.

For example, "A" and "a" have different encodings. We can use the built-in `ord()` function to see the numeric code for any character:

```{code-cell} ipython3
# each character has a unique numeric code
print("A:", ord("A"))
print("a:", ord("a"))
print("B:", ord("B"))
print("0:", ord("0"))
print(" :", ord(" "))
```

Notice that `'A'` is 65 and `'a'` is 97 — completely different numbers! This is why Python does *not* see them as the same "letter". Similarly, a space character has its own code (32), which is why `"James"` and `"James "` are different strings:

```{code-cell} ipython3
s1 = "James"
s2 = "james"
s3 = "James "
print(s1 == s2)  # False - different case
print(s1 == s3)  # False - trailing space
```

## Working with strings: basics

Similar to lists, many basic operations with strings revolve around indexing and iteration.

### Getting parts of a string

#### Indexing

Works similarly to lists.

```{code-cell} ipython3
s = "my name is inigo montoya, you killed my father, prepare to die!"
for i in range(len(s)):
    char = s[i]
    print(i, char)
```

```{code-cell} ipython3
s = "my name is inigo montoya, you killed my father, prepare to die!"
for char in s:
    print(char)
```

```{code-cell} ipython3
s = "my name is inigo montoya, you killed my father, prepare to die!"
# give me the last letter
print(s[-1])
```

Just like with lists, negative indexing works too — `-1` gives you the last item, `-2` gives the second-to-last, and so on.

**PRACTICE**: How would you get the first number of the level (after the four-letter code)?

```{code-cell} ipython3
code = "INST201"
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
print(code[4])  # '2'
```

The department `INST` takes up indices 0 through 3, so the first number is at index 4.
`````

**PRACTICE**: How would you get the first initial for each name?

```{code-cell} ipython3
names = ["Joel", "Sarah", "John", "Michael", "Patrick", "Kacie"]
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
for name in names:
    print(name[0])
```

Each `name` is a string, so `name[0]` is its first character. This is the same as indexing into a list, just one level down: first we loop over the list to get each string, then we index into the string.
`````

#### Slicing

Remember slicing? Here we can think about substrings. Super useful for truncation, or getting particular parts of strings when you know the pattern (e.g., first four characters of a course code is always the department).

Remember: the index before the `:` indicates where you want to *start*, and the index after the `:` indicates where you want to stop *before*. So `[0:4]` will go from index `0` to index `3` (before index 4). Leaving out an index implicitly says "to the max" (e.g., from `0` or `until the end`).

```{code-cell} ipython3
code = "INST201"
# get the first four chars (index 0 to 3, stop before 4)
area = code[:4]
print(area)
```

**PRACTICE**: how would you get the course number?

```{code-cell} ipython3
# get last three characters
code = "INST201"
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
print(code[4:])  # '201'
```

Start at index 4 (right after the department) and leave out the stop to go to the end. `code[-3:]` (the last three characters) also works here.
`````

**PRACTICE**: How would you get the first 2 letters of the name?

```{code-cell} ipython3
name = "Michelle"
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
print(name[:2])  # 'Mi'
```

When you start from the beginning, the stop number is the same as how many characters you get.
`````

#### We can put these into filtering/counting patterns that check parts of strings!

**PRACTICE**: How many students in the class have names that begin with `Eli`?

```{code-cell} ipython3
names = [
    "Eliana",
    "John",
    "Elias",
    "Esther",
    "Joseph",
    "Ebenezer",
    "Eric",
    "Josiah",
    "Joe",
    "Eliza",
    "Frank",
    "Ellie",
]

count = 0

for name in names:
    if name[:3] == "Eli": # fill in your boolean expression
        count += 1

count
```

**PRACTICE**: What about grabbing the names that begin with `Jo`?

```{code-cell} ipython3
names = [
    "Eliana",
    "John",
    "Elias",
    "Esther",
    "Joseph",
    "Ebenezer",
    "Eric",
    "Josiah",
    "Joe",
    "Eliza",
    "Frank",
    "Ellie",
]

target_names = []

# your code here
```

`````{admonition} Answer:
:class: toggle

```python
for name in names:
    if name[:2] == "Jo":
        target_names.append(name)
target_names  # ['John', 'Joseph', 'Josiah', 'Joe']
```

This is the same filtering pattern as the `Eli` example, but we `.append()` the matching names instead of counting them. Notice the slice is `[:2]` this time, since `"Jo"` is 2 characters long.
`````

### Join strings

We've also already shown you concatenation.

```{code-cell} ipython3
s1 = "Hello"
s2 = " World!"
print(s1 + s2)
```

Now that you've seen lists, you can get a bit more intuition for how it works.

```{code-cell} ipython3
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)
```

### Check if character(s) is in string

Just like lists, the `in` operator also works for strings. We can think of this as checking whether some *substring* (could be a single character, or a sequence of characters) is part of a target string.

Example: check whether this message contains a keyword

```{code-cell} ipython3
message = "hello, my name is inigo montoya"
keyword = "ingo"
# let's check if the message mentions my name!
print(keyword in message)
```

**PRACTICE**: check whether these strings contain a space or tab!

tab is represented by `'\t'`
space is represented by `' '`

```{code-cell} ipython3
s1 = "\tInigo"
s2 = " Inigo"
# your code
```

`````{admonition} Answer:
:class: toggle

```python
print("\t" in s1)  # True
print(" " in s1)   # False
print("\t" in s2)  # False
print(" " in s2)   # True
```

Both strings *look* like they start with a blank, but `s1` starts with a tab and `s2` starts with a space. To Python, those are different characters.
`````

#### Put it into our filtering pattern!

**PRACTICE**: Only grab the classes from CMSC

```{code-cell} ipython3
course_codes = ["INST201", "INST126", "INFM322", "CMSC126"]

target_courses = []

# your code
```

`````{admonition} Answer:
:class: toggle

```python
for code in course_codes:
    if "CMSC" in code:
        target_courses.append(code)
target_courses  # ['CMSC126']
```

Our filtering pattern again, with `in` as the Boolean expression.
`````

**PRACTICE**: Only grab the emails that are from `.edu` domain

```{code-cell} ipython3
emails = ["oasislab@gmail.com", "joelchan@terpmail.umd.edu", "rony@terpmail.com", "joelchan@umd.edu", "joelchan@gmail.com", "sarahp@umd.edu", "sarah@umd.org"]
target_emails = []

# your code here
```

`````{admonition} Answer:
:class: toggle

```python
for email in emails:
    if ".edu" in email:
        target_emails.append(email)
target_emails  # ['joelchan@terpmail.umd.edu', 'joelchan@umd.edu', 'sarahp@umd.edu']
```

This works for these emails, but `in` checks for `".edu"` *anywhere* in the string. So it would also grab an email like `"joe.education@gmail.com"`! We'll see a more precise way to check this (`.endswith()`) in the next section.
`````

### Practice: Indexing, slicing, and checking parts of strings

We'll practice these basics in two ways. First, we'll **read** code and predict what it does (code tracing). Then we'll flip it around and **write** the code ourselves from an English description.

#### Part 1: Code tracing

Predict the output of each code snippet before running the cell!

##### Trace 1

```{code-cell} ipython3
:tags: [remove-output]

code = "INST126"
print(code[0])
print(code[-1])
```

- A) `I` then `6`
- B) `N` then `6`
- C) `I` then `2`
- D) `INST` then `126`

````{admonition} Answer:
:class: toggle

**A) `I` then `6`**

Just like lists, index `0` is the first character and index `-1` is the last character. If you picked B, you're thinking of index 0 as the "second" item. If you picked D, you're thinking of the "parts" of the code that matter to *us* (department and number). But to Python, a string is just a sequence of characters, so an index always gives you one character.
````

##### Trace 2

```{code-cell} ipython3
:tags: [remove-output]

word = "seashells"
print(word[3:6])
```

- A) `she`
- B) `shel`
- C) `ash`
- D) `ashe`

````{admonition} Answer:
:class: toggle

**A) `she`**

Let's count: `s`(0) `e`(1) `a`(2) `s`(3) `h`(4) `e`(5) `l`(6) `l`(7) `s`(8). The slice `[3:6]` starts at index 3 and stops *before* index 6, so we get indices 3, 4, and 5: `she`. If you picked B, remember the stop is not included. If you picked C or D, you may have started counting from 1 instead of 0.
````

##### Trace 3

```{code-cell} ipython3
:tags: [remove-output]

name = " Joel "
print(len(name))
print(name[0] == "J")
```

- A) `4` then `True`
- B) `6` then `False`
- C) `6` then `True`
- D) `4` then `False`

````{admonition} Answer:
:class: toggle

**B) `6` then `False`**

The spaces at the beginning and end are characters too! So `" Joel "` has 6 characters, and the character at index `0` is a space `" "`, not `"J"`. If you picked A, you're seeing the string the way your eye does, not the way Python does. This is exactly the kind of thing that will trip you up with real-world data.
````

##### Trace 4

```{code-cell} ipython3
:tags: [remove-output, raises-exception]

name = "joel"
name[0] = "J"
print(name)
```

- A) `Joel`
- B) `joel`
- C) Error
- D) `J`

````{admonition} Answer:
:class: toggle

**C) Error**

You get a `TypeError: 'str' object does not support item assignment`. Strings are **immutable**: you can't change a character in a string directly, even though you *can* do this with a list. If you picked A, you were thinking of how this works with lists.

To get `"Joel"`, you have to make a *new* string and assign it: `name = "J" + name[1:]`.
````

##### Trace 5

```{code-cell} ipython3
:tags: [remove-output]

email = "joelchan@umd.edu"
print("umd" in email)
print("UMD" in email)
print("chan@" in email)
```

- A) `True` then `True` then `True`
- B) `True` then `False` then `True`
- C) `True` then `False` then `False`
- D) `False` then `False` then `True`

````{admonition} Answer:
:class: toggle

**B) `True` then `False` then `True`**

`in` checks whether the substring on the left appears anywhere in the string on the right. `"umd"` is in there. `"UMD"` is not, because uppercase and lowercase letters are *different* characters to Python. `"chan@"` is in there too: a substring can be any sequence of characters in a row, even if it crosses what we'd think of as the "parts" of the email. If you picked C, you may be thinking that `in` only finds whole "words."
````

##### Trace 6

```{code-cell} ipython3
:tags: [remove-output]

word = "mississippi"
count = 0
for char in word:
    if char == "s":
        count += 1
print(count)
```

- A) `2`
- B) `4`
- C) `11`
- D) `1`

````{admonition} Answer:
:class: toggle

**B) `4`**

Looping over a string gives you one character at a time. We add 1 to `count` every time the character is `"s"`, and there are four `s`'s in "mississippi". If you picked A, you may be counting the `"ss"` pairs instead of the individual characters. If you picked C, you counted every character (that would be `len(word)`).
````

##### Trace 7

```{code-cell} ipython3
:tags: [remove-output]

code = "INFM322"
print(code[-3:])
print(code[:-3])
```

- A) `322` then `INFM`
- B) `322` then `INFM3`
- C) `22` then `INFM3`
- D) `INF` then `M322`

````{admonition} Answer:
:class: toggle

**A) `322` then `INFM`**

Negative numbers work in slices too. `[-3:]` starts at the 3rd-to-last character and goes to the end: "the last 3 characters." `[:-3]` starts at the beginning and stops *before* the 3rd-to-last character: "everything except the last 3 characters." If you picked B or C, remember that the stop is not included, even when it's negative. If you picked D, you're reading the negative numbers as counting from the front.
````

#### Part 2: Writing code with strings

Now let's flip it around: instead of predicting what code does, **write the code** that does what the English description says. For each problem, ask yourself:

1. Do I want **one character** (indexing), or **several characters in a row** (slicing)?
2. Is it easier to count from the **front** (0, 1, 2, ...) or from the **back** (-1, -2, ...)?
3. Do I need to **build** a new string (e.g., with `+`)? Remember that you can't change a string directly!

Write your code in the cell, run it to check that it gives you what you expect, then compare with the answer.

##### Write 1: Initials

```{code-cell} ipython3
first = "Sravya"
last = "Rao"
# print the initials, like "SR"

```

````{admonition} Answer:
:class: toggle
```python
initials = first[0] + last[0]
print(initials)
```

Index `0` gets the first character of each name, and `+` joins them together into a new string.
````

##### Write 2: Splitting a course code into its parts

```{code-cell} ipython3
code = "INST126"
# print the department (the first four characters)

# print the course number (everything after the department)

```

````{admonition} Answer:
:class: toggle
```python
print(code[:4])
print(code[4:])
```

Notice how the two slices fit together: `[:4]` stops *before* index 4, and `[4:]` starts *at* index 4. So they split the string at the same place, with nothing missing and nothing repeated. `code[-3:]` also works for the course number here, but only if every course number is exactly 3 characters long. `[4:]` works as long as every department is 4 letters.
````

##### Write 3: Card ending in...

```{code-cell} ipython3
card_number = "4111222233334444"
# print a message like "Card ending in 4444" (using the last 4 digits of the card number)

```

````{admonition} Answer:
:class: toggle
```python
print("Card ending in " + card_number[-4:])
```

`[-4:]` gets the last 4 characters, no matter how long the card number is. A common mistake is `card_number[-4:-1]`, which leaves out the last digit (the stop is not included!).
````

##### Write 4: Does the message mention a keyword?

```{code-cell} ipython3
message = "hi, I'd like a refund for my order please"
keyword = "refund"
# print True if the keyword is anywhere in the message, and False if it isn't

```

````{admonition} Answer:
:class: toggle
```python
print(keyword in message)
```

`in` is a Boolean expression, so it evaluates to `True` or `False`. That means you could also use it directly as the condition in an `if` statement (e.g., `if keyword in message:`).
````

##### Write 5: Filtering by part of a string

```{code-cell} ipython3
# dates are always written as YYYY-MM-DD
dates = ["2026-09-28", "2026-10-02", "2026-10-15", "2026-11-01", "2026-10-30"]
october_dates = []
# put only the dates that are in October (month "10") into october_dates, then print it

```

````{admonition} Answer:
:class: toggle
```python
for date in dates:
    if date[5:7] == "10":
        october_dates.append(date)
print(october_dates)
```

This prints `['2026-10-02', '2026-10-15', '2026-10-30']`. Because the dates always follow the same pattern, the month is always at indices 5 and 6, so `[5:7]` grabs it. Counting it out is worth doing: `2`(0) `0`(1) `2`(2) `6`(3) `-`(4) `1`(5) `0`(6). This is our filtering pattern from Iteration, where the Boolean expression checks part of each string.

Watch out: `"10" in date` would *not* work here! It would also match `"2026-11-10"` (the 10th of November).
````

##### Write 6: Building an acronym

```{code-cell} ipython3
words = ["Portable", "Network", "Graphics"]
acronym = ""
# build up the acronym (the first letter of each word, like "PNG") in a loop, then print it

```

````{admonition} Answer:
:class: toggle
```python
for word in words:
    acronym = acronym + word[0]
print(acronym)
```

This is the same accumulator pattern we used for adding up numbers, but with strings! We start with an empty string `""` (instead of `0`), and each time through the loop we make a new, longer string with `+` and reassign it to `acronym`. You can also write it as `acronym += word[0]`.
````

##### Write 7: "Changing" a string

```{code-cell} ipython3
name = "joel"
# change name so it starts with a capital J (without using any string methods), then print it

```

````{admonition} Answer:
:class: toggle
```python
name = "J" + name[1:]
print(name)
```

We can't do `name[0] = "J"`, because strings are immutable (see Trace 4). Instead, we build a **new** string: the new first letter, plus everything from index 1 onward. Then we assign that new string back to `name`. We'll see in the next section that string methods (like `.capitalize()`) make this easier, but they follow the same rule: they give you back a new string, and you have to assign it if you want to keep it.
````

## Working with strings: advanced

Similar to lists, there is a collection of in-built **string methods**: functions in Python that operate on strings: https://docs.python.org/3/library/stdtypes.html#string-methods

I'm not going to show you all of them, but I will talk through them and discuss some fairly common ones

No need to memorize them – just know:
- There are many methods that allow you to do things with strings – if you want to do something, first search for that method! It's often way more efficient/bug-free than what you'll write (even after you get good)
- Where to find the exact code for it, how to figure out how they work

More importantly, I want you to practice reading documentation, get a sense of how to use functions (code that other people have written that you can reuse): what are the parameters? return values? what can you learn from examples? how do you learn how to use it appropriately in your own code?

```{code-cell} ipython3
message = "Hello, my name is Inigo Montoya"
# let's check if the message mentions my name!
print("inigo" in message.lower())
```

### Checking a string

Common methods include:
- `.isnumeric()` - is it all numeric?
- `.isalnum()` - is it all letters and numbers?
- `.isalpha()` - is it all letters?
- `.startswith()` - does it start with some substring?
- `.endswith()` - does it end with some substring?

Example: `.isnumeric()` checks if the string is entirely composed of numeric characters.

```{code-cell} ipython3
a = " 123"
a.isnumeric() # False! The leading space is not a numeric character
```

```{code-cell} ipython3
# we want to do math
a = "x123"
b = "567"
# but first we want to make sure the strings are all numbers before we convert them
if a.isnumeric() and b.isnumeric():
    a = int(a)
    b = int(b)
    print(a*b)
else:
    print("One of the input strings contains non-digits!")
```

Example application: cleaning a sales record!

```{code-cell} ipython3
# need to turn into a number so I can do math with it
sales_record = "$1,000,000"

# with iteration
cleaned = "" # initialize clean string as a blank/empty string
# for each character in the sales record string
for char in sales_record:
    if char.isnumeric(): # if the character is numeric
        cleaned += char # grab it (notice the use of concatenation here)
print(cleaned)
```

Another example: `.startswith()` and `.endswith()` check whether the beginning/end of a string matches a substring (single character or sequence of characters).

```{code-cell} ipython3
l = ["INST201", "INST126", "INFM322", "CMSC126", "joelchan@umd.edu", "joelchan", ".edu", "sarah@umd.edu"]
# get all the strings that start with INST
for item in l:
    if item.startswith("INST"):
        print(item)
```

**PRACTICE**: Use `.startswith()` to only grab the classes from CMSC

```{code-cell} ipython3
course_codes = ["INST201", "INST126", "INFM322", "CMSC126"]
target_courses = []
# your code
```

`````{admonition} Answer:
:class: toggle

```python
for code in course_codes:
    if code.startswith("CMSC"):
        target_courses.append(code)
target_courses  # ['CMSC126']
```

Compare this with the `in` version from earlier: `.startswith()` only matches `"CMSC"` at the *beginning* of the string, which is what we really mean by "a CMSC class."
`````

**PRACTICE**: Use `.endswith()` to only grab the emails that are from `.edu` domain

```{code-cell} ipython3
emails = ["oasislab@gmail.com", "joelchan@terpmail.umd.edu", "rony@terpmail.com", "joelchan@umd.edu", "joelchan@gmail.com", "sarahp@umd.edu", "sarah@umd.org"]

target_emails = []
# your code
```

`````{admonition} Answer:
:class: toggle

```python
for email in emails:
    if email.endswith(".edu"):
        target_emails.append(email)
target_emails  # ['joelchan@terpmail.umd.edu', 'joelchan@umd.edu', 'sarahp@umd.edu']
```

Same result as the `in` version for these emails, but `.endswith()` only matches `".edu"` at the very *end*. So unlike `in`, it would correctly skip something like `"joe.education@gmail.com"`.
`````

**PRACTICE**: Write code that counts how many items in `data` are valid positive integers (contain only digits).

```{code-cell} ipython3
data = ["42", "-7", "100", "3.5", "abc", "0", "99"]
count = 0
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
data = ["42", "-7", "100", "3.5", "abc", "0", "99"]
count = 0
for item in data:
    if item.isnumeric():
        count += 1
count  # 4: "42", "100", "0", "99"
```
`````

**PRACTICE**: Write code that grabs only the filenames that end with `.csv` from the list.

```{code-cell} ipython3
files = ["data.csv", "notes.txt", "report.csv", "image.png", "grades.csv", "readme.md"]
csv_files = []
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
files = ["data.csv", "notes.txt", "report.csv", "image.png", "grades.csv", "readme.md"]
csv_files = []
for f in files:
    if f.endswith(".csv"):
        csv_files.append(f)
csv_files  # ['data.csv', 'report.csv', 'grades.csv']
```
`````

**PRACTICE**: Write code that checks each username and prints only the ones that are alphanumeric (letters and digits only, no special characters).

```{code-cell} ipython3
usernames = ["joel86", "sarah!", "john_doe", "kacie2024", "mr.smith", "rony99"]
valid = []
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
usernames = ["joel86", "sarah!", "john_doe", "kacie2024", "mr.smith", "rony99"]
valid = []
for u in usernames:
    if u.isalnum():
        valid.append(u)
valid  # ['joel86', 'kacie2024', 'rony99']
```
`````

**PRACTICE**: Write code that separates the course codes into two lists: one for courses that start with `"INST"` and one for everything else.

```{code-cell} ipython3
codes = ["INST126", "CMSC132", "INST201", "MATH140", "INST314", "PSYC100"]
inst_courses = []
other_courses = []
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
codes = ["INST126", "CMSC132", "INST201", "MATH140", "INST314", "PSYC100"]
inst_courses = []
other_courses = []
for code in codes:
    if code.startswith("INST"):
        inst_courses.append(code)
    else:
        other_courses.append(code)
inst_courses   # ['INST126', 'INST201', 'INST314']
other_courses  # ['CMSC132', 'MATH140', 'PSYC100']
```
`````

#### Practice: Code Tracing with Checking Methods

Predict the output of each code snippet before running the cell!

##### Trace 1

```{code-cell} ipython3
:tags: [remove-output]

print("2026".isnumeric())
print("20.26".isnumeric())
```

- A) `True` then `True`
- B) `True` then `False`
- C) `False` then `False`
- D) `2026` then `20.26`

````{admonition} Answer:
:class: toggle

**B) `True` then `False`**

`.isnumeric()` checks whether **every** character in the string is a digit. `"20.26"` has a `.`, which is not a digit, so it's `False`, even though it looks like a number to us. If you picked D, remember that checking methods give back a Boolean (`True` or `False`), not the string itself.
````

##### Trace 2

```{code-cell} ipython3
:tags: [remove-output]

values = ["42", "-5", " 7", "3"]
count = 0
for v in values:
    if v.isnumeric():
        count += 1
print(count)
```

- A) `4`
- B) `3`
- C) `2`
- D) `1`

````{admonition} Answer:
:class: toggle

**C) `2`**

Only `"42"` and `"3"` are made up entirely of digits. `"-5"` has a `-`, and `" 7"` has a space at the start; neither of those is a digit. If you picked A, you're thinking about whether each value *means* a number to you, rather than checking each character. If you picked B, look closely at `" 7"`: that leading space counts!
````

##### Trace 3

```{code-cell} ipython3
:tags: [remove-output]

course = "inst126"
print(course.startswith("INST"))
```

- A) `True`
- B) `False`
- C) `inst`
- D) Error

````{admonition} Answer:
:class: toggle

**B) `False`**

`"inst"` and `"INST"` are different, because uppercase and lowercase letters are different characters. If you want a check that ignores case, normalize the string first, e.g., `course.upper().startswith("INST")` (more on this in the next section). If you picked C, remember that `.startswith()` gives back a Boolean, not the beginning of the string.
````

##### Trace 4

```{code-cell} ipython3
:tags: [remove-output]

filename = "report.CSV"
print(filename.endswith(".csv"))
print(filename.lower().endswith(".csv"))
print(filename)
```

- A) `False` then `True` then `report.csv`
- B) `True` then `True` then `report.CSV`
- C) `False` then `True` then `report.CSV`
- D) `False` then `False` then `report.CSV`

````{admonition} Answer:
:class: toggle

**C) `False` then `True` then `report.CSV`**

The first check is `False` because `".CSV"` and `".csv"` are different. In the second line, `filename.lower()` makes a new lowercase string (`"report.csv"`), and *that* new string ends with `".csv"`, so it's `True`. But we never assigned the lowercase version to anything, so `filename` is unchanged (strings are immutable!). If you picked A, that's the immutability gotcha.
````

##### Trace 5

```{code-cell} ipython3
:tags: [remove-output]

name = "Mary Jane"
print(name.isalpha())
print(name.replace(" ", "").isalpha())
```

- A) `True` then `True`
- B) `False` then `True`
- C) `False` then `False`
- D) `True` then `False`

````{admonition} Answer:
:class: toggle

**B) `False` then `True`**

`.isalpha()` checks that **every** character is a letter, and a space is not a letter. So `"Mary Jane"` fails the check. Once we remove the space with `.replace(" ", "")`, we get `"MaryJane"`, which is all letters. If you picked A, remember: spaces are characters too!
````

##### Trace 6

```{code-cell} ipython3
:tags: [remove-output]

usernames = ["joel86", "sarah!", "kacie_2024", "rony99"]
valid = []
for u in usernames:
    if u.isalnum():
        valid.append(u)
print(valid)
```

- A) `['joel86', 'kacie_2024', 'rony99']`
- B) `['joel86', 'rony99']`
- C) `['sarah!', 'kacie_2024']`
- D) `['joel86', 'sarah!', 'kacie_2024', 'rony99']`

````{admonition} Answer:
:class: toggle

**B) `['joel86', 'rony99']`**

`.isalnum()` is `True` only if every character is a letter or a digit. `"sarah!"` has a `!`, and `"kacie_2024"` has an `_`, so neither passes. If you picked A, you may have assumed the underscore counts (it's common in usernames, but it isn't a letter or a digit). If you picked C, you flipped the filter: those are the usernames that *fail* the check.
````

### "Cleaning" / normalizing a string

Often we get data in string form, and we need to make sure it conforms to our expectations. Sometimes this means we modify it.

Common methods include:
- `.lower()` or `.upper()` - convert the string to all lowercase or uppercase so we eliminate differences that have to do with case; remember that `A` and `a` are *different* to Python!
- `.replace()` - replace parts of a string with something else - often we use this to strip out characters we don't like (by replacing them with a blank string)
- `.strip()` - remove hidden whitespace at the beginning and end of strings. super handy in data cleaning scenarios! closely related are `.lstrip()` and `.rstrip()` (can you guess what they do?)

Note: you can "**chain**" methods, and often want to do so! Often this is handy to "bundle together" cleaning/normalizing operations.

```{code-cell} ipython3
# can use .replace() if you know in advance which characters you want to strip out
def normalize_sales_record(sale):
    return sale.replace("$","").replace(",","")

sales_record = "$1,000,000"
cleaned = normalize_sales_record(sales_record)
print(cleaned)
```

Chaining works because a `str.method()` expression yields a string, which then is also able to do another `.method()`. We can do this as many times as we like, though be careful to make sure your code is still readable!

```{code-cell} ipython3
def normalize_string(s):
    return s.upper().strip() # convert the string to upper case and remove leading and trailing blank spaces

# need to make sure it's normalized and we remove all weird stuff
n = " Josh Lyman"
m = "JOSH LYMAN"
print(n)
print(m)
print(n == m)
n_normal = normalize_string(n)
m_normal = normalize_string(m)
print(n_normal)
print(m_normal)
print(n_normal == m_normal)
```

**PRACTICE**: Given a list of names with messy whitespace, use `.strip()` to clean them and collect into a new list.

```{code-cell} ipython3
raw_names = ["  Alice", "Bob  ", "  Charlie  ", "Diana"]
cleaned_names = []
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
raw_names = ["  Alice", "Bob  ", "  Charlie  ", "Diana"]
cleaned_names = []
for name in raw_names:
    cleaned_names.append(name.strip())
cleaned_names  # ['Alice', 'Bob', 'Charlie', 'Diana']
```
`````

**PRACTICE**: Write code that checks if two strings are the "same" word regardless of case and whitespace. Print `True` or `False`.

```{code-cell} ipython3
a = "  Hello "
b = "HELLO"
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
a = "  Hello "
b = "HELLO"
print(a.strip().lower() == b.strip().lower())  # True
```
`````

**PRACTICE**: Write code that takes a list of messy phone numbers and removes all dashes and spaces to produce clean digit-only strings.

```{code-cell} ipython3
phones = ["301-555-1234", "240 555 5678", "301-555 9999", "2405554321"]
cleaned_phones = []
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
phones = ["301-555-1234", "240 555 5678", "301-555 9999", "2405554321"]
cleaned_phones = []
for phone in phones:
    cleaned_phones.append(phone.replace("-", "").replace(" ", ""))
cleaned_phones  # ['3015551234', '2405555678', '3015559999', '2405554321']
```
`````

**PRACTICE**: Write code that normalizes a list of email addresses to lowercase, then counts how many are from `umd.edu`.

```{code-cell} ipython3
emails = ["JoelChan@UMD.EDU", "sarah@gmail.com", "RONY@umd.edu", "pat@UMD.edu", "lee@yahoo.com"]
count = 0
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
emails = ["JoelChan@UMD.EDU", "sarah@gmail.com", "RONY@umd.edu", "pat@UMD.edu", "lee@yahoo.com"]
count = 0
for email in emails:
    if email.lower().endswith("umd.edu"):
        count += 1
count  # 3
```
`````

**PRACTICE**: Write code that takes a list of product names with inconsistent casing and extra whitespace, and produces a cleaned list where every name is title case (first letter capitalized) with no extra spaces.

```{code-cell} ipython3
products = ["  COFFEE mug", "water BOTTLE ", "  LAPTOP stand  ", "phone CASE"]
cleaned = []
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
products = ["  COFFEE mug", "water BOTTLE ", "  LAPTOP stand  ", "phone CASE"]
cleaned = []
for p in products:
    cleaned.append(p.strip().lower().replace("  ", " ").title())
cleaned  # ['Coffee Mug', 'Water Bottle', 'Laptop Stand', 'Phone Case']
```

Note the chaining: `.strip()` → `.lower()` → `.replace()` → `.title()`. Each method returns a new string for the next method to work on.
`````

**PRACTICE**: Write code that takes a messy list of hashtags and normalizes them: remove any leading/trailing spaces, convert to lowercase, and remove the `#` symbol. Collect the cleaned tags into a new list.

```{code-cell} ipython3
tags = ["#Python ", " #DataScience", "#INST126 ", " #coding", "#Python"]
cleaned_tags = []
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
tags = ["#Python ", " #DataScience", "#INST126 ", " #coding", "#Python"]
cleaned_tags = []
for tag in tags:
    cleaned_tags.append(tag.strip().lower().replace("#", ""))
cleaned_tags  # ['python', 'datascience', 'inst126', 'coding', 'python']
```
`````

#### Practice: Code Tracing with Cleaning/Normalizing

Predict the output of each code snippet before running the cell!

##### Trace 1

```{code-cell} ipython3
:tags: [remove-output]

s = "  Hello World  "
result = s.strip()
print(result)
print(len(result))
```

- A) `Hello World` then `11`
- B) `Hello World` then `15`
- C) `HelloWorld` then `10`
- D) `Hello World  ` then `13`

````{admonition} Answer:
:class: toggle

**A) `Hello World` then `11`**

`.strip()` removes leading and trailing whitespace only — it does not touch spaces *inside* the string. The original has 2 leading and 2 trailing spaces, so 15 - 4 = 11.
````

##### Trace 2

```{code-cell} ipython3
:tags: [remove-output]

s = "Hello"
s.lower()
print(s)
```

- A) `hello`
- B) `Hello`
- C) `HELLO`
- D) Error

````{admonition} Answer:
:class: toggle

**B) `Hello`**

Strings are immutable! `.lower()` returns a new string, but the result is never assigned to anything. `s` is unchanged.
````

##### Trace 3

```{code-cell} ipython3
:tags: [remove-output]

s = "$1,200.50"
s = s.replace("$", "").replace(",", "")
print(s)
```

- A) `$1,200.50`
- B) `120050`
- C) `1200.50`
- D) `1,200.50`

````{admonition} Answer:
:class: toggle

**C) `1200.50`**

The first `.replace("$", "")` removes the dollar sign → `"1,200.50"`. The second `.replace(",", "")` removes the comma → `"1200.50"`. The period is not removed because we didn't replace it. And because we reassigned `s = ...`, the change is preserved.
````

##### Trace 4

```{code-cell} ipython3
:tags: [remove-output]

a = " Python "
b = "PYTHON"
a = a.strip().upper()
print(a == b)
print(a)
```

- A) `False` then `Python`
- B) `True` then `PYTHON`
- C) `False` then ` PYTHON `
- D) `True` then `python`

````{admonition} Answer:
:class: toggle

**B) `True` then `PYTHON`**

`.strip()` removes the spaces → `"Python"`, then `.upper()` converts to `"PYTHON"`. After reassignment, `a` is `"PYTHON"`, which equals `b`.
````

##### Trace 5

```{code-cell} ipython3
:tags: [remove-output]

msg = "aaa-bbb-ccc"
msg = msg.replace("-", " ")
msg = msg.upper()
print(msg)
```

- A) `AAA-BBB-CCC`
- B) `aaa bbb ccc`
- C) `AAA BBB CCC`
- D) `AAABBBCCC`

````{admonition} Answer:
:class: toggle

**C) `AAA BBB CCC`**

First `.replace("-", " ")` swaps dashes for spaces → `"aaa bbb ccc"`. Then `.upper()` converts everything to uppercase → `"AAA BBB CCC"`. Both results are reassigned to `msg`.
````

##### Trace 6

```{code-cell} ipython3
:tags: [remove-output]

names = ["  alice", "BOB  ", " Charlie "]
result = []
for name in names:
    result.append(name.strip().lower())
print(result)
```

- A) `['alice', 'bob', 'charlie']`
- B) `['  alice', 'bob  ', ' charlie ']`
- C) `['Alice', 'Bob', 'Charlie']`
- D) `['alice', 'BOB', 'Charlie']`

````{admonition} Answer:
:class: toggle

**A) `['alice', 'bob', 'charlie']`**

Each iteration strips whitespace then lowercases: `"  alice"` → `"alice"`, `"BOB  "` → `"bob"`, `" Charlie "` → `"charlie"`. The cleaned versions are appended to `result`.
````

### "Parsing" a string (getting specific bits we want)

You can do this if you know there is some *separator* that you can rely on to divide the string into the "bits" you want.

Examples:
- Parse an email
- Parse a URL
- Parse a sentence into words!
- Parse a time stamp

These all use the `.split()` method, which takes a `separator` parameter as input, and returns a `list` of strings that are separated around the `separator`.

Example: get elements of an email address.

```{code-cell} ipython3
email = "joelchan@umd.edu"
# we want to split the email into username and domain
elements = email.split("@") # split on the `@` character
print(elements)
username = elements[0] # username is the 1st element in the split
print(username)
```

```{code-cell} ipython3
email = "joelchan@umd.edu"
# if we only want the domain (.edu), we can do a multiple split
split1 = email.split("@") # split the email by the @ separator
domainserver = split1[1] # grab the second item
split2 = domainserver.split(".") # split that second item by the . separator
domain = split2[1] # get the second item from that one
print(domain)
```

#### Picture it: how `.split()` cuts up a string

It helps to picture what `.split()` is doing under the hood. Python goes through the string looking for the separator. Every time it finds one, it makes a cut there. Then:

- The separators themselves are **thrown away**.
- Each **piece** is the slice of the string *between* the separators.
- The pieces go into a new **list**, in order.

Let's start with the simplest case: a string with one instance of a separator in it, which will get sliced into two pieces. 

```{image} assets/split-one-separator.svg
:alt: Diagram of the string 'joelchan@umd.edu' as a row of character boxes with boundary indexes 0 to 16. The @ at index 8 is highlighted as the separator. The pieces s[0:8] and s[9:16] are bracketed, and they become the list ['joelchan', 'umd.edu'].
:width: 600px
:align: center
```

Notice how each piece is a slice you could have written yourself (the `@` at index 8 isn't in either slice!).

With more separators, we get more cuts, and so more pieces. A handy rule: **N separators give you N + 1 pieces.**

```{image} assets/split-many-separators.svg
:alt: Diagram of the string '13:30:31' with the two colons highlighted as separators. The pieces s[0:2], s[3:5], and s[6:8] become the list ['13', '30', '31'].
:width: 450px
:align: center
```

Now for the tricky one. What if two separators are right next to each other (like a double space)? Python still makes a cut at *each* separator, so there's a piece between them. But there's nothing in that piece, so it's an **empty string**: `s[8:8]` starts and stops at the same place.

```{image} assets/split-empty-piece.svg
:alt: Diagram of the string 'one two  three' with the three spaces highlighted as separators, two of them next to each other at indexes 7 and 8. The pieces are s[0:3], s[4:7], an empty piece s[8:8], and s[9:14], which become the list ['one', 'two', '', 'three'].
:width: 560px
:align: center
```

This is where the mysterious `''` in your results comes from! (If you're splitting words that might have extra spaces, `.split()` with *no* argument is smarter: it treats any run of whitespace as one separator, so you won't get empty strings.)

Finally, what if the separator isn't in the string at all? There's nothing to cut, so you get the whole string back as the only piece. Notice that you still get a **list** (with one item), not just the string.

```{image} assets/split-no-separator.svg
:alt: Diagram of the string 'joelchan' with no @ anywhere. The whole string s[0:8] is one piece, which becomes the one-item list ['joelchan'].
:width: 480px
:align: center
```

This one is a common source of bugs: if you write `"joelchan".split("@")[1]` expecting the domain, you'll get an `IndexError`, because the list only has an index `0`. The key idea here is to make sure you understand what (and how many) separators are in your strings, to write appropriate `.split()` operations and avoid errors.

#### Syntax variations for `.split()`

You'll see (and can use) a few different ways to work with the result of `.split()`. They all do the same thing — pick whichever is clearest to you!

**1. Store the list, then index into it** (what we've been doing):

```{code-cell} ipython3
email = "joelchan@umd.edu"
parts = email.split("@")
username = parts[0]
print(username)
```

**2. Chain the index directly onto `.split()`** — since `.split()` returns a list, you can index into it right away:

```{code-cell} ipython3
email = "joelchan@umd.edu"
username = email.split("@")[0]
print(username)
```

**3. Unpacking** — if you know exactly how many pieces `.split()` will produce, you can assign them to multiple variables at once:

```{code-cell} ipython3
email = "joelchan@umd.edu"
username, domain = email.split("@")
print(username)
print(domain)
```

Unpacking is handy when you need *all* the pieces. But be careful: if the number of variables doesn't match the number of pieces, you'll get an error!

```{code-cell} ipython3
:tags: [raises-exception]

# this will error — .split("@") gives 2 pieces but we have 3 variables
a, b, c = "joelchan@umd.edu".split("@")
```

Example: get elements of a url.

```{code-cell} ipython3
url = "www.ischool.umd.edu"
elements = url.split(".") # split on the `.` character
elements[1]
```

**PRACTICE**: get elements of a timestamp (get the hour).

```{code-cell} ipython3
# get hour
timestamp = "13:30:31"
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
hour = timestamp.split(":")[0]
print(hour)  # '13'
```

The pieces are separated by `:`, and the hour is the first piece. Remember that `.split()` gives you back strings, so `hour` is `"13"`, not `13`. If you want to do math with it, convert it first: `int(hour)`.
`````

**PRACTICE**: get the words in a sentence.

```{code-cell} ipython3
# get words
message = "She sells seashells by the sea shore, with sea in the wind, and sea in my shoes"
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
words = message.split(" ")
print(words)
```

Words are separated by spaces, so we split on `" "`. Look closely at the result, though: the punctuation stays attached to the words (e.g., `'shore,'` and `'wind,'`). If you wanted to count how many times `"sea"` shows up, you'd want to clean those off first (e.g., with `.replace(",", "")`).
`````

A more complicated example: parse records string into a list of lists!

```{code-cell} ipython3
records_string = "NAME\tSCORE\tGRADE\nJoel\t81\tB-\nRony\t98\tA+\nSravya\t99\tA+"

records = []

for row in records_string.split("\n"):
    row_data = row.split("\t")
    records.append(row_data)
records
```

**PRACTICE**: A more complicated example: parse comma-separated records string into a list of lists!

```{code-cell} ipython3
records_string = "NAME,SCORE,GRADE\nJoel,81,B-\nRony,98,A+\nSravya,99,A+"
records = []
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
for row in records_string.split("\n"):
    row_data = row.split(",")
    records.append(row_data)
records
# [['NAME', 'SCORE', 'GRADE'], ['Joel', '81', 'B-'], ['Rony', '98', 'A+'], ['Sravya', '99', 'A+']]
```

This is the exact same code as the tab-separated example above. The only thing that changes is the separator for each row: `","` instead of `"\t"`.
`````

**PRACTICE**: Given a list of full names, split each into first and last name, and collect just the last names into a list.

```{code-cell} ipython3
full_names = ["Joel Chan", "Sarah Park", "John Smith", "Kacie Lee"]
last_names = []
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
full_names = ["Joel Chan", "Sarah Park", "John Smith", "Kacie Lee"]
last_names = []
for name in full_names:
    last = name.split(" ")[1]
    last_names.append(last)
last_names  # ['Chan', 'Park', 'Smith', 'Lee']
```

You could also use unpacking: `first, last = name.split(" ")`
`````

**PRACTICE**: Given a list of file paths, extract just the file extension (the part after the last `.`) for each one, and collect the unique extensions into a list.

```{code-cell} ipython3
paths = ["data/report.csv", "images/photo.png", "docs/notes.txt", "data/grades.csv", "images/logo.png"]
extensions = []
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
paths = ["data/report.csv", "images/photo.png", "docs/notes.txt", "data/grades.csv", "images/logo.png"]
extensions = []
for path in paths:
    ext = path.split(".")[-1]  # last piece after splitting on "."
    if ext not in extensions:
        extensions.append(ext)
extensions  # ['csv', 'png', 'txt']
```
`````

**PRACTICE**: Given a log string where each entry is separated by `|` and has the format `"LEVEL:message"`, extract only the messages (not the level) from entries where the level is `"ERROR"`.

```{code-cell} ipython3
log = "INFO:started|ERROR:disk full|INFO:retrying|ERROR:timeout|INFO:done"
errors = []
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
log = "INFO:started|ERROR:disk full|INFO:retrying|ERROR:timeout|INFO:done"
errors = []
for entry in log.split("|"):
    level, message = entry.split(":")
    if level == "ERROR":
        errors.append(message)
errors  # ['disk full', 'timeout']
```
`````

#### Practice: Code Tracing with Parsing

Predict the output of each code snippet before running the cell!

##### Trace 1

```{code-cell} ipython3
:tags: [remove-output]

s = "a-b-c-d"
parts = s.split("-")
print(parts)
print(len(parts))
```

- A) `['a-b-c-d']` then `1`
- B) `['a', 'b', 'c', 'd']` then `4`
- C) `['a', '-', 'b', '-', 'c', '-', 'd']` then `7`
- D) `'abcd'` then `4`

````{admonition} Answer:
:class: toggle

**B) `['a', 'b', 'c', 'd']` then `4`**

`.split("-")` splits on every `-` character and removes the separators. The result is a list of the pieces between the dashes.
````

##### Trace 2

```{code-cell} ipython3
:tags: [remove-output]

email = "joel@umd.edu"
domain = email.split("@")[1]
tld = domain.split(".")[1]
print(tld)
```

- A) `umd`
- B) `edu`
- C) `joel`
- D) `umd.edu`

````{admonition} Answer:
:class: toggle

**B) `edu`**

First split: `"joel@umd.edu".split("@")` → `['joel', 'umd.edu']`, index `[1]` → `"umd.edu"`. Second split: `"umd.edu".split(".")` → `['umd', 'edu']`, index `[1]` → `"edu"`.
````

##### Trace 3

```{code-cell} ipython3
:tags: [remove-output]

data = "10,20,30"
nums = data.split(",")
print(nums[0] + nums[1])
```

- A) `30`
- B) `1020`
- C) Error
- D) `10,20`

````{admonition} Answer:
:class: toggle

**B) `1020`**

`.split(",")` returns `['10', '20', '30']` — a list of **strings**, not numbers! So `nums[0] + nums[1]` is string concatenation: `"10" + "20"` → `"1020"`. To get `30`, you'd need `int(nums[0]) + int(nums[1])`.
````

##### Trace 4

```{code-cell} ipython3
:tags: [remove-output]

line = "Joel,81,B-"
name, score, grade = line.split(",")
print(name)
print(type(score))
```

- A) `Joel` then `<class 'int'>`
- B) `Joel` then `<class 'str'>`
- C) `J` then `<class 'str'>`
- D) Error

````{admonition} Answer:
:class: toggle

**B) `Joel` then `<class 'str'>`**

Unpacking assigns each piece of the split to a variable. `.split()` always returns a list of **strings**, even if the content looks numeric. So `score` is `"81"` (a string), not `81` (an integer).
````

##### Trace 5

```{code-cell} ipython3
:tags: [remove-output]

msg = "one two  three"
words = msg.split(" ")
print(words)
print(len(words))
```

- A) `['one', 'two', 'three']` then `3`
- B) `['one', 'two', '', 'three']` then `4`
- C) `['one two  three']` then `1`
- D) `['one', 'two', 'three']` then `4`

````{admonition} Answer:
:class: toggle

**B) `['one', 'two', '', 'three']` then `4`**

There are two spaces between `"two"` and `"three"`. When you split on a single space `" "`, each space is a separator, so the double space produces an empty string `""` between them. This is a common gotcha! If you want to avoid this, use `.split()` with no argument, which splits on *any* whitespace and ignores extra spaces.
````

##### Trace 6

```{code-cell} ipython3
:tags: [remove-output]

path = "home/user/docs/file.txt"
parts = path.split("/")
print(parts[-1])
filename = parts[-1].split(".")
print(filename[0])
```

- A) `file.txt` then `file`
- B) `docs` then `docs`
- C) `file.txt` then `file.txt`
- D) `file` then `file`

````{admonition} Answer:
:class: toggle

**A) `file.txt` then `file`**

First split: `path.split("/")` → `['home', 'user', 'docs', 'file.txt']`. Index `[-1]` → `"file.txt"`. Second split: `"file.txt".split(".")` → `['file', 'txt']`. Index `[0]` → `"file"`.
````

## REMEMBER: STRINGS ARE IMMUTABLE

Remember! Unlike lists, string methods return a new object (and do not modify the original string), since strings are immutable.

This means if you don't assign the return value of the string method to a new variable, the change will be **lost**. Remember this!

```{code-cell} ipython3
a = "Hello"
b = "WORLD"
# these look like they should change a and b...
a.lower()
b.lower()
# ...but they DON'T! a and b are unchanged:
print(a, b)  # still "Hello WORLD"
```

To actually preserve the change, you must reassign:

```{code-cell} ipython3
a = "Hello"
b = "WORLD"
a = a.lower()  # reassign the result back to a
b = b.lower()  # reassign the result back to b
print(a, b)    # now "hello world"
print(a == b)  # still False (different words), but both are lowercase now
```

```{code-cell} ipython3
message = "Hello, my name is Inigo Montoya"
print(message)
# let's check if the message mentions my name!
message = message.lower() # change to lower case
message = message.replace("inigo", "MYSTERY")
print(message)
```

## String formatting

So far we've taken strings as given, and we often specify a string directly. But frequently it is useful to compose a string programmatically, from variables.

Often this is done for debugging (to read the state of your program at various steps), but often this is used as outputs of your program, intermediate or final.

Here's an example

```{code-cell} ipython3
msg = "hello"
friend = "rony"
name = "anna"
output = f"{msg} {friend}, my name is {name}!"
print(output)
```

```{code-cell} ipython3
weight_kgs = 120
print(f"{weight_kgs} is {weight_kgs*2.2} lbs")
```

Example application: a guessing game!

```python
# game parameters
name = "sarah"
attempts = 5
target = 138

# initial guess
guess = input("Guess the number (or type q to quit): ")

# as long as there are attempts remaining
# and the user hasn't said quit
while attempts > 0 and guess != "q":
    # change to number
    guess_num = int(guess)

    # if the guess is correct
    if guess_num == target:
        # congratulate the user
        msg = f"congrats, {name}! {guess} is indeed the number!"
        print(msg)
        # and break out of the loop (no need to keep guessing!)
        break
    # otherwise
    else:
        # subtract 1 from the number of attempts
        attempts -= 1
        # tell the user how many attempts are left
        msg = f"sorry that wasn't right, {name}, you have {attempts} remaining attempts"
        print(msg)
        # get another guess
        guess = input("Take another guess (or type q to quit): ")
```

*Note: this example uses `input()` and requires interactive input. Try running it in your own Python environment!*

Example output:
```
Guess the number (or type q to quit): 3
sorry that wasn't right, sarah, you have 4 remaining attempts
Take another guess (or type q to quit): 5
sorry that wasn't right, sarah, you have 3 remaining attempts
Take another guess (or type q to quit): 138
congrats, sarah! 138 is indeed the number!
```

Here's another example of f-strings used for debugging/tracing:

```{code-cell} ipython3
sales = ["$100", "$250", "$500"]

for i in range(len(sales)):
    sale = sales[i]
    print(f"Processing the item at index {i}: {sale}")
    print(sale)
```

### The basics
Let's look in more detail. The intuition here is that you're defining a series of "slots" for variables. Each slot is indicated with the `{}` curly braces. And you put data / variables in them (which can include expressions that yield data!).

You also indicate that you're doing this slot thing by prefixing the string with the letter `f`

Here's how it looks:

```{code-cell} ipython3
names = ["Joel", "Sarah", "Michael", "Kacie"]
for name in names:
    message = f"Welcome, {name}!"
    print(message)
```

```{code-cell} ipython3
birth_year = 1956
this_year = 2023
name = "Joel"
message = f"Happy birthday, {name}! You are {this_year - birth_year} this year!"
print(message)
```

**PRACTICE**: print out the following message for each row: "{name} got a {grade}"!

```{code-cell} ipython3
records_string = "NAME,SCORE,GRADE\nJoel,81,B-\nRony,98,A+\nSravya,99,A+"
for row in records_string.split("\n")[1:]:
    name, score, grade = row.split(",")
    # add your msg here!
```

`````{admonition} Answer:
:class: toggle

```python
records_string = "NAME,SCORE,GRADE\nJoel,81,B-\nRony,98,A+\nSravya,99,A+"
for row in records_string.split("\n")[1:]:
    name, score, grade = row.split(",")
    msg = f"{name} got a {grade}"
    print(msg)
```

Output:
```
Joel got a B-
Rony got a A+
Sravya got a A+
```

The `[1:]` skips the header row (`"NAME,SCORE,GRADE"`), so we don't print `"NAME got a GRADE"`.
`````

### Controlling the way it looks
You can also control how the string looks! Various things like controlling how many decimal places are printed out (very useful when doing math), or how wide or indented the string is.

```{code-cell} ipython3
# most common
x = 2
y = 3
message = f"{x} divided by {y} is {x/y:.2f}" # only show two decimal places for the float value of result
print(message)
```

The general design pattern here is to put a colon after and then specify some kind of formatting option. More details here: http://zetcode.com/python/fstring/

**PRACTICE**: complete the output message so it prints out something like this: "Please charge my card for \$5.23" (if the total value is 5.23)

```{code-cell} ipython3
tip = 0.18
check = 25.00
total_value = check + check*tip
# complete the output msg
# msg = f"..."
# print(msg)
```

`````{admonition} Answer:
:class: toggle

```python
msg = f"Please charge my card for ${total_value:.2f}"
print(msg)  # Please charge my card for $29.50
```

The `$` is outside the `{}`, so it's just a regular character in the string. Inside the `{}`, `:.2f` shows exactly two decimal places, so we get `29.50` instead of `29.5`.
`````

**PRACTICE**: Given a list of items and prices, print a receipt where each line says `"{item}: ${price:.2f}"` and the last line says `"Total: ${total:.2f}"`.

```{code-cell} ipython3
items = ["Coffee", "Bagel", "Juice"]
prices = [4.5, 3.75, 5.0]
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
items = ["Coffee", "Bagel", "Juice"]
prices = [4.5, 3.75, 5.0]
total = 0
for i in range(len(items)):
    print(f"{items[i]}: ${prices[i]:.2f}")
    total += prices[i]
print(f"Total: ${total:.2f}")
```

Output:
```
Coffee: $4.50
Bagel: $3.75
Juice: $5.00
Total: $13.25
```
`````

**PRACTICE**: Given a CSV-style string of student records, parse it and print a report line for each student: `"{name} scored {score}/100 ({percentage:.1f}%)"` where percentage is the score out of 100.

```{code-cell} ipython3
records_string = "Joel,81\nRony,98\nSravya,74\nKacie,92"
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
records_string = "Joel,81\nRony,98\nSravya,74\nKacie,92"
for row in records_string.split("\n"):
    name, score_str = row.split(",")
    score = int(score_str)
    percentage = score / 100 * 100
    print(f"{name} scored {score}/100 ({percentage:.1f}%)")
```

Output:
```
Joel scored 81/100 (81.0%)
Rony scored 98/100 (98.0%)
Sravya scored 74/100 (74.0%)
Kacie scored 92/100 (92.0%)
```
`````

**PRACTICE**: Given a list of distances in kilometers, print each one converted to miles using the format: `"{km} km = {miles:.1f} miles"` (1 km = 0.621371 miles).

```{code-cell} ipython3
distances_km = [5, 10, 21.1, 42.2]
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
distances_km = [5, 10, 21.1, 42.2]
for km in distances_km:
    miles = km * 0.621371
    print(f"{km} km = {miles:.1f} miles")
```

Output:
```
5 km = 3.1 miles
10 km = 6.2 miles
21.1 km = 13.1 miles
42.2 km = 26.2 miles
```
`````

**PRACTICE**: Given a list of student names and a list of scores, print a numbered roster where each line is: `"{rank}. {name} - {score}/100"` where rank starts at 1.

```{code-cell} ipython3
names = ["Sravya", "Rony", "Joel", "Kacie"]
scores = [99, 98, 81, 92]
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
names = ["Sravya", "Rony", "Joel", "Kacie"]
scores = [99, 98, 81, 92]
for i in range(len(names)):
    print(f"{i + 1}. {names[i]} - {scores[i]}/100")
```

Output:
```
1. Sravya - 99/100
2. Rony - 98/100
3. Joel - 81/100
4. Kacie - 92/100
```
`````

#### Practice: Code Tracing with f-strings

Predict the output of each code snippet before running the cell!

##### Trace 1

```{code-cell} ipython3
:tags: [remove-output]

x = 5
y = 3
print(f"{x} + {y} = {x + y}")
```

- A) `x + y = x + y`
- B) `5 + 3 = 8`
- C) `{5} + {3} = {8}`
- D) `5 + 3 = 53`

````{admonition} Answer:
:class: toggle

**B) `5 + 3 = 8`**

Inside `{}`, Python evaluates the expression. `x` is `5`, `y` is `3`, and `x + y` is `8` (integer addition, not string concatenation, because these are numbers). Text outside `{}` is literal.
````

##### Trace 2

```{code-cell} ipython3
:tags: [remove-output]

name = "Joel"
score = 85
msg = f"{name} got {score}%"
score = 90
print(msg)
```

- A) `Joel got 90%`
- B) `Joel got 85%`
- C) `Joel got score%`
- D) `name got 85%`

````{admonition} Answer:
:class: toggle

**B) `Joel got 85%`**

The f-string is evaluated when it's *created* (line 3), not when it's *printed* (line 5). At creation time, `score` is 85. Changing `score` to 90 afterward doesn't affect the already-created string.
````

##### Trace 3

```{code-cell} ipython3
:tags: [remove-output]

val = 1/3
print(f"{val}")
print(f"{val:.2f}")
```

- A) `0.3333333333333333` then `0.33`
- B) `0.33` then `0.33`
- C) `1/3` then `0.33`
- D) `0.3333333333333333` then `0.3333333333333333`

````{admonition} Answer:
:class: toggle

**A) `0.3333333333333333` then `0.33`**

Without formatting, the full float is printed. `:.2f` means "format as a float with 2 decimal places", so it rounds to `0.33`.
````

##### Trace 4

```{code-cell} ipython3
:tags: [remove-output]

items = ["apple", "banana", "cherry"]
for i in range(len(items)):
    print(f"{i}: {items[i]}")
```

- A) `0: apple` `1: banana` `2: cherry`
- B) `1: apple` `2: banana` `3: cherry`
- C) `apple: 0` `banana: 1` `cherry: 2`
- D) `i: items[i]` (three times)

````{admonition} Answer:
:class: toggle

**A) `0: apple` `1: banana` `2: cherry`**

`range(len(items))` gives `0, 1, 2`. Each iteration, `i` is the index and `items[i]` is the value at that index. The f-string evaluates both expressions.
````

##### Trace 5

```{code-cell} ipython3
:tags: [remove-output]

word = "hello"
print(f"{word.upper()} has {len(word)} letters")
print(word)
```

- A) `HELLO has 5 letters` then `HELLO`
- B) `HELLO has 5 letters` then `hello`
- C) `hello has 5 letters` then `hello`
- D) `HELLO has 5 letters` then Error

````{admonition} Answer:
:class: toggle

**B) `HELLO has 5 letters` then `hello`**

You can call methods and functions inside `{}`. `word.upper()` evaluates to `"HELLO"` and `len(word)` evaluates to `5`. But remember: `word.upper()` returns a *new* string — it doesn't change `word`. So `word` is still `"hello"` on the last line.
````

##### Trace 6

```{code-cell} ipython3
:tags: [remove-output]

price = 49.99
qty = 3
total = price * qty
print(f"Total: ${total:.2f}")
print(f"Per item: ${total/qty:.2f}")
```

- A) `Total: $149.97` then `Per item: $49.99`
- B) `Total: $149.97` then `Per item: $50.00`
- C) `Total: $150.0` then `Per item: $49.99`
- D) `Total: $149.970000` then `Per item: $49.990000`

````{admonition} Answer:
:class: toggle

**A) `Total: $149.97` then `Per item: $49.99`**

`49.99 * 3` = `149.97`. `:.2f` formats it to 2 decimal places → `$149.97`. `total/qty` = `149.97/3` = `49.99`. The `$` outside the `{}` is literal text, not special.
````

For the curious: there was a time when string formatting was done differently (but Python's creators basically tell everyone *not* to use it anymore): just pointing it out as a historical novelty in case you see it in the wild in other people's code (*cough* Joel's code *cough*).

https://realpython.com/python-string-formatting/#1-old-style-string-formatting-operator
