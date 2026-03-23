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

For the curious: there was a time when string formatting was done differently (but Python's creators basically tell everyone *not* to use it anymore): just pointing it out as a historical novelty in case you see it in the wild in other people's code (*cough* Joel's code *cough*).

https://realpython.com/python-string-formatting/#1-old-style-string-formatting-operator
