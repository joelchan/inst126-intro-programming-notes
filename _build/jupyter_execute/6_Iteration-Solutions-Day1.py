#!/usr/bin/env python
# coding: utf-8

# # 6: Iteration
# 
# ## What are loops and why should we care about them?

# Loops are a fundamental building block of comptutational solutions to problems. They are an example of a **control structure**. Conditionals are another example of control structures.
# 
# Control structures allow you to control *when/whether* (conditional) and *how many times* (loops) you do things

# It's hard to build programs without a concise way to instruct the computer to do *repeated actions*.
# 
# Here are some simple examples. Try to think of how you might solve these without loops!
# - Put 6 cups of flour into this box
# - Stir occasionally until the sauce starts to reduce

# In[1]:


def scoop_into_box():
    print("Scooping!")


# In[2]:


scoop_into_box()
scoop_into_box()
scoop_into_box()
scoop_into_box()
scoop_into_box()
scoop_into_box()


# In[3]:


def stir():
    print("stirring")

def check_sauce():
    print("Checking sauce")
    
stir()
if check_sauce() == "thick":
    stir()
    if check_sauce() == "thick":
        stir()
        if check_sauce() == "thick":
            stir()


# With loops these get a LOT easier to specify, and become more robust and reusable too.

# In[4]:


#
for i in range(3):
    scoop_into_box()


# In[5]:


# 
while check_sauce() == "thick":
    stir()


# Loops also enable many useful algorithms/patterns that go nicely with lists. You'll be practicing and applying them in PCEs and Projects this module!
# 
# For example:
# - Searching through a list
# - Filtering a list of items
# - Counting occurrences in some collection

# Continuing with our running example for this module, here are loops in the context of a program:

# In[6]:


# key variables:
# the input LIST of strings
inputs = [
    "hello sarah@umd.edu",
    "from: joelchan@umd.edu",
    "some other text that doesn't have an email"
]
# a LIST to store the email addresses
emails = []

# LOOP over every text input
for text_input in inputs:
    
    # extract an email address
    # split the text into subsets
    chunks = text_input.split()
    
    # LOOP over the list of chunks to check each one
    for chunk in chunks:
        # check if it has @ and .
        if "@" in chunk and "." in chunk:
            # put the chunk in the email list
            emails.append(chunk)
# give the email address back to the user
print(emails)


# ## Definite loops (for loops)

# Quite often we have a list of items of the lines in a file - effectively a finite set of things. We can write a loop to do some operation once for each of the items in a set using the Python for construct.
# 
# These loops are called “*definite loops*” because they execute an exact number of times. We say that “definite loops iterate through the members of a set”
# 
# Use definite/for when you know in advance how many times you want to do something.
# 
# This is the use case in our running example.
# 
# Other examples:
# - Do an action N times
# - Take M steps
# - Do something for every item in a finite list

# ### Anatomy of a definite (for) loop in Python

# Let's take a closer look.
# 
# - The **iteration variable** "iterates" through the **sequence** (ordered set)
# - The **block (body)** of code is executed once for each value **in** the **sequence**
# - The **iteration variable** moves through all of the values in the **sequence**

# In[7]:


nums = [5, 4, 3, 2, 1]
# here, i is the iteration variable

n = nums[0]
n = nums[1]
n = nums[2]

for n in nums: 
    print("taking something from the list")
    print(n) # block/body


# In[ ]:





# In[8]:


nums = [5, 4, 3, 2, 1]
# here, i is the iteration variable
for i in nums: 
    print(i)
    new_num = i*20
    print(new_num) # block/body


# The iteration variable is a *variable*: this means you can name it whatever you like, subject to the basic syntax rules and of course our heuristic to name things to make the logic of the program legible.

# In[9]:


nums = [5, 4, 3, 2, 1]
# here, num is the iteration variable
for a_number in nums: 
    new_num = a_number*20
    print(new_num) # block/body


# In[10]:


nums = [5, 4, 3, 2, 1]
# here, num is the iteration variable
for num in nums:
    if num % 2 == 0: # check if even
        print(num) # block/body


# In[11]:


for name in ["john", "terrell", "qian", "malala"]:
    print(name)


# In[12]:


# the range function produces an iterable sequence of numbers
# that start at the optional first argument, and stop before
# the required second argument
# https://www.w3schools.com/python/ref_func_range.asp
list(range(0,5))


# In[13]:


# use this if you want to specify doing something N times
# e.g., here, take a step 5 times
for i in range(7):
    print("I has the value", i)
    print("Taking a step")


# In[14]:


# use this if you want to specify doing something N times
# e.g., here, take a step 5 times
for i in [0,1,2,3,4]:
    print("I has the value", i)
    print("Taking a step")


