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

**PRACTICE**: How would you get the first initial for each name?

```{code-cell} ipython3
names = ["Joel", "Sarah", "John", "Michael", "Patrick", "Kacie"]
# your code here
```

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

**PRACTICE**: How would you get the first 2 letters of the name?

```{code-cell} ipython3
name = "Michelle"
# your code here
```

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

#### Put it into our filtering pattern!

**PRACTICE**: Only grab the classes from CMSC

```{code-cell} ipython3
course_codes = ["INST201", "INST126", "INFM322", "CMSC126"]

target_courses = []

# your code
```

**PRACTICE**: Only grab the emails that are from `.edu` domain

```{code-cell} ipython3
emails = ["oasislab@gmail.com", "joelchan@terpmail.umd.edu", "rony@terpmail.com", "joelchan@umd.edu", "joelchan@gmail.com", "sarahp@umd.edu", "sarah@umd.org"]
target_emails = []

# your code here
```

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

**PRACTICE**: Use `.endswith()` to only grab the emails that are from `.edu` domain

```{code-cell} ipython3
emails = ["oasislab@gmail.com", "joelchan@terpmail.umd.edu", "rony@terpmail.com", "joelchan@umd.edu", "joelchan@gmail.com", "sarahp@umd.edu", "sarah@umd.org"]

target_emails = []
# your code
```

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

### "Cleaning" / normalizing a string

Often we get data in string form, and we need to make sure it conforms to our expectations. Sometimes this means we modify it.

Common methods include:
- `.lower()` or `.upper()` - convert the string to all lowercase or uppercase so we eliminate differences that have to do with case; remember that `A` and `a` are *different* to Python!
- `.replace()` - replace parts of a string with something else - often we use this to strip out characters we don't like (by replacing them with a blank string)
- `.strip()` - remove hidden whitespace at the beginning and end of strings. super handy in data cleaning scenarios! closely related are `.lstrip()` and `.rstrip()` (can you guess what they do?)

Note: you can "chain" methods, and often want to do so! Often this is handy to "bundle together" cleaning/normalizing operations.

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

**PRACTICE**: get the words in a sentence.

```{code-cell} ipython3
# get words
message = "She sells seashells by the sea shore, with sea in the wind, and sea in my shoes"
# your code here
```

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
