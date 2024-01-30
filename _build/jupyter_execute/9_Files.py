#!/usr/bin/env python
# coding: utf-8

# # 9: Files

# ## What are files?

# From Python's perspctive, files are data that is outside of the program's main memory. The PY4E textbook calls it "secondary memory".
# 
# Secondary memory is essential, because main memory, which holds all the data you create while your Python program is running, goes away once the program stops.
# 
# Secondary memory is a place to have data that is persistent. Sort of like long-term memory in humans.
# 
# I like this picture from the [PY4E textbook](https://www.py4e.com/html3/07-files) to illustrate the point:
# 
# <img src="https://www.py4e.com/images/arch.svg" height=600 width=800></img>
# 
# The middle box is where the Python program "lives". 
# 
# Sometimes Python needs a way to connect to the outside world: "input and output devices" on the left, "network" (e.g., the internet!) on the right, and "secondary memory" (e.g., the hard drive! files!) on the right.
# 
# So far our programs have been self-contained (except for talking to the outside world via `input()` and `print()`.
# 
# Now we will talk about how to access and write to files in secondary memory so our data can persist beyond a single Python session/program, and also access data that is... more than we can just write into a single Python file or Jupyter cell.

# ## The `open()` function, and the file handle object
# 
# Python interacts with files using the **file handle** object. The `open()` function, as you might suspect, opens a file handle for a file.
# 
# Here is an example. What do you think is in `fhand`?

# In[1]:


fhand = open('assets/mbox-email-receipts.txt', 'r')
print(fhand)


# The main parameters of `.open()` are:
# 1. Path: The *path* to the file you want to connect to
# 2. Mode: A specification of *how* you want to connect (to read, to write, etc.). 
# 
# But its return value is *not* the contents of the file! Instead, its output is a **file handle** object: `io.TextIOWrapper`.
# 
# I like this picture from the PY4E textbook:
# 
# <img src="https://www.py4e.com/images/handle.svg" height=800 width=600></img>
# 
# What kind of thing is it? What does it allow us to do?
# 
# Just like lists have methods like `.append()`, strings have methods like `.upper()` and `.split()`, and dictionaries have methods like `.update()` and `.get()`, file handle objects have key methods that enable us to work with the actual file:
# - read the contents of the file (with `.read()` or `readlines()`)
# - write to the file (with `.write()` or `writelines()`)
# 
# So, in the example above, I've opened a file handle for the mbox-email-receipts.txt file, in the reading mode (`r`), which enables me to use `.read()` to read the contents of the file.
# 
# We'll return to the concepts of mode and operations in a bit. First, we need to understand how to direct python to a file so we can actually open a file handle to it!

# ## File paths
# 
# File paths are a way of giving Python directions to the file's location. 
# 
# In the example above, the file path was `'assets/mbox-email-receipts.txt'`
# 
# There are two parts to a file path: 
# 1. The filename itself.
# 2. The path/directions to the folder it's in "from where you are"
# 
# The filename is obvious, but the path/directions part is not. So let's take a closer look.

# ### Path, aka directions to a folder

# Like in everyday directions, to write the path (directions to the folder that has the file), you need to know:
# 1. Where you are (your current location)
# 2. The target location
# 3. The "directions" to the target location
# 
# The parts of a path are:
# 1. Operations: `..` for "go up a level", and `/` for "open the door / go down to..."
# 2. Names of folders ("rooms")
# 
# So you can think of a path as a route/directions from where you are, to the target folder/room that has the file you want Python to act on.
# 
# In the example above, we have the target location of the `assets` folder, and we give directions to Python to "open the door" (`/`) to the `assets` folder, and that is where it can find the `mbox-email-receipts.txt` file.
# 
# These directions work because we are currently in a room/folder that has the `assets` folder in it. 
# 
# We can use the `os` library to check/change where we are. This helps understand the concept of paths better, I find. It's also a bit of a preview of using libraries, which we'll do more of in Module 4. If you're confused, don't worry! You don't need to use `os` in this module. This is just for us to see where we are.

# In[2]:


import os # get all the data and functions from the os library

cwd = os.getcwd() # show me where i am on the hard drive
current_view = os.listdir() # list all the names of things i can immediately see in my current location

print(f"You are currently in {cwd}\n")
print(f"Here are all the things you can see:")
for thingname in current_view:
    print(thingname)


# ### Practice writing directions (paths) to files!
# 
# Let's open the `newfile2.txt` file in the `other_stuff` folder

# In[3]:


fpath = 'other_stuff/newfile2.txt'
fhand = open(fpath, 'r')
fhand


# Let's open the `newfile3.txt` file in the `a_drawer` folder

