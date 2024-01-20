#!/usr/bin/env python
# coding: utf-8

# ## Buggy program 1
# 
# symptoms: keys are letters instead of team names? and dollar signs are still there?

# In[1]:


team_donations = {}
#read the donations as a list of lines
donations = open("data/donations.txt").readlines()
#for every donation line in donations
for donation in donations:
    #split the donation into columns
    columns = donation.split("|")
    #clean the donation amounts by removing the $ so that python can recognize it as numbers
    #store as var
    columns[2].replace("$", "")
    #for every team in the team column
    for team in columns[1]:
        # # get the current value associated with the key in the index
        team_count = team_donations.get(team, [])
        # update the value
        team_count.append(columns[2])
        # update the index with the key and its updated value
        team_donations.update({team: team_count})
team_donations


# In[ ]:





# In[2]:


def clean_email_list(email_list, allowed_domains):
    cleaned_list = []
    non_approved_count = 1
    for email in email_list:
        domain = email.split('@')[1]
        if domain != "gmail.com" or "umd.edu":
            non_approved_count += 1
        else:
            cleaned_list.append(email)
                
    output_msg = "Screened out " + str(non_approved_count) + " email addresses from non-approved domains"
    return cleaned_list, output_msg


# ## Buggy program 2
# 
# Symptom: Attribute Error??

# In[3]:


def get_details(d, key): # fill out / check the parameters
    value = d.get(d)
    
    # write the body of the function
    return value# write the return value

classes_to_instructors = {"INST126": "Chan", "INST201": "Sauter"}
get_details(classes_to_instructors, "INST126")


# ## Buggy program 3
# 
# Symptom: Attribute Error??

# In[8]:


def string_list_to_dict(input_list, separator):
    dictionary = {}
    
    for item in input_list:
        key,value = item.split(separator)
        dictionary.update({key:value})
    return dictionary

input_l = [
     "stephen curry,warriors",
     "lebron james,lakers",
     "kevin durant,nets",
     "giannis antetokounmpo,bucks"
 ]
sep = ","
d = string_list_to_dict(input_list=input_l, separator=sep)
d


# ## Buggy program 4
# 
# symptom: truncated... short words instead of long words??

# In[6]:


words = ['We', 'hold', 'these', 'truths', 'to', 'be', 'self-evident,', 'that', 'all', 'men', 'are', 'created', 'equal,', 'that', 'they', 'are', 'endowed', 'by', 'their', 'Creator', 'with', 'certain', 'unalienable', 'Rights,', 'that', 'among', 'these', 'are', 'Life,', 'Liberty', 'and', 'the', 'pursuit', 'of', 'Happiness.--That', 'to', 'secure', 'these', 'rights,', 'Governments', 'are', 'instituted', 'among', 'Men,', 'deriving', 'their', 'just', 'powers', 'from', 'the', 'consent', 'of', 'the', 'governed,', '--That', 'whenever', 'any', 'Form', 'of', 'Government', 'becomes', 'destructive', 'of', 'these', 'ends,', 'it', 'is', 'the', 'Right', 'of', 'the', 'People', 'to', 'alter', 'or', 'to', 'abolish', 'it,', 'and', 'to', 'institute', 'new', 'Government,', 'laying', 'its', 'foundation', 'on', 'such', 'principles', 'and', 'organizing', 'its', 'powers', 'in', 'such', 'form,', 'as', 'to', 'them', 'shall', 'seem', 'most', 'likely', 'to', 'effect', 'their', 'Safety', 'and', 'Happiness.', 'Prudence,', 'indeed,', 'will', 'dictate', 'that', 'Governments', 'long', 'established', 'should', 'not', 'be', 'changed', 'for', 'light', 'and', 'transient', 'causes;', 'and', 'accordingly', 'all', 'experience', 'hath', 'shewn,', 'that', 'mankind', 'are', 'more', 'disposed', 'to', 'suffer,', 'while', 'evils', 'are', 'sufferable,', 'than', 'to', 'right', 'themselves', 'by', 'abolishing', 'the', 'forms', 'to', 'which', 'they', 'are', 'accustomed.', 'But', 'when', 'a', 'long', 'train', 'of', 'abuses', 'and', 'usurpations,', 'pursuing', 'invariably', 'the', 'same', 'Object', 'evinces', 'a', 'design', 'to', 'reduce', 'them', 'under', 'absolute', 'Despotism,', 'it', 'is', 'their', 'right,', 'it', 'is', 'their', 'duty,', 'to', 'throw', 'off', 'such', 'Government,', 'and', 'to', 'provide', 'new', 'Guards', 'for', 'their', 'future', 'security.--Such', 'has', 'been', 'the', 'patient', 'sufferance', 'of', 'these', 'Colonies;', 'and', 'such', 'is', 'now', 'the', 'necessity', 'which', 'constrains', 'them', 'to', 'alter', 'their', 'former', 'Systems', 'of', 'Government.', 'The', 'history', 'of', 'the', 'present', 'King', 'of', 'Great', 'Britain', 'is', 'a', 'history', 'of', 'repeated', 'injuries', 'and', 'usurpations,', 'all', 'having', 'in', 'direct', 'object', 'the', 'establishment', 'of', 'an', 'absolute', 'Tyranny', 'over', 'these', 'States.']

clean_list = []
cleaned_count = 0

limit = int(input("Character limit:"))
# for each word
for word in words:
    # check if the word is over the character limit
    if len(word) > limit: 
        print(f"Over character limit: {word}")
        new_word = word[0:limit]
        new_word = new_word + "..."
        clean_list.append(new_word)
        cleaned_count =+ 1 
    else:
        print(f"Ok with limit: {word}")
        clean_list.append(word)
print(clean_list)
print(f"Truncated {cleaned_count} words that were over the character limit")


# ## Buggy program 5
# 
# symptom: permission error??

# In[10]:


def read_file(filename):
    # open the file with read permissions
    fhand = open(filename, "r")
    # then read the contents and return it
    return fhand.read()

filename = "myfile.txt"
read_file(filename)


# In[ ]:




