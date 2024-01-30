#!/usr/bin/env python
# coding: utf-8

# # Introduction to Jupyter

# **Acknowledgement**:
# This notebook was adapted from a [chapter](https://gureckislab.org/courses/spring21/labincp/chapters/02/00-jupyter.html) authored by [Todd M. Gureckis](http://gureckislab.org/~gureckis) is released under the CC BY-SA 4.0 license. Several of the sections on how to use the Jupyter Interface were developed and shared by [Jessica Hamrick](http://www.jesshamrick.com) as part of a course developed at UC Berkeley.
# 
# For extra orientation, I recommend checking out that chapter, as well as the [accompanying video lecture](https://vimeo.com/501114991) by Todd. It's quite excellent!

# ## A bit more about Jupyter notebooks

# The "notebook" interface is an approach to a programming and data analysis which combines programming/analysis code with text, images, figure, animations, and other multimedia in the same document.   The idea for computational notebooks has been around for a long time (e.g., [Mathematica](https://www.wolfram.com/mathematica/) is a commercial product that has long provided a notebook interface for data analysis and programming).  However, Jupyter is now one of the leading tools that data scientists use to analyze their data and write code.
# 
# 
# There are several reasons for the popularity of Jupyter:
# 
# 1. Jupyter is open source and free.  This means it is not owned by any one person or company.  Scientists and other programmers devote their time to improving Jupyter.  The code is readable by anyone which means it is easier to catch bugs.
# 2. Jupyter works with several different programming languages including R, Python, Matlab and others which are popular for data analysis.
# 3. Jupyter runs in a standard webbrowser.  This means you can use Jupyter often on any computing device you like including low-cost laptops like Chromebooks/Netbooks or even a tablet like an iPad.
# 4. Jupyter has many extensions which provide interactive widgets, animations, beautiful graphics, etc...
# 5. Jupyter is fun!  Once you get the hang of the notebook concept then it makes develping and debugging code a pretty fun experience.
# 6. Many companies use Jupyter internally and are looking to hire people with this skill.

# ## The "notebook" and "kernel" concepts

# The key to Jupyter is the concept of a **computational notebook**.  A computational notebook is a document-based approach to structuring data analysis and programming.  A notebook appears and acts similar to other programs you are familiar with like Excel or Google Sheets (spreadsheets) or Word or Google Docs (word processor).  These programs provide ways for you to enter information into documents and to save those file, send them to others, copy-paste, text, alter the formatting, etc...
# 
# We will primarily use the "classic" Jupyter Notebook interface which consists of a single document which you interact with not unlike a word processor.  There is a newer interface called [JupyterLab](https://blog.jupyter.org/jupyterlab-is-ready-for-users-5a6f039b8906) which looks more like Matlab or RStudio's interface allowing multiple windows and views of the running code.  The traditional notebook interface is prefered here primarily because it simple and faciliates reading along.
# 
# ### Cells
# 
# A computational notebook typically is made up of a set of elements called "cells" that group little bits of information together.  A notebook document (usually ending with the .ipynb extension on the file name) is a list of cells arranged from the top of the document to the bottom.  Cells can contain several types of information including code, text, images and so forth.  You develop your project by creating new cells, entering information, reordering cells, and saving the results.
# 
# ### The Kernel
# 
# The key element which makes a notebook "computational" is that it can be linked to a computing engine known as a "kernel" which can run on the same computer or another computer using the Internet.  The kernel is separate from the notebook and can for instance be stopped and started independently from the program displaying the notebook itself. The magic happens when a cell is "executed."  This sounds scary but refers simply to making the code in the cell "go".  When this happens the code from the cell that was executed is sent to the computational kernel and this kernel will run the sequence of commands contained within the cell.  Any results such as figures or printouts from the results of that code running will be sent to the notebook from the kernel and will be inserted beneath the cell which was just executed.  
# 
# A diagram of the basic conceptual idea is shown in the following figure that sketches out the flow between the notebook and the kernel.  Cells when they are executed are sent to the computational kernel which is an independent piece of software which can be started and stopped independently from the notebook.
# 
# 
# <img src="https://gureckislab.org/courses/spring21/labincp/_images/jupyterflow.png" width="400" height="200" />
# 

# ### Caution: The Notebook State and Kernel State are not the Same!