# In[7]:


path = 'other_stuff/a_drawer/'
fname = 'newfile3.txt'
fpath = f'{path}{fname}'
fhand = open(fpath, 'r')
fhand


# Let's open the `newfile.txt` file in the `more_stuff` folder

# In[6]:


fpath = '../more_stuff/newfile.txt'
fhand = open(fpath, 'r')
fhand


# ## File handle "mode" (aka access controls/permissions)
# 
# The second parameter of an `open()` function call specifies what you intend to do with the file.
# 
# This part is how the file data structure includes some basic security: you can only write to files you have "write access" to, for example.
# 
# ### Read mode (`r`)

# In[10]:


path = "assets/"
fname = "mbox-email-receipts.txt"
fpath = f"{path}{fname}"

# basic read
# put 'r' as the second argument
fhand = open(fpath, 'r')
fhand.read()


# This is the default. If you don't specify a mode, this is what it defaults to.

# In[15]:


path = "assets/"
fname = "mbox-email-receipts.txt"
fpath = f"{path}{fname}"

# basic read
# put 'r' as the second argument
fhand = open(fpath)
fhand.read()


# ### Write mode (`w`)

# In[21]:


path = "assets/"
fname = "newfile.txt"
fpath = f"{path}{fname}"

# basic write
# put 'w' as the seocnd argument
fhand = open(fpath, 'w')
fhand.write("Hello world, my programming friends!")
fhand.close()


# if you don't put 'w' as the second argument, python doesn't know that you want to write, and will block you from doing so. this is good for security!

# In[22]:


path = "assets/"
fname = "newfile.txt"
fpath = f"{path}{fname}"

fhand = open(fpath, 'r')
fhand.write("Hello world from INST126 SP23 Week 12!")
fhand.close()


# `w` mode also creates a new file if it doesn't already exist at that path. 
# 
# be careful though! if you run it again and do `.write()`, you'll overwrite the file!

# In[24]:


path = "assets/"
fname = "newfile-from-class.txt"
fpath = f"{path}{fname}"

fhand = open(fpath, 'w')
fhand.write("This is a new file from class!")
fhand.close()


# In[27]:


# basic write
# if you don't put 'w' as the second arugment, python doesn't know that you want to write, and will block you from doing so
# good for security
path = "assets/"
fname = "newfile.txt"
fpath = f"{path}{fname}"

fhand = open(fpath, 'w')
# f is now a connection to the file that allows you to write to it
fhand.write("Hello world from INST126 SP23 Week 12!")
fhand.close()


# ### Append mode (`a`)
# 
# This is a variant of the write mode: specifically, it allows you to write, but *only* by adding stuff to the end of the file.

# In[25]:


path = "assets/"
fname = "newfile.txt"
fpath = f"{path}{fname}"

# append to a file
fhand = open(fpath, 'a')
# f is now a connection to the file that allows you to write to it
fhand.write("More stuff from INST126 SP23 Week 12!")
fhand.close()


# There are more advanced ways to specify how you want to connect (e.g., `'rb'` read binary, for when you have weird fileformats). But basic `r` and `w` should cover most of your needs for now.

# ## Operations on files
# 
# Ok, assuming we have the right mode, let's look more closely at how we do things with files.
# 
# ### Reading the contents of a file

# Very often you want to connect to a file because you want to *read* it. There are two ways to do this:
# 1. `.read()` reads in the whole contents of the file as a `string`
# 2. `.readlines()` reads in the whole contents of the file as a `list` of strings
# 
# In both cases, you end up with strings. You can then parse it to do what you want with it.

# In[28]:


# the path
path = "assets/"
fname = "mbox-email-receipts.txt"
fpath = f"{path}{fname}"

# open the file connection and store in f
fhand = open(fpath, 'r') # open the file connection and store in the variable fhand
content_s = fhand.read() # read the contents of the file, and dump into a string called content_s
content_s


# In[29]:


content_s.split("\n")


# In[27]:


# # open the file connection and store in f
fhand = open(fpath, 'r') # open the file connection and store in the variable fhand
# # do this if you know that the structure of the file is basically a list of lines
content_list = fhand.readlines() # read the contents of the file, and dump into a list of strings called content_list
content_list

# content_list = fhand.readlines()
# fhand.close()

# print("content as string from .read()", content_s)
# print("content as list from .readlines()", content_list)


# In the next module we will learn how the `pandas` library connects to files to cover common parsing situations (e.g., I have a spreadsheet, I want to go straight into a `dataframe` for analysis). More on that later! The concepts of accessing files will still apply.

# ### Writing to a file
# 
# Another common use case for connecting to files is to *write* to secondary memory. 
# 
# The main thing to know here is the `.write()` method.
# 
# Think of it as similar to the `print()` function, except it writes to the file instead of the screen.

# In[36]:


path = "assets/"
fname = "newfile5.txt"
fpath = f"{path}{fname}"

# basic write
# put 'w' as the seocnd argument
fhand = open(fpath, 'w')
fhand.write("Hello INST126!") # .write() takes a string as input, and returns the number of characters written, just writes to the file
fhand.write("\n\nAnother line")
# fhand.close()
# numwritten


# You may be told in various places that you need to `.close()` a file to safely exit the connection. As best we can tell, this used to be very true: sometimes data would be lost if the file wasn't closed. But now, in Python 3, we the instructional team have been unable to determine concrete, repeatable consequences of forgetting this *in the context of this course*. However! This can have consequences in very specific circumstances in professional settings: https://realpython.com/why-close-file-python/
# 
# This is why you'll often see code using the `with` pattern, like this.

# In[10]:


path = "assets/"
fname = ""
fpath = f"{path}{fname}"

# once the code inside the with block finishes, Python automatically closes the file
with open(fpath, 'w') as f:
    fhand.write("Hello world! Something new") # .write() takes a string as input, and then doesn't really return any values, just writes to the file


# ### Iterating through a file, similar to readlines

# In[42]:


path = "assets/"
fname = "mbox-email-receipts.txt"
fpath = f"{path}{fname}"

thursday_records = []
fhand = open(fpath, 'r')
for line in fhand:
    if 'Thu' in line:
        thursday_records.append(line)
        
thursday_records


# In[49]:


path = "assets/"
fname = "newfile2.txt"
fpath = f"{path}{fname}"

with open(fpath, 'r') as fhand:
    # use .read()
    fstring = fhand.read()

with open(fpath, 'r') as fhand:
    # use readlines
    flines = fhand.readlines()

# iterate through lines in the file
with open(fpath, 'r') as fhand:
    records = []
    for line in fhand:
        records.append(line)
        
print(fstring)

print(flines)

print(records)


# ### Aside: a reminder of chaining operations

# Consider these common variants of the open + read steps that accomplish them in one line (we previously separated the steps in part to make them clearer). Let's say we have a file named `"some_file.txt"`. This is what it would look like to open and read them in a single line:

# In[51]:


fstring = open("assets/newfile2.txt", "r").read() # read all the contents of the file in as a string
fstring
# flines = open("some_file.txt", "r").readlines() # read the contents of the file in as a list of strings, one for each "line" in the file


# This works because the `open()` function is an expression that produces a file object, which is the kind of thing that can do the `.read()` or `.readlines()` methods. So, we can actually **chain** the `read()` or `readlines()` methods directly on the file object created by the `open()` expression, without bothering to first save the file object to a variable. This is the concept of **chaining methods/functions/operations directly on the result of an expression". 
# 
# Often we do this because we don't want to waste "mental/visible" space on variables we actually don't care about (e.g., often we never want to do anything with the file object later).

# Remember how we saw this with "cleaning" strings? 
# 
# For example, you might want to normalize a string by converting it to uppercase AND remove all leading and trailing whitespace. You can do it in one line like this

# In[ ]:


s_raw = "hello WorlD "

# you can do it like this
s_upper = s_raw.upper()
s_clean = s_upper.strip()

# or like this (skip the intermediate variable)
s_clean = s_raw.upper().strip() # convert to uppercase, which yields an uppercase string, and then chain the .strip() method directly on that string
# instead of first saving in another variable
print(s_clean)

# only get the first four characters, but make sure it's clean and uppercase
first_four = s_raw.upper().strip()[:4]
print(first_four)


# ## Common errors with files

# ### Can't find the file: FileNotFoundError

# In[56]:


fhand = open("mbox-email-receipts.txt", 'r')
print(fhand.read())


# In basically all cases, the issue/mismatch is between your understanding of where the thing is (path) or what its name is (fname) and what you actually told to Python.
# 
# This could be a:
# - Misspelling (remember how literal Python is?)
# - Wrong/missing directions (e.g., missing a folder, or an operation)

# ### Wrong connection type/permission: UnsupportedOperation

# In[62]:


# i said i would write to it
# but i tried to read it
fhand = open("assets/mbox-email-receipts.txt", 'r')
print(fhand.read())
fhand.close()


# In[58]:


# i said i would read it
# but i tried to write to it
fhand = open("assets/mbox-email-receipts.txt", 'r')
print(fhand.write("Hello world"))


# In[63]:


import os
os.listdir()


# In[ ]:




