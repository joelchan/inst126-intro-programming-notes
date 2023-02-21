# Problem Formulation

## Learning outcomes
- Construct a computational problem formulation for an English problem statement
- Analyze problem formulations in terms of their values

## What is problem formulation and why should we care about it?

Remember the overarching division between "solving problems" (computational thinking) and "coding" (giving instructions to the computer in Python) that we talked about [before](https://joelchan.github.io/inst126-intro-programming-notes/what-is-programming.html)?


A BIG part of computational thinking is **problem formulation**. 

To do real-world programming, you need to know more than how to write code. You need to be able to take a relatively vague problem like "get all the email addresses out of this file", and **model the problem so that it can be solved by a computer**.

### An example

Let's walk through an example together of what this looks like.

Here's a vague problem statement: I get so many emails, and i have a blocklist of usernames that i don't want to see. so, please filter all the emails that come in everyday, so i don't see the emails from the blocked usernames

```{note}
As a user, I want to get all email addresses out of a file
```

And here is a draft problem formulation:

```{image} assets/probform-ex-email-filter.png
:class: bg-primary mb-1
:width: 1000px
:align: center
```

Notice how this formulation specifies in much more detail the (sub)operations, data, and logical relationships between the operations/data.

### More on why problem formulation matters

If you don't learn this skill (and it is a skill!) in this class, you *will* struggle in future programming courses (e.g., INST326) and any other area where you're actually needing to *use* programming to solve information science problems.

To give a flavor of this, consider this note I got from an INST326 instructor on what students were really struggling with in her class:

> "They are struggling with programming in general. Even though this is their second course, they **don’t have much ability to think about how to solve problems**. We’re in the “I watched everything you did and followed but have absolutely no idea where to start” phase, even with very simple work. **I suspect they are sneaking through 126 without learning what they need and suddenly have to create from scratch with me and are panicked**"

To emphasize: If you can't formulate a problem in computational terms, it doesn't matter whether you know how to write a legal conditional statement, or how to assign variables, and so on. You’ll know *how* to instruct the computer, but not what instructions to give it! The *what* comes from problem formulation. It’s absolutely critical!

### When/how to do problem formulation?

You should be able to think through these bits without knowing how to write the code for it! 

In fact, it's a **really good idea** to get started on this *before* you write any code. Your problem formulation doesn't have to be perfect or complete, and you will refine it as you go, but it will guide what you write, and help you think through your debugging and help-seeking as well (recall how it's useful to have a navigator and driver in paired programming: the problem formulation representation can help be a passive navigator resource)

This is why we have your first deliverable for Project 2 be a problem formulation.

## Anatomy of a problem formulation

Let's go back to our running example. What are the parts of the problem formulation?

I find it useful to think about a problem formulation as specifying three sets of things:
1. The key steps/**operations** of your program
2. The **data** that is going in and out of the steps/operations
3. The **logical flow** of how all the pieces fit together

Here is our example again:

```{image} assets/probform-ex-email-filter.png
:class: bg-primary mb-1
:width: 1000px
:align: center
```

In this example, the key elements were:
- Operations: *extract* email address from email record, *extract* username from email, *add* email to filtered emails list if the username isn't in the blocked username list
- Data: *raw email list*, *filtered emails*, etc.
- Logic: *loop* over every raw email, *conditional* for the adding operation, sequence between the operations.

In this class we will use a simple diagramming convention of red post-its for operations, blue post-its for data, and orange/yellow for logical relationships. This is a very simplified convention to get at these key ideas around problem formulation. In professional practice, there are a number of different diagram types and practices (often [involving a whiteboard](https://twitter.com/Sydonahi/status/1239804661642620930)), such as [UML diagrams](https://www.tutorialspoint.com/uml/uml_standard_diagrams.htm) and [other conventions/diagrams](https://www.quora.com/Programmers-what-kind-of-diagram-helps-you-most-when-solving-problems).

## Let's practice!
Let's look at another simple example: I'm going to give you a list of numbers, and I want you to give me back a list that only has odd numbers in it:
1. What are the main substeps/**operations** in this problem?
2. What **data** is going in/out of the operations?
3. What is the **logical flow** of how they fit together?

Let's look at slightly more complex example that we *definitely* don't know how to code yet. I'm going to give you a bunch of birth certificates (N=500,000), and I want you to tell me what the top 50 and top 10 baby names are, because I want to choose names that are recognizable (i.e., in the top 50), but not too common (top 10):
1. What are the main substeps/**operations** in this problem?
2. What **data** is going in/out of the operations?
3. What is the **logical flow** of how they fit together?

## Homework for next time

Chatbot-based search is all the rage now (e.g., Bing, Bard). For next class, try to start with that vague problem statement and map out:
1. What are the main substeps/**operations** in this problem?
2. What **data** is going in/out of the operations?
3. What is the **logical flow** of how they fit together?

We'll discuss this together in class and pick up the question: *what makes for a good problem formulation?*