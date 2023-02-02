#!/usr/bin/env python
# coding: utf-8

# # Sample program(s): course code filtering
# 
# ## Example program: copy only the 100-level courses over to my course list
# 
# Computational formulation:
# 
# Main data:
# - COURSE_CODE_LIST - list of only course codes
# - COURSE_CODE - the element we'll need to look at to decide whether to copy something over
# - MY_COURSES (list of course codes I care about)
# 
# Subparts:
# - PARSER to get course code number
# - FILTER to decide whether something should be grabbed
# - ADDER to add grabbed course to my course list
# 
# Logic/flow:
# - LOOP over the list of course codes
# - CONDITIONAL to grab course code or not based on filter

# In[1]:


# PARSER
def parse_code(course_code):
    r = 0
    # go through teh course code character by character
    for char in course_code:
        # if it's a number
        if char.isnumeric():
            # grab it!
            r = char
            # and be done with the loop, since we only want the first one
            break
    
    # reutrn the code
    return r


# In[2]:


# FILTER
def code_filter(course_code, target_code):
    code = parse_code(course_code)
    # check if the code is the one we want
    if code == target_code:
        return True
    else:
        return False


# In[3]:


# Putting it together

COURSE_CODE_LIST = ['INST126', 'INST201', 'INST311', 'INST314', 'INST326', 'INST327', 'INST335',
 'INST346', 'INST352', 'INST354', 'INST362', 'INST377', 'INST408Y', 'INST408Z',
 'INST414', 'INST447', 'INST462', 'INST466', 'INST490', 'INST604', 'INST612',
 'INST614', 'INST616', 'INST622', 'INST627', 'INST630', 'INST652', 'INST702',
 'INST709', 'INST728G', 'INST728V', 'INST733', 'INST737', 'INST741', 'INST742',
 'INST746', 'INST762', 'INST767', 'INST776', 'INST785', 'INST794']

# to hold the courses i care about
MY_COURSES = []

# the code i care about
MY_TARGET_CODE = "2"

# LOOP over list of courses
for course_code in COURSE_CODE_LIST:
    
    # CONDITIONAL to decide whether or not to copy over course
    if code_filter(course_code, MY_TARGET_CODE):
        # ADDER to add course to my list
        MY_COURSES.append(course_code)
        
print(MY_COURSES)


# ## Example program: copy only the 400-level courses and below over to my course list
# 
# Computational formulation is same as before, only diff is we need to **generalize** the filter

# In[4]:


# FILTER
def code_filter_lte(course_code, threshold):
    # get the first number in the code
    code = parse_code(course_code)
    
    # change to number data type so we can do "math"
    code = int(code)
    
    # check if it's less than or equal to our threshold level
    if code <= threshold:
        return True
    else:
        return False


# In[5]:


# TRANSFERRER v2

MY_UNDERGRAD_COURSES = []

MY_THRESHOLD = 4

for course_code in COURSE_CODE_LIST:
    if code_filter_lte(course_code, MY_THRESHOLD):
        MY_UNDERGRAD_COURSES.append(course_code)
        
print(MY_UNDERGRAD_COURSES)

