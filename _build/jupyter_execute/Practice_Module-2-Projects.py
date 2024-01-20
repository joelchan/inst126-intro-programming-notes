#!/usr/bin/env python
# coding: utf-8

# # Practice: Module 2 Project (Lists, Iteration, Strings)
# 
# ## Reformat and count names
# 
# Process the list to convert to lastname, firstname format. Count the number of names that have lastname "Wright". Be careful! There are some inconsistencies in upper/lowercase!
# 
# e.g., the first three elements of the output list should look like
# 
# `["Thompson, Amelia", "Martinez, Oscar", "Green, Sophie"]`
# 
# And you should print out a message that is formatted like this:
# `"There are M names with lastname Wright"`
# 
# Here is the correct output:
# 
# `['Thompson, Amelia', 'Martinez, Oscar', 'Wright, Sophie', 'Harrison, Miles', 'Wright, Isabella', 'Patel, Lucas', 'Murphy, Chloe', 'Rodriguez, Leo', 'Lee, Ella', 'Kim, David', 'Chen, Emily', 'Davis, Oliver', 'Robinson, Lily', 'Adams, Caleb', 'wright, Ava', 'Garcia, Nathan', 'Hernandez, Grace', 'Brown, Ethan', 'Taylor, Avery', 'WrighT, Jacob']`
# 
# `There are 4 names with lastname Wright`

# In[1]:


# make sure you run this cell before you attempt your program
names = [
    'Amelia Thompson',
    'Oscar Martinez',
    'Sophie Wright',
    'Miles Harrison',
    'Isabella Wright',
    'Lucas Patel',
    'Chloe Murphy',
    'Leo Rodriguez',
    'Ella Lee',
    'David Kim',
    'Emily Chen',
    'Oliver Davis',
    'Lily Robinson',
    'Caleb Adams',
    'Ava wright',
    'Nathan Garcia',
    'Grace Hernandez',
    'Ethan Brown',
    'Avery Taylor',
    'Jacob WrighT'
]


# In[2]:


names_lf = [] # for output list (reformatted names)
num_wright = 0 # count of names with lastname wright

# for every name in the input list
for name in names:
    # parse name into first and last name
    elements = name.split(" ")
    # firstname is the first thing
    firstname = elements[0]
    # lastname is the second thing
    lastname = elements[1]
    
    # MAP
    # make the lastname, firstname format
    name_lf = lastname + ", " + firstname
    # add it to our new list
    names_lf.append(name_lf)
    
    # COUNT
    # normalize the lastname by turning into lowercase
    lastname_lower = lastname.lower()
    # check if it's wright
    if lastname_lower == "wright":
        # update our count
        num_wright += 1

# print out results
print(names_lf)        
print(f"There are {num_wright} names with lastname Wright")


# Here is a variant that is slightly more compact and (in my opinion) readable and debuggable.
# 
# For the parsing step, instead of saving the output of `name.split(" ")` into an intermediate list (since we don't care about it), we unpack it directly into two variables `firstname`, and `lastname`, since we know (assume!) the split will produce two elements. The first element in the split goes into the first variable, and the second into the second variable. This gives us one less variable to keep track of.
# 
# Second, instead of joining the lastname and firstname with `+`, we use the f-string string formatting.
# 
# Finally, for the step of checking the lastname, we can also skip assigning it to a variable, and just directly compare the output of `lastname.lower()` to the string `"Wright"`.

# In[3]:


names_lf = [] # for output list (reformatted names)
num_wright = 0 # count of names with lastname wright

# for every name in the input list
for name in names:
    
    # parse name into first and last name
    firstname, lastname = name.split(" ")
    
    # MAP
    # make the lastname, firstname format
    name_lf = f"{lastname}, {firstname}"
    # and add to output list
    names_lf.append(name_lf)
    
    # COUNT
    # check if the lastname (normalized) is wright
    if lastname.lower() == "wright":
        # update count if so
        num_wright += 1

# print out results
print(names_lf)
print(f"There are {num_wright} names with lastname Wright")


# ## Clean dataset
# 
# Clean this dataset. The values should all be between 0 and 100. Anything above 100 is an outlier. Anything coded -999 is a missing value. Compute the average value of the cleaned dataset (i.e., w/ outliers and missing removed), and report how many outliers and missing values there are. Your output message shoudl only show 3 decimal points.
# 
# Here is the correct output:
# 
# `[67, 96, 95, 78, 36, 94, 67, 85, 96, 60, 73, 45, 6, 17, 24, 82, 82, 100, 44, 81, 12, 60]`
# 
# `After removing 4 missing values and 4 outliers, average value is 63.636`

# In[4]:


# make sure you run this cell before you attempt your program
data = ['67', '96', '95', '78', '36', '94', '67', '85', '96', '60', '73', '45', '6', '17', '24', '82', '125', '150', '136', '106', '82', '100', '44', '81', '12', '-999', '-999', '-999', '-999', '60']


# In[5]:


# your program here

clean = [] # output list (cleaned dataset)
num_missing = 0 # count of missing
num_outliers = 0 # count of outliers

for item in data:
    
    # convert to number
    num = int(item)
    
    # check if missing or outlier
    # if missing (this will catch -999)
    if num < 0:
        # update count of missing
        num_missing += 1
    # otherwise, if outlier
    elif num > 100:
        # update count of outlier
        num_outliers += 1
    # otherwise
    else:
        # add to our cleaned dataset
        clean.append(num)

# compute the average
avg = sum(clean)/len(clean)

# print out results
print(clean)
print(f"After removing {num_missing} missing values and {num_outliers} outliers, average value is {avg:.3f}")


# ## Process submissions (with late penalties and exceptions)
# 
# Here is a list of submissions that I want you to process.
# 
# The submissions have three parts to them (separated by commas):
# 1. The score (0 to 100)
# 2. A value that indicates whether the submission was late (0 or 1)
# 3. A value that indicates whether the submission had a late exception
# 
# Produce a final list of scores that applies a late penalty (reduce score by 20%) unless the submission has a late exception. 
# 
# Also, report:
# 1. The average score of the final list (M)
# 2. The number of non-exempted late submissions (N)
# 
# In the following format:
# `"The average score (after penalizing N late submissions) is M"`
# 
# Make sure M is formatted with only 2 decimal points.
# 
# Here is the correct output:
# 
# `[62, 80, 5, 12.0, 64.0, 97, 61, 20, 56, 74, 73, 89, 57, 27.200000000000003, 63, 2, 27, 60, 33, 65.60000000000001]`
# 
# `The average score (after penalizing 4 late submissions) is 51.39`

# In[6]:


# make sure you run this cell before you attempt your program
submissions = ['62,0,0', '80,0,0', '5,0,0', '15,1,0', '80,1,0', '97,0,0', '61,0,0', '20,1,1', '56,0,0', '74,0,0', '73,0,0', '89,0,0', '57,0,0', '34,1,0', '63,0,0', '2,0,0', '27,0,0', '60,0,0', '33,1,1', '82,1,0']


# In[7]:


# your program here

