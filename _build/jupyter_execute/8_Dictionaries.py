#!/usr/bin/env python
# coding: utf-8

# # 8: Dictionaries
# 
# ## What are dictionaries and why should we care about them?

# Dictionaries are for **associating data** and **quick lookup**

# Motivating example: I am making an index for a book, because I want to know which concepts show up on which pages, to make it easier to jump back to the right spots.

# In[1]:


# how to know which chapters talk about strings? or debugging?
book = [
  "Chapter 1: talks about strings and how they have the property of immutability also some basic debugging",
  "Chapter 2: continues talking about advanced methods for strings and also introduces the concept of functions",
  "Chapter 3: discusses iteration and lists and also debugging",
]


# Here's what it might look like *without* dictionaries.

# In[2]:


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


# In[3]:


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


# And here is what it might look like *with* dictionaries.

# In[4]:


# now consider if the concept index is in a dictionary (much more like what you might see in a book!)
index_d = {
    'strings': ['Chapter 1', 'Chapter 2'],
    'debugging': ['Chapter 1', 'Chapter 3']
}


# In[5]:


# given this data structure, how to find 
# all the chapters that have strings in them?
query = "strings"
index_d.get("strings")


# Another common use case: attributes of data entries. For instance, attributes of a class, like credit hours, pre-reqs, instructor, location, hours, and so on.

# In[6]:


# without dictionaries
courses = [
    ["INST126", 3, "no", "Chan", "hybrid", "MWF"],
    ["INST256", 4, "yes", "Kanishka", "in-person", "TR"]
]

# look up INST126 and check whether it has prereqs
for course in courses:
    if course[0] == "INST126":
        print(course[2])


# Rather than trying to remember which position we happened to have decided to use to store a particular attribute (if we used lists), we can use **semantically meaningful indices for values**, i.e., keys!

# In[7]:


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


# It's a lot easier to remember keys (if we name them useful things) compared to just indices. And Python can help us remember too!

# If you're interested, there are also formal technical reasons to prefer dictionaries over lists if you care about speed/efficiency and your computational task is **checking** if an item exists in a collection *and* you're dealing with very large scale data: https://www.jessicayung.com/python-lists-vs-dictionaries-the-space-time-tradeoff/. 

# Later we will learn the `pandas` library (and the `dataframe` data structure, which is sort of a hybrid of `lists` and `dictionaries`): you can do really fast lookup, but also sort stuff!

# ## Anatomy of a dictionary
# 
# 
# 
# 

# Dictionaries are not so different from... our dictionaries in real life. :) Basically *map* a bunch of **keys** (e.g., a word) to corresponding **values** (e.g., a definition). Another example is indices in the back of print(!!!) books that map key terms to pages where that term shows up, or tags on websites, that map tags to webpages that include those tags.
# 
# The key parts of a dictionary `literal` are:
# 1. The `{ }` curly braces, which tell you and Python that it's a dictionary (similar to `""` for strings, or `[]` for lists)
# 2. At least one **entry** (but usually several), that maps a **value** on the right of a  `:` --- which functions like the `=` expression --- to a **key** on the left. For example, our first entry maps the value "apple" to the key "a".
# 3. Similar to lists, we include `,` to separate multiple entries in the dictionary.
# 
# Let's look at a simple example that maps letters to an example word that starts with the letter

# In[8]:


d = {
   'a': 'apple', # an entry that maps the value apple to the letter a
   'b': 'ball', # another entry that maps the value ball to the letter b
   'c': 'crayon' 
}
d


# Style note: the indentation inside the dictionary is more for readability. Python doesn't care, as long as there are commas between the dictionary entries. 
# 
# You can also write it out like this, but i find it harder to read:
# 

# In[9]:


d = {'a': 'apple', 'b': 'ball', 'c': 'crayon'} 
d


# Here are some other examples.

# In[10]:


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


# ### Properties of a dictionary

# Here are some key properties of a dictionary in Python:
# 
# #### Dictionaries have length
# 
# Similar to lists, dictionaries have **length**. 

# In[11]:


d = {
   'a': 'apple', # an entry that maps the value apple to the letter a
   'b': 'ball', # another entry that maps the value ball to the letter b
   'c': 'crayon' 
}
len(d)


# #### Dictionaries do not have an order or indexing by position
# 
# Different from lists, dictionaries **do not have an order**. So you can't really sort a list, or grab things by position. You grab things by... key!

# In[12]:


# can't get things by position
d[0]


# In[18]:


# can't sort either
d.sort()


# In[34]:


sorted(d) # this does *not* sort the dictionary; it returns a sorted list of the keys


# Though as we will see next week, you can sneakily get some order, bc now Python allows you to actually iterate through a dictionary in the order that stuff was put into it. It's not reliable though! If you need your collection to have an actual sequence to it, don't use dictionaries!

# #### All keys in a dictionary are unique
# 
# Also, all keys in a dictionary have to be **unique**. This makes dictionaries handy for keeping track of unique items (in contrast to say, lists, where you can have duplicate entries). 
# 
# Values in the dictionary do *not* have to be unique, though: you can have different keys point to the same value, but not multiple values point to duplicate keys. There is a related data structure that has a similar property called `sets` if you're interested.

# In[35]:


d = {
   'a': 'apple', # an entry that maps the value apple to the letter a
   'b': 'ball', # another entry that maps the value ball to the letter b
   'c': 'crayon',
   'a': 'animal',
   'd': 'ball'
}
print(d) # oops, where did apple go? overwritten by the last a:animal entry since we can't have duplicate keys. d:ball is fine though, even though we already have b:ball.


# #### Dictionaries are mutable
# 
# Like lists, dictionaries are also **mutable**: you can modify them directly (in contrast to strings, where you never modify them directly, but only ever create a new modified version of the string).

# In[21]:


print(f"d before modification: {d}")
print("modifying d, by adding an entry mapping the key f to the value friend")
d.update({"f": "friend"})
print(f"d after modification: {d}")


# ### What kinds of data can we put in a dictionary?

# #### Anything goes for values
# 
# Basically anything goes for **values**. You can even nest a dictionary inside another dictionary, by mapping a dictionary value to some key.

# In[4]:


def hello():
    print("hello world!")

d = {
   'a': ['apple', "animal"], # an entry that maps the value apple to the letter a
   'b': 'ball', # another entry that maps the value ball to the letter b
   'c': 2,
   'd': [1, 3, "denizen"],
   'e': hello # even a function is fine!
}
d


# In[15]:


students = {
    'joel': {
        'major': 'info sci',
        'year': 'senior',
        'interests': ['programming', 'football', 'dancing']
    },
}
students


# #### Keys must be hashable
# 
# But **keys** need to be *hashable*. 
# 
# What does this mean?
# 
# From the [Python glossary](https://docs.python.org/2/glossary.html):
# 
# > An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method), and can be compared to other objects (it needs an __eq__() or __cmp__() method). Hashable objects which compare equal must have the same hash value. Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.
# 
# > All of Python’s immutable built-in objects are hashable, while no mutable containers (such as lists or dictionaries) are. Objects which are instances of user-defined classes are hashable by default; they all compare unequal, and their hash value is their id().
# 
# More info here: https://stackoverflow.com/questions/14535730/what-does-hashable-mean-in-python

# In[30]:


d = {['3']: 'apple'}


# I mention this because a common error when first working with dictionaries is to try to use an unhashable data structure as a key. 
# 
# Understanding hashes is not something to worry about *for now*. We can focus on a basic rule of thumb for now: strings and numbers are ok as keys; everything else (that you'll learn now) is not.

# ## Working with dictionaries: basics
# 

# ### Create a dictionary

# In[ ]:


d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon', 
}


# You can also start with an empty dictionary, and then add stuff later, programmatically or with other functions.

# In[38]:


emptyd = {} # dictionary with nothing in it
emptyd = dict() # same thing
print(emptyd)
len(emptyd)


# **PRACTICE**: make a dictionary e that has the following entries: smith:A, chan:B, abuye:A+

# In[5]:


# your code here


# ### Get the value associated with a key from a dictionary

# In[42]:


d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon' 
}
d['c'] # put a key inside square brackets associated with a dictionary


# This is called the "old style" or "indexing" pattern. Looks a little bit like lists.

# In[43]:


d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon' 
}
d.get('c') # use the get function to get the value for the key that we give it


# This is the newer pattern that I prefer for clarity.

# It also has the advantage of not breaking your program if you try to access a key that doesn't exist.

# In[46]:


d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon' 
}
d['d'] # will crash the program with key error


# `.get()` lets you specify a default value that should come back if the key doesn't exist. This is very useful for writing clean and understandable dictionary patterns, such as indexing, which we'll dig into next week.

# In[47]:


d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon' 
}
result = d.get('d', "Key not found") # will return None as a default
print(result)


# **PRACTICE**: how do you get the value associated with the key `a`?

# In[6]:


# your code here


# ### Adding entries to a dictionary (or updating entries)

# Classic style, using indexing and assignment

# In[37]:


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


# Newer style, using `.update()`

# In[39]:


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


# **PRACTICE**: how do you update d with new entry `h:hello`?

# In[7]:


# your code here


# **PRACTICE**: how do you update d so that `a` maps to the value `asteroid`?

# In[8]:


# your code here


# `.update()` has the advantage of being able to add multiple key-value pairs at once.

# In[10]:


d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon' 
}
print(d)
d.update({'a': 'ashes', 'b':'bread', 'c':'charming', 'e': 'egg'})
print(d)


# **PRACTICE**: how do you update d with new entries `f:friend` and `g:grapes` in a single operation?

# In[9]:


# your code here


# **PRACTICE**: how do you update d so that `f` now points to `funny` and `b` points to `bundle`, in a single operation?

# In[11]:


# your code here


# You can use the pattern that is comfortable for you, but I prefer `.get()` and `.update()` for now because it's more readable and robust.

# ### List keys and values

# `.keys()` gives you all the keys in the dictionary
# 
# `.values()` gives you allt he values in the dictionary
# 
# `.items()` gives you all the entries in the dictionary
# 
# each of these is iterable

# In[41]:


d


# In[58]:


# list all the keys in the dictionary
d.keys()


# In[59]:


# list all the values in the dictionary
d.values()


# In[60]:


# list all the key-value pairs in the dictionary
d.items()


# In[61]:


# this means you can iterate through the keys/values
for key in d.keys():
    print(key, d.get(key))


# In[62]:


# iterate through the items
for key, value in d.items():
    print(f'{key} is associated with the value {value}')


# ### Check if a key is in a dictionary

# In[65]:


d = {
   'a': 'apple',
   'b': 'ball',
   'c': 'crayon' 
}
print('h' in d)


# Can only use 'in' operator with keys

# You can also do this with `.get()`!

# In[64]:


# retrieve value for a, if it's not found, say "not found"
d.get("h", False)


# **PRACTICE**: how do you check if the key "c" is in the dictionary `d`?

# In[12]:


# your code here


# ### Reverse look up keys from values: YOU CAN'T! Not really...

# Dictionaries are very powerful transformations of your data that make it REALLY easy to do a specific kind of operation, but lock you out of doing other things. So design the structure of the dictionary carefully. For example, if you make an index, and find that you actually care a lot about grabbing the top N words, you probably want to map counts (as keys) to words (as values), not words to counts.

# In[67]:


s = "she sells sea shells by the sea shore in the sea and the shells and the sea sea sea"

d = {} # define a dictionary to hold hte index
# go through word by word
for word in s.split():
  # get the current count for the word, default to 0 if we haven't seen it
  current_count = d.get(word, 0)
  # update the count
  new_count = current_count + 1
  # update the dictionary with the word and count
  d.update({word: new_count})

d


# Could try to invert it, but....

# In[ ]:


def reverse_dictionary(d):
    return {v: k for k, v in d.items()}


# You actually lose information, because remember: keys are unique! No duplicates! So we lose one of our "2" entries.

# In[ ]:


d_invert = reverse_dictionary(d)
d_invert


# In[ ]:


d_invert = {}
for word, count in d.items():
    words = d_invert.get(count, []) # get the current list of words associated with this count
    words.append(word)
    d_invert.update({count: words})
d_invert


# ## Dictionary Application: Indexing

# Now that we have the dictionary data structure, we can apply it in a program that can *create* an index.
# 
# ### Example
# 
# Here's an example from above that takes a list of book chapter strings and a list of key concepts, and spits out an index that maps key concepts to chapters.

# In[ ]:


# how to know which chapters talk about strings? or debugging?
book = [
  "Chapter 1: talks about strings and how they have the property of immutability also some basic debugging",
  "Chapter 2: continues talking about advanced methods for strings and also introduces the concept of functions",
  "Chapter 3: discusses iteration and lists and also debugging",
]


# In[72]:


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


# What dictionary concepts do you recognize?

# ### The indexing pattern
# 
# Here's the generic structure of an indexing pattern

# In[ ]:


# create an empty dictionary to hold the index

# for every item in a list of things you want to index

    # (optional: parse out the keys and values you want to index from the item)
    
    # get the current value associated with the key in the index
    
    # update the value
    
    # update the index with the key and its updated value


# Let's look at a super simple example: making a **word count index**. 
# 
# We'll take in a list of words, and produce an index that maps words as `keys` to counts of occurrences as `values`.

# In[87]:


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


# ### Practice: index grade counts
# 
# Practice! Test your understanding by adapting the above code to count how many times each grade was earned in a course.

# In[93]:


grades_counts = {}


# In[13]:


# your code here


# ### Practice: which words are n characters long?
# 
# Now let's extend this a bit. We'll modify the first program to index word lengths: we want an index that can tell us "what words in the list were 2 characters long, or 5 characters long?"

# In[15]:


# the thing we want to index
word_list = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore', 'in', 'the', 'sea', 'and', 'the', 'shells', 'and', 'the', 'sea', 'sea', 'sea']

# your code here


# ### Practice: counts of email addresses from email records
# 
# Let's index how many times we got emails from which email addresses!

# In[16]:


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


# ### Practice: map email addresses to email records
# 
# Now modify the previous program to map email **records** (as values) to email addresses (as keys). We want to ask questions like "can i see the emails I got from `cwen@iupui.edu`?

# In[17]:


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


# In[108]:


email_occurrences.get("david.horwitz@uct.ac.za")


# ### Investigate: integrate the book chapter indexing program into our generic structure
# 
# What's the same? What needs to be modified?

# In[ ]:





# ### Practice: flag important emails
# 
# Let's say you have a list of 'starred contacts', and you want a separate index where you can ask the question "give me all the emails i got from this starred contact". You can imagine this being sort of a rudimentary back-end of your "important" tab in Gmail. 
# 
# How might we modify our email indexing program to do this?

# In[18]:


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

