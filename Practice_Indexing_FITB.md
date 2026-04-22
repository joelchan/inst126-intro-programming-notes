---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Practice: Dictionary Indexing (Fill-in-the-Blank & Ordering)

## Part 1: What's the right default value?

### Q1: Counting words

We want to count how many times each word appears. What should go in the blank?

```python
words = ["the", "cat", "sat", "on", "the", "mat"]
counts = {}
for word in words:
    counts[word] = counts.get(word, ____) + 1
```

- A) `[]`
- B) `""`
- C) `0`
- D) `None`

````{admonition} Answer:
:class: toggle

**C) `0`**

We're counting (adding 1 each time), so the default must be a number we can add to. Starting at `0` means the first time we see a word, we get `0 + 1 = 1`. If we used `[]`, Python would try to do `[] + 1`, which is an error. If we used `""`, we'd get `"" + 1`, also an error.
````

### Q2: Grouping items

We want to group student names by their grade. What should go in the blank?

```python
records = [("Joel", "B"), ("Sarah", "A"), ("Rony", "A"), ("Kacie", "B")]
grade_groups = {}
for name, grade in records:
    grade_groups[grade] = grade_groups.get(grade, ____)
    grade_groups[grade].append(name)
```

- A) `0`
- B) `[]`
- C) `""`
- D) `name`

````{admonition} Answer:
:class: toggle

**B) `[]`**

We're *accumulating* items into a list (notice the `.append()` on the next line). So the default needs to be an empty list `[]`. The first time we see a grade, `.get()` returns `[]`, and then we append the first name to it. If we used `0`, Python would try `0.append(name)`, which would crash.
````

### Q3: Summing values

We want to compute total sales per product. What should go in the blank?

```python
sales = [("coffee", 4.50), ("tea", 3.00), ("coffee", 5.25), ("tea", 2.75)]
totals = {}
for product, amount in sales:
    totals[product] = totals.get(product, ____) + amount
```

- A) `[]`
- B) `amount`
- C) `0`
- D) `1`

````{admonition} Answer:
:class: toggle

**C) `0`**

We're summing dollar amounts (adding `amount` each time), so the default must be a number. Starting at `0` means the first sale of coffee gives `0 + 4.50 = 4.50`. Option D (`1`) would give wrong totals (coffee would be `1 + 4.50 + 5.25 = 10.75` instead of `9.75`). Option B (`amount`) doesn't make sense as a default — it would double-count the first sale.
````

### Q4: Collecting unique items

We want to map each department to a list of course codes. What should go in the blank?

```python
courses = ["INST126", "CMSC131", "INST201", "CMSC132", "INST326"]
dept_courses = {}
for course in courses:
    dept = course[:4]
    dept_courses[dept] = dept_courses.get(dept, ____)
    dept_courses[dept].append(course)
```

- A) `0`
- B) `course`
- C) `{}`
- D) `[]`

````{admonition} Answer:
:class: toggle

**D) `[]`**

We're building up a list of courses per department (notice `.append(course)` on the next line), so we need an empty list as the starting value. Option C (`{}`) is an empty *dictionary*, which doesn't have an `.append()` method.
````

## Part 2: What goes in the blank? (operation logic)

### Q5: The update step

We're counting email domains. What should go in the blank?

```python
emails = ["joel@umd.edu", "sarah@gmail.com", "rony@umd.edu"]
domain_counts = {}
for email in emails:
    domain = email.split("@")[1]
    count = domain_counts.get(domain, 0)
    ____
    domain_counts[domain] = count
```

- A) `count = count + domain`
- B) `count += 1`
- C) `count = 0`
- D) `domain_counts[domain] = domain_counts[domain] + 1`

````{admonition} Answer:
:class: toggle

**B) `count += 1`**

We retrieved the current count, now we need to increment it by 1 before storing it back. Option A tries to add a string to a number. Option C resets the count to 0 every time (would always end up as 1). Option D would crash on the first lookup because the key doesn't exist yet (that's why we used `.get()` in the first place!).
````

### Q6: The get step

We're grouping words by length. What should go in the blank?

```python
words = ["cat", "hi", "dog", "go", "bird"]
by_length = {}
for word in words:
    length = len(word)
    ____ = by_length.get(length, [])
    current.append(word)
    by_length[length] = current
```

- A) `by_length[length]`
- B) `word`
- C) `current`
- D) `length`

````{admonition} Answer:
:class: toggle

**C) `current`**

The `.get()` call retrieves the current list for this length (or `[]` if we haven't seen this length before). We need to store that in a variable so we can `.append()` to it on the next line, then save it back. The variable name `current` matches the usage on the next two lines.
````

## Part 3: Put the lines in order (Parson's problems)

### Q7: Count letter frequencies

Arrange these lines to count how many times each letter appears in a string. One line is a **distractor** (it doesn't belong).

```
A) letter_counts[letter] = count
B) count += 1
C) for letter in text:
D) count = letter_counts.get(letter, 0)
E) letter_counts = {}
F) count = letter_counts[letter]
```

````{admonition} Answer:
:class: toggle

**Correct order: E, C, D, B, A**

```python
letter_counts = {}                          # E: create empty dict
for letter in text:                         # C: loop through each letter
    count = letter_counts.get(letter, 0)    # D: get current count (default 0)
    count += 1                              # B: increment
    letter_counts[letter] = count           # A: store updated count
```

**Distractor: F** — `letter_counts[letter]` without `.get()` would crash with a `KeyError` the first time we see a new letter.

Key ordering logic: you must **get** the current value *before* you update it, and you must **store it back** *after* you update it. E must come first (create the dict), and C must come before D (you need `letter` from the loop to look it up).
````

### Q8: Group students by section

Arrange these lines to build a dictionary mapping sections to lists of student names. One line is a **distractor**.

```
A) section_roster[section].append(name)
B) section_roster = {}
C) students = section_roster.get(section, [])
D) section_roster[section] = students
E) for name, section in enrollment:
F) students.append(name)
```

````{admonition} Answer:
:class: toggle

**Correct order: B, E, C, F, D**

```python
section_roster = {}                              # B: create empty dict
for name, section in enrollment:                 # E: loop through records
    students = section_roster.get(section, [])    # C: get current list (default [])
    students.append(name)                         # F: add name to list
    section_roster[section] = students            # D: store updated list
```

**Distractor: A** — `section_roster[section].append(name)` tries to access the key directly. This *would* actually work on the second+ occurrence of a section, but would crash with a `KeyError` the first time. That's why we need the `.get()` pattern (line C) to handle the "first time" case safely.

Key ordering logic: C must come before F (you need the list before you can append to it), and D must come after F (store the list *after* appending).
````

### Q9: Sum scores per team

Arrange these lines to compute total scores per team. One line is a **distractor**.

```
A) team_totals[team] = total
B) total = team_totals.get(team, 0)
C) for team, score in games:
D) total = total + score
E) team_totals = {}
F) total = team_totals.get(team, [])
```

````{admonition} Answer:
:class: toggle

**Correct order: E, C, B, D, A**

```python
team_totals = {}                          # E: create empty dict
for team, score in games:                 # C: loop through games
    total = team_totals.get(team, 0)      # B: get current total (default 0)
    total = total + score                 # D: add this game's score
    team_totals[team] = total             # A: store updated total
```

**Distractor: F** — uses `[]` as the default, but we're *summing* numbers, not collecting into a list. `[] + score` would crash. The default must match the operation: `0` for addition, `[]` for appending.
````

### Q10: Index file extensions

Arrange these lines to build a dictionary mapping file extensions to lists of filenames. **No distractors** — all lines belong.

```
A) ext = fname.split(".")[-1]
B) file_index[ext] = files
C) files = file_index.get(ext, [])
D) file_index = {}
E) files.append(fname)
F) for fname in filenames:
```

````{admonition} Answer:
:class: toggle

**Correct order: D, F, A, C, E, B**

```python
file_index = {}                           # D: create empty dict
for fname in filenames:                   # F: loop through filenames
    ext = fname.split(".")[-1]           # A: parse out the extension
    files = file_index.get(ext, [])       # C: get current list (default [])
    files.append(fname)                   # E: add filename to list
    file_index[ext] = files               # B: store updated list
```

Key ordering logic:
1. D first (create dict before the loop)
2. F next (start the loop)
3. A before C (you need `ext` to look it up)
4. C before E (you need the list before you can append)
5. E before B (append before storing back)

Notice the pattern: **parse → get → update → store**. This is always the order inside the loop body.
````
