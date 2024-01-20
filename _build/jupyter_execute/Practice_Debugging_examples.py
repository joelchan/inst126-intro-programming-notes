#!/usr/bin/env python
# coding: utf-8

# # Practice: Debugging
# 
# ## Semantic Errors
# 
# Semantic errors come about when your program does not work as it is supposed to. These usually do not lead to an actual error message, the program instead outputs something you did not expect or want, or does not output anything when you were expecting it to.

# ### Example 1
# 
# Intent: program that takes two numbers by user input, adds them together, and prints the sum
# 
# #### Reproducible example

# In[1]:


num1 = input('Enter a number:') 
num2 = input('Enter another number:') 
result = num1 + num2 
print('The sum of', num1, 'and', num2, 'is', result)


# #### Debugging notes

# In[ ]:


# debugging notes here!

# what did you expect?

# what did you see instead?

# what do you think is going on? what's the mismatch between your model and the computer's?
# checklist of strategies to draw from:
# [ ] model
# [ ] document/comment the code
# [ ] test with diff. inputs
# [ ] add print statements to help model what is happening / use python tutor


# #### Fixed version:

# In[ ]:





# #### Explanation of fix:

# In[ ]:





# ### Example 2
# 
# Intent: program that subtracts 2 from a given number until it reaches 0 
# 
# #### Reproducible example

# In[1]:


num = 30 
while num >= 0: 
    num = num - 2 
    print(f'num is now {num}') 


# #### Debugging notes

# In[2]:


# debugging notes here!

# what did you expect?

# what did you see instead?

# what do you think is going on? what's the mismatch between your model and the computer's?
# checklist of strategies to draw from:
# [ ] model
# [ ] document/comment the code
# [ ] test with diff. inputs
# [ ] add print statements to help model what is happening / use python tutor


# #### Fixed version:

# In[ ]:





# #### Explanation of fix:

# In[ ]:





# ### Example 3
# 
# Intent: program that prints all even numbers from 1 to 10
# 
# #### Reproducible example

# In[3]:


nums = [1,2,3,4,5,6,7,8,9,10]
for num in nums: 
    if num%2 != 0: 
        print(nums) 


# #### Debugging notes

# In[4]:


# debugging notes here!

# what did you expect?

# what did you see instead?

# what do you think is going on? what's the mismatch between your model and the computer's?
# checklist of strategies to draw from:
# [ ] model
# [ ] document/comment the code
# [ ] test with diff. inputs
# [ ] add print statements to help model what is happening / use python tutor


# #### Fixed version:

# In[ ]:





# #### Explanation of fix:

# In[ ]:





# ### Example 4
# 
# Intent: program that takes two numbers and prints out if the first number is greater than or less than the second number
# 
# #### Reproducible example

# In[5]:


a = 3
b = 3

if (a > b):
    print("a is greater than b")
else:
    print("a is less than b")


# #### Debugging notes

# In[6]:


# debugging notes here!

# what did you expect?

# what did you see instead?

# what do you think is going on? what's the mismatch between your model and the computer's?
# checklist of strategies to draw from:
# [ ] model
# [ ] document/comment the code
# [ ] test with diff. inputs
# [ ] add print statements to help model what is happening / use python tutor


# #### Fixed version:

# In[ ]:





# #### Explanation of fix:

# In[ ]:





# ### Example 5
# 
# Intent: program that adds course codes (strings) from one list to a new list if the courses are from INST (contain code INST)
# 
# #### Reproducible example

# In[7]:


items = ["INST201", "CMSC100", "STAT100", "INST126", "INST326"]
output = []
keyphrase = "INST"
for item in items:
    if "INST" in items:
        output.append(item)
print(output)


# #### Debugging notes

# In[8]:


# debugging notes here!

# what did you expect?

# what did you see instead?

# what do you think is going on? what's the mismatch between your model and the computer's?
# checklist of strategies to draw from:
# [ ] model
# [ ] document/comment the code
# [ ] test with diff. inputs
# [ ] add print statements to help model what is happening / use python tutor


# #### Fixed version:

# In[ ]:





# #### Explanation of fix:

# In[ ]:





# ## Syntax Errors
# 
# Syntax errors come from the user failing to follow the set rules given by python (e.g., syntax errors, indentation errors, index errors. These almost always lead to some type of error message
# 

# ### Example 1
# 
# Intent: Program that checks if a number is even or odd
# 
# #### Reproducible example

# In[9]:


x = input('Enter a number (or "exit" to quit): ') # get initial input from user

while x != "exit": # check if we should keep going (stop if user says "exit")
    if int(x)%2 = 0: # check if number is even
        print('You have entered an even number.')
    else:
        print('You have entered an odd number.')
    x = input('Enter a number (or "exit" to quit): ') # get new input from user


# #### Debugging notes

# In[10]:


# debugging notes here!

# what did you expect?

# what did you see instead?

# what do you think is going on? what's the mismatch between your model and the computer's?
# checklist of strategies to draw from:
# [ ] model
# [ ] document/comment the code
# [ ] test with diff. inputs
# [ ] add print statements to help model what is happening / use python tutor


# #### Fixed version:

# In[ ]:





# #### Explanation of fix:

# In[ ]:





# ### Example 2
# 
# Intent: program that checks if a list of numbers are even or odd 
# 
# #### Reproducible example

# In[11]:


numbers = [3, 14, 58, 9, 88, 104, 25]

for num in numbers:
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# #### Debugging notes

# In[12]:


# debugging notes here!

# what did you expect?

# what did you see instead?

# what do you think is going on? what's the mismatch between your model and the computer's?
# checklist of strategies to draw from:
# [ ] model
# [ ] document/comment the code
# [ ] test with diff. inputs
# [ ] add print statements to help model what is happening / use python tutor


# #### Fixed version:

# In[ ]:





# #### Explanation of fix:

# In[ ]:





# ### Example 3
# 
# Intent: program to see how "small" a number is (Under 5 is smallest, under 25 is smaller, under 50 is smallest, other is not small)
# 
# #### Reproducible example

# In[13]:


num = 4
if num < 5
    print (str(num) + " is smallest")
elif num < 25
    print(str(num) + " is smaller")
elif num < 50
    print (str(num) " is small")
else
    print (str(num) + " is not small")


# #### Debugging notes

# In[14]:


# debugging notes here!

# what did you expect?

# what did you see instead?

# what do you think is going on? what's the mismatch between your model and the computer's?
# checklist of strategies to draw from:
# [ ] model
# [ ] document/comment the code
# [ ] test with diff. inputs
# [ ] add print statements to help model what is happening / use python tutor


# #### Fixed version:

# In[ ]:





# #### Explanation of fix:

# In[ ]:





# ### Example 4
# 
# Intent: program that compares two numbers. Check if the first number is divisible by the second (no remainder)
# 
# #### Reproducible example

# In[15]:


first_num = 10
second_num = 2

if frist_num % second_num == 0:
    print(first_num , "is divisible by", second_num)


# #### Debugging notes

# In[16]:


# debugging notes here!

# what did you expect?

# what did you see instead?

# what do you think is going on? what's the mismatch between your model and the computer's?
# checklist of strategies to draw from:
# [ ] model
# [ ] document/comment the code
# [ ] test with diff. inputs
# [ ] add print statements to help model what is happening / use python tutor


# #### Fixed version:

# In[ ]:





# #### Explanation of fix:

# In[ ]:





# ### Example 5
# 
# Intent: program that prints all the items in a list
# 
# #### Reproducible example

# In[17]:


mylist = ["Garlic", "Lime", "Onion", "Banana", "Broccoli", "Pomegranate"]

for item in mylist:
    print(item


# #### Debugging notes

# In[18]:


# debugging notes here!

# what did you expect?

# what did you see instead?

# what do you think is going on? what's the mismatch between your model and the computer's?
# checklist of strategies to draw from:
# [ ] model
# [ ] document/comment the code
# [ ] test with diff. inputs
# [ ] add print statements to help model what is happening / use python tutor


# #### Fixed version:

# In[ ]:





# #### Explanation of fix:

# In[ ]:




