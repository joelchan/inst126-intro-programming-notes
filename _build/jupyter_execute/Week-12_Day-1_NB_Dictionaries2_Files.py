#!/usr/bin/env python
# coding: utf-8

# # The indexing pattern with files and dictionaries

# ## Motivating use case: index data from a file for later search
# 
# Very similar to the theme of Project 3.
# 
# Let's say we have this file: https://drive.google.com/file/d/1dY7tFf8H-TcUdiZQ90X-SPIkGIBhYsRD/view?usp=sharing (it's also in the `/resources/` directory.
# 
# It contains a list of email receipts. I want to know how many emails came to me from which email addresses.
# 
# I can use the indexing pattern to do this, plus a way to access the file system.

# ### Problem formulation
# 
# https://miro.com/app/board/uXjVO9Pn42E=/?share_link_id=262351000292
# 
# <img src="../resources/email-indexing-problem-formulation.png" height=800 width=1200></img>

# In[1]:


# in comments

# READ data from the file into list

# loop over the list
    # PARSE the record
    # UPDATE the index info for the record


# ### Writing the code

# In[2]:


def filter_string(s, cue):
    # split into elements
    elements = s.split(" ")
    # go through and find the element that has the cue
    for e in elements:
        # if cue in the element
        if cue in e:
            # give us the thing
            return e


# In[3]:


line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
target = filter_string(line, ":")
target


# In[4]:


# READ data from the file into list
# where is the file?
fpath = '../resources/mbox-email-receipts.txt'
# open the file
f = open(fpath, 'r')
# read the file's contents into a list
records = f.readlines()

# make the index
index = {}

# loop over the list
for r in records:
    # PARSE the record
    email_address = filter_string(r, '@')
    
    # UPDATE the index info for the record

    # GET the current value of the key (email)
    # default to zero if not found
    count = index.get(email_address, 0)
    # UPDATE the value
    count += 1
    # UPDATE the index with the key and updated value
    index.update({email_address: count})
    
index


# # Fundamental concept: Files

# ## What are files?

# A special Python data structure that provides an interface and container for data that is outside of your program's main memory. The PY4E textbook calls it "secondary memory".
# 
# Secondary memory is essential, because main memory, which holds all the data you create while your Python program is running, goes away once the program stops.
# 
# Secondary memory is a place to have data that is persistent. Sort of like long-term memory in humans.

# ## Key operations on files

# ### Open a file

# In[22]:


f = open('../resources/mbox-email-receipts.txt', 'r')
f


# `open()` function, as you might suspect, opens a connection to the file.
# 
# Its parameters are:
# 1. The *path* to the file you want to connect to
# 2. A specification of *how* you want to connect (to read, to write, etc.). 
# 
# And its output is a file connection object: `io.TextIOWrapper`

# #### Specifying a path to a file
# 
# The first bit is about giving Python directions to the file's location. This is the concept of a *path*.
# 
# There are two parts to a path: the folder it's in, and then the filename itself.

# In[12]:


fpath = '../resources/mbox-email-receipts.txt'
fdir = '../resources/'


# In[3]:


f = open(fpath, 'r')
f.read()


# What is a path? Let's look at some pictures and write a definition together.

# Now let's practice! I'll move the file around, and let's modify the path to match it.

# In[27]:


fpath = 'newfolder/mbox-email-receipts.txt'
f = open(fpath, 'r')
f.read()


# #### Specifying a connection type/permission
# 
# The second bit is how the file data structure includes some basic security: you can only write to files you have "write access" to, for example.
# 
# Let's look at an example.

# In[2]:


# basic read
# put 'r' as the second argument
f = open(fpath, 'r')
print(f.read())


# In[31]:


# basic write
# put 'w' as the seocnd argument
f = open(fpath, 'w')
print(f)
f.write("Hello world!")
f.close()


# In[ ]:


# basic write
# if you don't put 'w' as the second arugment, python doesn't know that you want to write, and will block you from doing so
# good for security
f = open(fpath, 'r')
# f is now a connection to the file that allows you to write to it
f.write("Hello world from INST126 SP21 Week 11 at 9:30am!")
f.close()


# In[ ]:


# basic write
# if you don't put 'w' as the second arugment, python doesn't know that you want to write, and will block you from doing so
# good for security
f = open(fpath, 'w')
# f is now a connection to the file that allows you to write to it
f.write("Hello world from INST126 SP21 Week 11 at 9:30am!")
f.close()


# In[ ]:


# append to a file
f = open(fpath, 'a')
# f is now a connection to the file that allows you to write to it
f.write("More stuff from INST126 SP21 Week 11 at 9:33am!")
f.close()


# There are more advanced ways to specify how you want to connect (e.g., `'rb'` read binary, for when you have weird fileformats). But basic `r` and `w` should cover most of your needs for now.

# ### Reading the contents of a file

# Very often you want to connect to a file because you want to *read* it. There are two ways to do this:
# 1. `.read()` reads in the whole contents of the file as a `string`
# 2. `.readlines()` reads in the whole contents of the file as a `list` of strings
# 
# In both cases, you end up with strings. You can then parse it to do what you want with it.

# In[35]:


# the path
fpath = '../resources/mbox-email-receipts.txt'

# open the file connection and store in f
# fhand = open(fpath, 'r') # open the file connection and store in the variable fhand
# content_s = fhand.read() # read the contents of the file, and dump into a string called content_s
# content_s

# # open the file connection and store in f
fhand = open(fpath, 'r') # open the file connection and store in the variable fhand
# # do this if you know that the structure of the file is basically a list of lines
content_list = fhand.readlines() # read the contents of the file, and dump into a list of strings called content_list
content_list

# content_list = f.readlines()
# f.close()

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


# basic write
# put 'w' as the seocnd argument
f = open(f'{fdir}/test2.txt', 'w')
f.write("Hello INST126!") # .write() takes a string as input, and then doesn't really return any values, just writes to the file
f.close()


# You may be told in various places that you need to `.close()` a file to safely exit the connection. As best we can tell, this used to be very true: sometimes data would be lost if the file wasn't closed. But now, in Python 3, we the instructional team have been unable to determine concrete, repeatable consequences of forgetting this. So.
# 
# 
# 
# But you can avoid this by using the `with` pattern, like this.

# In[10]:


# once the code inside the with block finishes, Python automatically closes the file
with open(f'{fdir}/test2.txt', 'w') as f:
    f.write("Hello world! Something new") # .write() takes a string as input, and then doesn't really return any values, just writes to the file


# ### Iterating through a file, similar to readlines

# In[37]:


fhand = open(fpath, 'r')
for line in fhand:
    if 'Thu' in line:
        print(line)


# ### Aside: chaining operations

# Consider these common variants of the open + read steps that accomplish them in one line (we previously separated the steps in part to make them clearer). Let's say we have a file named `"some_file.txt"`. This is what it would look like to open and read them in a single line:

# In[ ]:


fstring = open("some_file.txt", "r").read() # read all the contents of the file in as a string
flines = open("some_file.txt", "r").readlines() # read the contents of the file in as a list of strings, one for each "line" in the file


# This works because the `open()` function is an expression that produces a file object, which is the kind of thing that can do the `.read()` or `.readlines()` methods. So, we can actually **chain** the `read()` or `readlines()` methods directly on the file object created by the `open()` expression, without bothering to first save the file object to a variable. This is the concept of **chaining methods/functions/operations directly on the result of an expression". 
# 
# Often we do this because we don't want to waste "mental/visible" space on variables we actually don't care about (e.g., often we never want to do anything with the file object later).
# 
# Another common situation for this might be parsing a string. For example:

# In[ ]:


# suppose we have an email
email = "joelchan@umd.edu"

# do this if you care about the elements
elements = email.split() # store result of split operation in elements variable
username = elements[0] # do the indexing operation on the list of elements
server = elements[1]

# do this if you only care about the username
# we could grab it directly from the output of a .split() expression by chaining an index operation ([0]) directly on the output of the .split() expression (which is a list)
# instead of saving that list in a variable and then doing the index operation on that variable
username = email.split()[0]
# this makes sense if we don't care about the list enough to use it more than once.


