# Resource Pointers: Problem Formulation, Specifications, and Testing

These are curated resources to potentially link from Problem-Formulation.md. Organized by topic, with notes on relevance and audience level.

## Where to add in the chapter

I'd suggest a new section at the end of the chapter (before or after the values section), something like "## Further reading" or "## Going deeper: from problem formulation to professional practice". Could also sprinkle individual links inline where relevant (noted below).

---

## 1. Problem Formulation / Computational Thinking

### [Computational Thinking for Problem Solving (UPenn / Coursera)](https://www.coursera.org/learn/computational-thinking-problem-solving)
- Full course for non-CS students: decomposition, pattern recognition, abstraction, algorithms
- Free to audit
- **Level:** Beginner
- **Possible placement:** Inline link in the "What is problem formulation" section, or in a further reading section

### [Library Carpentry: Introducing Computational Thinking](https://librarycarpentry.github.io/lc-computational-thinking/aio.html)
- Designed for librarians and information professionals (directly relevant audience!)
- Teaches computational thinking through practical scenarios, includes pseudocode exercises
- CC-BY licensed, free
- **Level:** Beginner
- **Possible placement:** Great inline recommendation since it's aimed at info science folks

### [OpenStax: Computational Thinking (Intro to CS, Ch. 2.1)](https://openstax.org/books/introduction-computer-science/pages/2-1-computational-thinking)
- Free, peer-reviewed textbook chapter covering decomposition, pattern recognition, abstraction, algorithms
- **Level:** Beginner
- **Possible placement:** Further reading section

### [Polya's "How to Solve It" Applied to Code (Jeremy Howard)](https://gist.github.com/jph00/d60301884c56fe063101a7cc6193b3af)
- Summary of Polya's 4-step framework (Understand, Plan, Execute, Review) applied to programming
- Written by the founder of fast.ai — a leader in accessible data science education
- Short read
- **Level:** Beginner
- **Possible placement:** Could work inline in the "What makes for a good problem formulation?" section, since it's about process/heuristics. Or further reading.

---

## 2. Specification Writing / Design by Contract

### [Programming "By Contract" (USF Lecture Notes, Terence Parr)](https://www.cs.usfca.edu/~parrt/course/601/lectures/programming.by.contract.html)
- University lecture on preconditions, postconditions, invariants
- Includes real-world failure examples (Ariane rocket, Mars probe) showing why specs matter
- Uses Java/Eiffel examples, but the conceptual framing transfers
- **Level:** Intermediate
- **Possible placement:** Further reading, with a note that the code examples are in other languages but the ideas apply

### [Design by Contract: Introduction (Eiffel Software / Bertrand Meyer)](https://www.eiffel.com/values/design-by-contract/introduction/)
- The canonical introduction from the creator of Design by Contract
- Uses a "client-supplier contract" business metaphor that's intuitive for non-CS students
- **Level:** Beginner-Intermediate
- **Possible placement:** Further reading. The contract metaphor could also be referenced inline in the new "From problem formulation to specification" section.

---

## 3. Test-Driven Development (TDD)

### [A Simple Introduction to Test Driven Development with Python (freeCodeCamp)](https://www.freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe/)
- Written by a beginner for beginners
- Walks through red-green-refactor in Python with unittest
- Honest, relatable tone about why testing matters when you're still learning
- **Level:** Beginner
- **Possible placement:** Further reading, or inline in the "They become your tests" bullet

### [Test-Driven Development in Python: A Beginner's Guide (DataCamp)](https://www.datacamp.com/tutorial/test-driven-development-in-python)
- From a data science education platform — framing aligns with students who work with data
- Practical Python TDD tutorial
- **Level:** Beginner
- **Possible placement:** Further reading

### [Test Driven Development: The Philosophy (Cprogramming.com)](https://www.cprogramming.com/tutorial/test-driven-development.html)
- Concise, language-agnostic explanation of TDD philosophy
- Emphasizes that writing tests first forces you to understand requirements before coding
- **Level:** Beginner
- **Possible placement:** Further reading

---

## 4. Related Practices

### [The Beginner's Guide to BDD (Inviqa)](https://inviqa.com/blog/bdd-guide)
- Explains Behaviour-Driven Development: writing requirements in plain English "Given-When-Then" format
- Relevant for iSchool students who often bridge technical and non-technical teams
- Includes interview with Dan North (BDD's originator)
- **Level:** Beginner
- **Possible placement:** Further reading, with a note that the "Given-When-Then" format connects to the input/output examples practice

### [Khan Academy: Planning with Pseudo-Code](https://www.khanacademy.org/computing/computer-programming/programming/good-practices/pt/planning-with-pseudo-code)
- Short, free video on using pseudocode to plan before coding
- **Level:** Beginner
- **Possible placement:** Could link inline in the problem formulation section, or further reading

### [Rubber Duck Debugging (freeCodeCamp)](https://www.freecodecamp.org/news/rubber-duck-debugging/)
- Explains debugging by explaining your code out loud — forces you to articulate your logic
- A lightweight "thinking before/while coding" technique
- **Level:** Beginner
- **Possible placement:** Further reading or inline in a debugging context

---

## Suggested grouping for a "Further Reading" section

If adding a single section to the chapter, I'd group them like this:

**Planning before you code:**
- Library Carpentry: Computational Thinking (info science audience!)
- Polya's problem-solving framework applied to code
- Khan Academy: Planning with Pseudo-Code

**From specifications to tests:**
- freeCodeCamp: Intro to TDD with Python
- DataCamp: TDD in Python
- Inviqa: Beginner's Guide to BDD (writing requirements in plain English)

**Going deeper (more advanced):**
- USF Lecture: Programming by Contract (preconditions, postconditions, real-world failures)
- Eiffel Software: Design by Contract (the original "contract" metaphor)
- UPenn Coursera: Computational Thinking for Problem Solving (full course)