# In[15]:


# scoop 6 cups
steps = 6
for step in range(steps):
    print("scooping cup number", step+1)


# Let's take a closer look in [python tutor](http://www.pythontutor.com/visualize.html#mode=edit)
# 
# 

# ### Common design patterns with definite loops

# #### Counting
# 
# A common situation: you have a list of stuff, and you want to count how many times a certain kind of thing shows up in that list. 
# 
# If you want to count occurrences based on a simple exact match, you can use the `.count()` list method.

# In[16]:


names = ["Joel", "John", "Jane", "Jamie", "John", "Michael", "Sarah", "Joseph", "Chris", "Ray"]
# count how many times "John" is in here
names.count("John")


# But often you want to count based on something more complex than an exact match. For example, let's say I want to count the number of "high performers" in a list of scores (where high performing means score of 95 or greater).
# 
# Iteration is a really helpful way to do this.

# In[17]:


# 
scores = [65, 78, 23, 97, 100, 25, 95] # input list

threshold = 67 # score of C

n_highperformers = 0 # define the count variable, initialize to 0

# go through each item
for score in scores: 
    # check if meets my criteria for being counted
    if score >= threshold: 
        # if so, increase count
        n_highperformers += 1 
print(n_highperformers)


# The generic pattern (or algorithm) is something like this:

# In[18]:


# initialize count variable

# for every item in list
    # check if meets my criteria for being counted
        # if so, increase count


# Practice: let's say I have a list of names, and I want to count how many names don't start with the letter J.

# In[19]:


names = ["Joel", "John", "Jane", "Jamie", "Johnny", "Michaela", "Sarah", "Joseph", "Chris", "Ray"]

target_letter = "J"

# initialize count variable
num_target_names = 0

# for every item in list
for name in names:
    # check if we should count it
    if name.startswith("J"):
        # increase count if it checks out
        num_target_names += 1


# Practice: count how many names are short (e.g., 4 characters or less)? Or long (e.g., more than 5 characters).

# In[20]:


len("Joel")


# In[21]:


names = ["Joel", "John", "Jane", "Jamie", "Johnny", "Michaela", "Sarah", "Joseph", "Chris", "Ray"]

# initialize count variable
num_long = 0

# for every item in list
for name in names:
    # check if we should count it
    if len(name) > 5: 
        # increase count if it checks out
        num_long += 1
        
print(num_long)


# Practice: check how many times we have a "banned" name.
# *hint: how do we check if an item is in a list?

# In[22]:


names = ["Joel", "John", "Jane", "Jamie", "Johnny", "Michaela", "Sarah", "Joseph", "Chris", "Ray"]

banned = ["Joel", "Chris"]

# initialize count variable
num_banned = 0

# for every item in list
for name in names:
    # check if we should count it
    if name in banned: 
        # increase count if it checks out
        num_banned += 1
        
print(num_banned)


# #### Filtering
# 
# A closely related situation is where we want to not only count, but also "grab" or *filter* the things that meet our criteria.
# 
# We'd want to create a new list, and make sure we have a bit of code that adds to that new list based on the criteria we have.
# 
# Example: grab all scores that cross our threshold.

# In[23]:


scores = [65, 82, 23, 97, 100, 95] # input list to be filtered

threshold = 93 # the criterion

# initialize empty list to hold filtered items
to_grab = [] 

# go through each item
for score in scores: 
    # check if item meets criteria for being filtered
    if score >= threshold: 
        # if so, add the item to the output list
        to_grab.append(score) 

print(to_grab)


# The generic pattern is something like this:

# In[24]:


# initialize empty list to hold filtered items

# go through each item
    # check if item meets criteria for being filtered
        # if so, add the item to the output list


# Let's grab all the names that start with the letter J.

# In[25]:


names = ["Joel", "John", "Lane", "Jamie", "Freddy"]

target_letter = "J"

# initialize list variable
target_names = []

# for every item in list
for name in names:
    # check if we should count it
    if name.startswith("J"):
        # if so, add the item to the output list
        target_names.append(name)


# Or grab only the names that aren't in our banned list.

# In[26]:


names = ["Joel", "John", "Jane", "Jamie", "Johnny", "Michaela", "Sarah", "Joseph", "Chris", "Ray"]

banned = ["Joel", "Chris"]

# initialize list variable
target_names = []

# for every item in list
for name in names:
    # check if we should count it
    if name not in banned:
        # if so, add the item to the output list
        target_names.append(name)
        
target_names


# Just a reminder that you can use the `filter()` function if you're curious, BUT YOU DO NOT HAVE TO. This is just an extra thing if you're curious

# In[27]:


scores = [65, 82, 23, 97, 100, 95] # input list to be filtered
threshold = 80

to_grab = list(filter(lambda x: x >= threshold, scores))
print(to_grab)


# #### Mapping / transforming
# 
# Finally, sometimes you want to modify some/all elements in a list into a new list. An example might be data cleaning, or data transformation.

# Convert to percentages.

# In[28]:


scores = [65, 82, 23, 97, 100, 95]

# output list
percentages = []

# go through every item
for score in scores:
    # apply the transformation
    percent = score/100
    # add the transformed value to the output list
    percentages.append(percent)
percentages


# The generic pattern is something like this

# In[29]:


# initialize empty list to hold transformed items

# go through each item
    # apply transformation to item
    # add transformed item to transformed items list


# Practice: Change outliers (those above 1000) to missing ("NA")

# In[30]:


scores = [65, 82, 2323, 97, 100, 95000]

# initialize empty list to hold transformed items

# go through each item
for i in range(len(scores)):
    # apply transformation to item
    # add transformed item to transformed items list


# Practice: Change the list from scores to grades.

# In[ ]:


scores = [65, 82, 23, 97, 100, 95] # input list to be filtered

# initialize empty list to hold transformed items

# go through each item
    # apply transformation to item
    # add transformed item to transformed items list


# As an extra thing to try, you can use the `map()` built-in function to do this too!

# In[ ]:


scores = [65, 82, 23, 97, 100, 95]
percentages = list(map(lambda x: x/100, scores))
percentages


# #### Coordinated iteration across multiple sequences
# 
# One of the Project problems relies on a design pattern I haven't yet explicitly shown you in clear terms. So I want to quickly review it. 
# 
# How do you go through the elements of a list, index by index? I'll show you a form of this, and you can figure out how this might generalize to the rock paper scissors problem, where you need to go through two lists in lockstep (first item from both lists, then second item from both lists, and so on)

# In[ ]:


# basic iteration through a list using indices
names = ["Joel", "John", "Lane", "Jamie", "Freddy"]
eligibilities = [True, False, True, True, False]

# make a list of numbers that start at 0, and stop before
# the length of the names list
# and go through every number in that list
for index in range(len(names)):
    # use the number as an index for the first list
    name = names[index]
    # use the same number as an index for the second list
    eligible = eligibilities[index]
    # do something with the items at the same index position for both lists
    print(name, eligible)


# The generic pattern is something like this:

# In[ ]:


# make a list of numbers that start at 0, and stop before
# the length of one of the lists (assuming they are the same length!)
# and go through every number in that list
    # use the number as an index for the first list
    # use the same number as an index for the second list
    # do something with the items at the same index position for both lists


# ## Indefinite loops (while loops)
# 
# Sometimes you want to repeat actions, but you don't know in advance how many times you want to repeat. But you do have a *stopping condition*. In this situation, you can use indefinite loops, which are called so because they keep going until a logical condition becomes `False`.
# 
# Examples:
# - Keep going until I tell you to stop
# - Keep stirring until the sauce thickens
# - Keep taking candy from the box until your bucket is full or the box is empty
# 
# Use indefinite/while when you don't know in advance how many times you want to do something, but do have a stopping condition you can clearly express.

# ### Anatomy of an indefinite (while) loop in Python

# - The **stopping condition** defines when the loop will stop and go to the next block of code
#   - It's composed of a *Boolean expression*
#   - It should be possible for the Boolean expression to be `False`!
# - The **block (body)** of code is executed once for each iteration in the loop
# - **Stopping condition update**: It is essential that the body of the loop has some operation it that modifies what is checked in the stopping condition

# In[ ]:


# keep taking steps until you hit a limit
steps = 0
limit = 20
# check stopping condition
while steps < limit: 
    # body of the loop (aka do some stuff)
    print("Taking a step", steps)
    # stopping condition update
    steps += 1 # 
print("Done!")


# Generic pattern:

# In[ ]:


# check stopping condition
    # body of the loop (aka do some stuff)
    # stopping condition update


# In[ ]:


guess = input("Try to guess the number between 1 and 10, or say `exit` to quit")
number = 5
found = False
while guess != "exit" and not found:
    if int(guess) == number:
        print("You got it!")
        found = True
    else:
        guess = input("Try to guess the number between 1 and 10, or say `exit` to quit")


# Let's take a closer look in [python tutor](http://www.pythontutor.com/visualize.html#mode=edit)

# ### Some applications of indefinite loops

# #### Generically: keep doing something until...
# 
# Keep adding characters to a string until it is a defined length, e.g., 10

# In[ ]:


input_string = "abc"

# check stopping condition
while len(input_string) < 10:
    # body of the loop (aka do some stuff)
    input_string = input_string + "a"
    # stopping condition update (not needed because we're modifying the thing being checked)
    
print(input_string)
print(len(input_string))


# Keep adding "." to the string until it is 13 characters long.

# In[ ]:


input_string = "abc"

# check stopping condition
    # body of the loop (aka do some stuff)
    # stopping condition update
    
print(input_string)


# Keep dividing a number by 2 until we can't anymore.

# In[ ]:


num = 12000

# check stopping condition
    # body of the loop (aka do some stuff)
    # stopping condition update
    
print(num)


# Example: get me 2 people named "John".

# In[ ]:


names = ["Joel", "John", "Jane", "Jamie", "John", "Michaela", "Sarah", "John", "Chris", "John"]


# #### Basic user interfaces (keep running program until user stops us.
# 
# Guessing game.

# In[ ]:


guess = input("Try to guess the number between 1 and 10, or say `exit` to quit")
number = 5
while guess != "exit":
    if int(guess) == number:
        print("You got it!")
        break # we're done, exit the loop
    else:
        guess = input("Try to guess the number between 1 and 10, or say `exit` to quit")
print("Thanks for playing!")


# In[ ]:


# check stopping condition
    # body of the loop (aka do some stuff)
    # stopping condition update


# #### All of the definite loops we saw earlier can be implemented with indefinite loops!

# In[ ]:





# ## Breaking a loop with the `break` statement

# The break statement ends the current loop and jumps to the statement immediately following the loop. 
# It is like a loop test that can happen anywhere in the body of the loop
# 

# In[ ]:


found = False # default is we hvaen't found it
names = ["Joel", "John", "Jane", "Jamie", "Lisa", "Anna", "Fred"]
for name in names:
    print(name)
    if name == "John":
        found = True # set found to true
        print("Found!")
        break
print("We're done with the loop")
if found:
    print("Found john!")
else:
    print("Didn't find john")


# In[ ]:


found = False # default is we hvaen't found it
names = ["Joel", "John", "Jane", "Jamie", "Lisa", "Anna", "Fred"]

name = names.pop()
while not found:
    print(name)
    if name == "John":
        found = True
        print(found)
        break
    else:
        if len(names) > 0:
            name = names.pop()

if found:
    print("Found john!")
else:
    print("Didn't find john")


# In[ ]:


while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')


# ## Common errors

# ### Indentation is key!
# 
# The way that Python knows what counts as the body of code for a loop (whether definite or indefinite) is through indentation. 
# 
# You must indent all code that goes in the body underneath the for/while statement (after the colon).
# 
# If you fail to indent the first line of code in the body, you will get an IndentationError.
# 
# If you fail to indent anything after the first line of code in the body, you will be committing a semantic error: Python will not alert you because it is legal code. But your program will probably malfunction.

# In[ ]:


for i in range(5):
print(i)


# In[ ]:


# i want to step through a list of numbers, multiply each of them by 5 and print htem out
nums = [1,2,3,4,5]
for num in nums:
  new_num = num*5
  print(new_num)


# ### IndexError when looping through a list
# 
# This comes up mostly with `while` loops. So, while it's possible to do any for loop with a while loop, you want to be careful with it.
# 

# In[ ]:


#
#
#
names = ["Joel", "John", "Jane", "Jamie", "John"]
to_grab = [] # output list, initialize to empty list

index = 0 # set initial index to zero
while index < 10: # until you reach the end of the list
  print(index)
  name = names[index] # get the name at this index
  if name == "John": # check if is john / meets my criteria for being filtered
    to_grab.append(name) # add the item to the output list
  index += 1 # increment the index

# print out the result
print(to_grab)


# In[ ]:


# basic iteration through a list using indices
names = ["Joel", "John", "Lane", "Jamie", "Freddy"]

for index in range(6):
  name = names[index]
  print(index, name)


# ### Infinite loops
# 
# Remember that with indefinite loops, we need the **stopping condition** to be `False` at some point. Or at least, give the loop a way to exit / `break`. Otherwise, it will go forever! A common error is to forget to include any block of code in the **body (block)** of the loop that modifies the **stopping condition** or provides a **break** condition.

# In[ ]:


# 
n = 5
while n > 0:
  print(n)
  n = n - 1
print("Blast off!")


# In[ ]:


# 
n = 5
while n > 0:
  print(n)
  n = n-1
print("Blast off!")


# In[ ]:


#
#
#
names = ["Joel", "Jane", "Jamie"]
to_grab = [] # output list, initialize to empty list

index = 0 # set initial index to zero
while len(to_grab) == 0: # until you reach the end of the list
    print(index)
    name = names[index] # get the name at this index
    if name == "John": # check if is john / meets my criteria for being filtered
        to_grab.append(name) # add the item to the output list
    index += 1 # increment the index

# print out the result
print(to_grab)

