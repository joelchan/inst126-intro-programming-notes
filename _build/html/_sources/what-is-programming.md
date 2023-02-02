# 1: What is programming? What is computational thinking?

## What is programming?

Programming is the art of making computers do what we want with programs. 
 
A computer program is **a repeatable set of instructions that a computer can use to solve a class of problems**

Computers lack both the same common sense and world model that we have, and English. This means we can't instruct them to do things as simply as instructing another person: we have to really "dumb it down" and use very specialized and precise language, like a programming language.

Critical mental model: programming skill is composed broadly of two things:
1. COMPUTATIONAL THINKING: how to model problems so they can be solved by computers
2. CODING: how to translate these models into valid instructions that a computer can follow

CODING tends to get all the attention. This is the syntax, the unfamiliarity of code language, should you learn Python or Javascript or C++ or Rust... And this is important!

But COMPUTATIONAL THINKING is the foundation, without which you cannot be a programmer. Professional programmers use computational thinking as a foundation and move from programming language to language, as the job requires.

## What is computational thinking?

Let's have a look at what the International Society for Technology in Education (ISTE) and the Computer Science Teachers Association (CSTA) [have to say about this](https://cdn.iste.org/www-root/Computational_Thinking_Operational_Definition_ISTE.pdf)

> Computational thinking (CT) is a problem-solving process that includes (but is not limited to) the following characteristics:
> • Formulating problems in a way that enables us to use a computer and other tools to help solve them.
> • Logically organizing and analyzing data
> • Representing data through abstractions such as models and simulations
> • Automating solutions through algorithmic thinking (a series of ordered steps)
> • Identifying, analyzing, and implementing possible solutions with the goal of achieving the most efficient and effective combination of steps and resources
> • Generalizing and transferring this problem solving process to a wide variety of problems

> These skills are supported and enhanced by a number of dispositions or attitudes that are essential dimensions of CT. These dispositions or attitudes include:
> • Confidence in dealing with complexity
> • Persistence in working with difficult problems
> • Tolerance for ambiguity
> • The ability to deal with open ended problems
> • The ability to communicate and work with others to achieve a common goal or solution

To get more intuition for the distinction from coding, consider that there are two broad classes of "bugs" (ways that programs can be broken/incorrect) that will come up as you program:
1. *Syntax errors*, which are when the computer can't even execute the code because it is not "legal"/valid code in some way. These bugs require CODING fixes: writing the code with correct, well-formed syntax for whatever programming language you are coding in. You can think of this as mapping to things like typos/misspellings and grammatical errors in writing.
2. *Semantic errors*, which are when the computer does (exactly!) what you say, but not what you want (e.g., unexpected behavior, incorrect outputs). These bugs require COMPUTATIONAL THINKING fixes: modeling the problem --- its data structures, subproblems, workflows, and algorithms --- better.