# Another very common situation is "cleaning" strings. For example, you might want to normalize a string by converting it to uppercase AND remove all leading and trailing whitespace. You can do it in one line like this

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

# In[39]:


f = open("mbox-email-receipts.txt", 'r')
print(f.read())


# ### Wrong connection type/permission: UnsupportedOperation

# In[40]:


# i said i would write to it
# but i tried to read it
f = open("mbox-email-receipts.txt", 'w')
print(f.read())


# In[41]:


# i said i would read it
# but i tried to write to it
f = open("mbox-email-receipts.txt", 'r')
print(f.write("Hello world"))


# # Fundamental concept: The indexing pattern with dictionaries
# 
# Now let's consider the indexing pattern, first by talking about its major components, then generalizing it by looking at different ways to index a file, but still with the same pattern

# In[ ]:


# READ data from the file into list
# where is the file?
fpath = '../resources/mbox-email-receipts.txt'
# open the file
f = open(fpath, 'r')
# read the file's contents into a list
records = f.readlines()

# make the index
index = {}

# loop over the list
for r in records:
    # PARSE the record
    email_address = filter_string(r, '@')
    
    # UPDATE the index info for the record

    # GET the current value of the key (email)
    # default to zero if not found
    count = index.get(email_address, 0)
    # UPDATE the value
    count += 1
    # UPDATE the index with the key and updated value
    index.update({email_address: count})
    
index


# Suppose we want to map email addresses to the times they came in. How would we change the indexing pattern?

# In[43]:


# READ data from the file into list
# where is the file?
fpath = '../resources/mbox-email-receipts.txt'
# open the file
f = open(fpath, 'r')
# read the file's contents into a list
records = f.readlines()

# make the index
index = {}

# loop over the list
for r in records:
    # PARSE the record
    # get the email address
    email_address = filter_string(r, '@')
    # get the time stamp
    time_stamp = filter_string(r, ":")
    
    # UPDATE the index info for the record

    # GET the current value of the key (email)
    # default to [] if not found
    time_stamps = index.get(email_address, [])
    # UPDATE the value
    time_stamps.append(time_stamp)
    # UPDATE the index with the key and updated value
    index.update({email_address: time_stamps})
    
index


# Suppose we want to map hours of the day to the list of email addresses that emailed us at that hour. How would we change the indexing pattern?

# In[44]:


# READ data from the file into list
# where is the file?
fpath = '../resources/mbox-email-receipts.txt'
# open the file
f = open(fpath, 'r')
# read the file's contents into a list
records = f.readlines()

# make the index
index = {}

# loop over the list
for r in records:
    # PARSE the record
    # get the email address
    email_address = filter_string(r, '@')
    # get the time stamp
    time_stamp = filter_string(r, ":")
    # get the hour, which is the first element after we split on the :
    hour = time_stamp.split(":")[0]
    
    # UPDATE the index info for the record

    # GET the current value of the key (hour)
    # default to [] if not found
    emails = index.get(hour, [])
    # UPDATE the value
    emails.append(email_address)
    # UPDATE the index with the key and updated value
    index.update({hour: emails})
    
index


# Suppose we want to know how many times you've gotten emails from each email domain. How would you modify this pattern?

# # Reminder: consequences of dictionary mutability

# Recall that for immutable data structures like strings, anytime you want the changes you are making to the data structure to persist, you need to save the results in a variable
# 
# The OPPOSITE is true for mutable data structures like lists and dictionaries. Any method that modifies these data structures do so directly; they change the data structure itself, and consequently do not return any values.

# In[ ]:


# let's say we have a dictionary d1
d1 = {
    'a': 1,
    'b': 2
}
print(type(d1))
# if we want to update the dictionary, we can do this
d2 = d1.update({'c': 3}) # updating will return None, because dictionaries are mutable
print(d2)
print(type(d2))
d2.get("a")
# if you want to update d1 and assign the resulting dictionary to d2, do this
d2 = d1
print(type(d2))
print(d2)