# One somewhat confusing aspect of Jupyter for beginners is that the notebook is simply a way to organize information and the order of information in a notebook has nothing to do with the order in which code has been executed on the server.
# 
# Instead, each time you execute a cell, the commands from that cell are sent to the kernel, run, and then returned.  Usually it make sense to organize your code so that multiple cells are arranged in order from the top of the document to the bottom.  You would then execute the first cell, then the second cell, and so forth. 
# 
# However, **and this is really important**, you don't have to execute the cells in order.  You can execute the third cell before the second or first cell if you want.  This just means that the code in the third cell would be sent to the kernel first and then the other cells would be sent.  This means that the order of the cells in the notebook document are really just for presentation, and it is up to you to "run/execute" the cells in whatever order you want.
# 
# This is mostly helpful because when you are doing and analysis you might want to go back up to the top and change something and then continue where you left off.  To do that you could scroll back to a earlier cell, change it, then execute it and then go back down to the beginning of the script.  
# 
# However, things can get confusing.  If you delete a cell it doesn't mean the code was "undone".  The kernel doesn't know anything about any edits you make to the notebook interface.  All it does is receive code when you send it via the "execute cell" command and then it waits.  This can mean that the "state" or current status of the kernel can at times be different from what your cells or notebook look like.  One easy option to deal with this is that if things get too far out of wack you can simply restart the kernel.  This will erase it's current state and set it back to a fresh start.  However, then you need to re-execute all of the cells in your notebook to get back to where you were.
# 
# The best analogy is like telling your friend how to cook a meal for you over the phone.  You have the instructions in front of you (your notebook) and you tell your friend (the kernel) what to do.  If you read the instructions out of order your friend can't tell the difference.  They just know each step you told them to do and follow it.  It is up to you to direct the instructions so they arrive to your friend (the kernel) in the right order.  And of course if things get confused you can just tell your friend to start over from stratch and begin again.
# 
# At first this can be confusing but eventually you get the hang of it.  It is one source of bugs/errors in Jupyter programming though and some people don't like using Jupyter for that reason.  In our case the upsides overweight this awkwardness.
# 
# <img src="https://gureckislab.org/courses/spring21/labincp/_images/jupyterwarning.png" width=400 height=200></img>

# ## Overview of the Jupyter Notebook

# In the following section we will go over the basics of the Jupyter interface.  While you can easily read this file on the web as a reminder it can be helpful to actually open this file in Jupyter so you can follow along and see the interface as it will actually appear.  Refer to the earlier section for several methods for opening this file in a Jupyter instance.
# 
# First, as described, notebooks are made up of a  series of *cells*. For example, the text you are reading is in what is called a "Markdown cell". The following cell is a "code cell":

# In[1]:


# this is a code cell


# You can tell what the type of a cell is by selecting the cell, and looking at the toolbar at the top of the page. For example, try clicking on this cell. You should see the cell type menu displaying "Markdown", like this:
# 
# <img src="https://gureckislab.org/courses/spring21/labincp/_images/cell-type-menu.png" width=400 height=200>

# ---

# ## Command mode and edit mode

# In the notebook, there are two modes: *edit mode* and *command mode*. By default the notebook begins in *command mode*. In order to edit a cell, you need to be in *edit mode*.

# **When you are in command mode**, you can press **enter** to switch to edit mode. The outline of the cell you currently have selected will turn green, and a cursor will appear.

# **When you are in edit mode**, you can press **escape** to switch to command mode. The outline of the cell you currently have selected will turn gray, and the cursor will disappear.

# ### Code cells
# 
# This is what a code cell looks like in command mode (Note: the following few cells are not actually cells -- they are images and just look like cells! This is for demonstration purposes only.):
# 
# <img src="https://gureckislab.org/courses/spring21/labincp/_images/command-mode-outline.png" width=400 height=200></img>
# 
# If we press enter, it will change to **edit mode**:
# 
# 
# <img src="https://gureckislab.org/courses/spring21/labincp/_images/edit-mode-outline.png" width=400 height=200></img>
# 
# And pressing escape will also go back to **command mode**:
# 
# <img src="https://gureckislab.org/courses/spring21/labincp/_images/command-mode-outline.png" width=400 height=200></img>
# 
# If we were to press **`Ctrl-Enter`**, this would actually *run* the code in the code cell:
# 
# <img src="https://gureckislab.org/courses/spring21/labincp/_images/code-cell-run.png" width=400 height=200></img>

# ---

# ## Executing cells

# Code cells can contain any valid Python code in them. When you run the cell, the code is executed and any output is displayed.

# **HINT**: 
# You can execute cells with **`Ctrl-Enter`** (which will keep the cell selected), or **`Shift-Enter`** (which will select the next cell).

# Try running the following cell and see what it prints out:

# In[2]:


print("Printing cumulative sum from 1-10:")
total = 0
for i in range(1, 11):
    total += i
    print("Sum of 1 to " + str(i) + " is: " + str(total))
print("Done printing numbers.")


# You'll notice that the output beneath the cell corresponds to the `print` statements in the code. Here is another example, which only prints out the final sum:

# In[3]:


total = 0
for i in range(1, 11):
    total += i
print(total)


# Another way to print something out is to have that thing be the last line in the cell. For example, we could rewrite our example above to be:

# In[4]:


total = 0
for i in range(1, 11):
    total += i
total


# However, this *will not work* unless the thing to be displayed is on the last line. For example, if we wanted to print the total sum and then a message after that, this will not do what we want (it will only print "Done computing total.", and not the total sum itself).

# In[5]:


total = 0
for i in range(1, 11):
    total += i
total
print("Done computing total.")


# If you are accustomed to Python 2, note that the parentheses are obligatory for the `print` function in Python 3.

# ---

# ## The IPython kernel

# When you first start a notebook, you are also starting what is called a *kernel*. This is a special program that runs in the background and executes code (by default, this is Python, but it could be other languages too, like R!). Whenever you run a code cell, you are telling the kernel to execute the code that is in the cell, and to print the output (if any).
# 
# Just like if you were typing code at the Python interpreter, you need to make sure your variables are declared before you can use them. What will happen when you run the following cell? Try it and see:

# In[6]:


a


# The issue is that the variable `a` does not exist. Modify the cell above so that `a` is declared first (for example, you could set the value of `a` to 1 -- or pick whatever value you want). Once you have modified the above cell, you should be able to run the following cell (if you haven't modified the above cell, you'll get the same error!):

# In[ ]:


print("The value of 'a' is: " + str(a))


# Running the above cell should work, because `a` has now been declared. To see what variables have been declared, you can use the `%whos` command:

# In[ ]:


get_ipython().run_line_magic('whos', '')


# If you ran the summing examples from the previous section, you'll notice that `total` and `i` are listed under the `%whos` command. That is because when we ran the code for those examples, they also modified the kernel state.

# (Note that commands beginning with a percent (%) or double percent (%%) are special IPython commands called *magics*. They will **only** work in IPython.)

# ### Restarting the kernel

# It is generally a good idea to periodically restart the kernel and start fresh, because you may be using some variables that you declared at some point, but at a later point deleted that declaration. 

# Your code should <b>always</b> be able to work if you run every cell in the notebook, in order, starting from a new kernel.

# To test that your code can do this, first restart the kernel by clicking the restart button:
# 
# <img src="https://gureckislab.org/courses/spring21/labincp/_images/restart-kernel-button.png" width=400 height=200></img>

# Then, run all cells in the notebook in order by choosing **Cell$\rightarrow$Run All** from the menu above.

# **HINTS**: 
# - There are many keyboard shortcuts for the notebook. To see a full list of these, go to <b>Help$\rightarrow$Keyboard Shortcuts</b>.
# - To learn a little more about what things are what in the IPython Notebook, check out the user interface tour, which you can access by going to <b>Help$\rightarrow$User Interface Tour</b>.

# ## Side note: the words in this notebook are also code! They're in a markup language called Markdown

# Markdown is a special way of writing text in order to specify formatting, like whether text should be bold, italicized, etc. If you're curious, you can read more here: [https://help.github.com/articles/markdown-basics](https://help.github.com/articles/markdown-basics)
# 
# - Hint #1: after editing the Markdown, you will need to run the cell so that the formatting appears.
# - Hint #2: try selecting *this* cell so you can see what the Markdown looks like when you're editing it. Remember to run the cell again to see what it looks like when it is formatted.
# 
# Markdown is a useful tool in Jupyter for making things look nice but you don't have to be a Markdown expert to succeed at this class.

# ## Additional Resources
# 
# This chapter gives you a basic introduction to the Jupyter Notebook system we will be using more or less daily in this class.  It is something you will get more familiar with through experience.  However, if you want additional resources here are some useful guides and videos introducing Jupyter:
# 
# - [What is Jupyter Notebook? (youtube)](https://www.youtube.com/watch?v=q_BzsPxwLOE)
# - [Jupyter Notebook: An Introduction (Mike Driscoll, RealPython.com)](https://realpython.com/jupyter-notebook-introduction/)
# - [Project Jupyter homepage](https://jupyter.org)
# - [List of other programming languages/kernels you can use with Jupyter](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)
# 
