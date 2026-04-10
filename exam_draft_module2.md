# Mock Exam: Module 2 (Iteration, Lists, Strings)

~15 minutes, 4 questions. Intended for ELMS online quiz.

---

## Question 1: Code Tracing

**You're writing a script to clean URLs for privacy. What is the output of the following code?**

```python
urls = [
    "https://shop.com/item?utm_source=twitter",
    "http://news.org/article?ref=homepage",
    "https://blog.io/post?utm_campaign=sale",
    "https://docs.dev/page"
]
cleaned = []
tracker_count = 0

for url in urls:
    url = url.replace("http://", "https://")
    if "?" in url:
        base, param = url.split("?")
        if param.startswith("utm"):
            cleaned.append(base)
            tracker_count += 1
        else:
            cleaned.append(url)
    else:
        cleaned.append(url)

print(len(cleaned))
print(tracker_count)
print(cleaned[1])
```

- A) `4` then `2` then `https://news.org/article?ref=homepage`
  - Note: Correct! Put in rationale from below.
- B) `2` then `2` then `https://blog.io/post`
  - Note: we're appending all urls to cleaned (this is a transform pattern), so len(cleaned) is 4 (same as input). blog.io/post is the 3rd item in cleaned (cleaned[2])
- C) `4` then `2` then `http://news.org/article?ref=homepage`
  - Note: Correct number of cleaned and tracked, and the correct url, but it should be https instead of http since we're doing `url.replace("http://", "https://")`
- D) `4` then `3` then `https://news.org/article`
  - Note: Correct number of cleaned, but not tracked (only two `utm_` params); so news.org url (correct position, cleaned[1]) should have the `?ref=homepage` param since it's not a tracker param
- E) `3` then `2` then `https://news.org/article?ref=homepage`
  - Note: Correct number of tracked, and correct url, but not `len(cleaned)`

**Correct answer: A**

Rationale: Walk through each URL:
1. `"https://shop.com/item?utm_source=twitter"` — has `?`, param starts with `utm` → append base `"https://shop.com/item"`, tracker_count = 1
2. `"http://news.org/article?ref=homepage"` — first replaced to `https://...`, has `?`, param is `ref=homepage` which does NOT start with `utm` → append the full url `"https://news.org/article?ref=homepage"`
3. `"https://blog.io/post?utm_campaign=sale"` — has `?`, param starts with `utm` → append base `"https://blog.io/post"`, tracker_count = 2
4. `"https://docs.dev/page"` — no `?` → append as-is

All 4 URLs end up in `cleaned` (len = 4). Two had trackers (tracker_count = 2). `cleaned[1]` is the news URL with `https://` and `?ref=homepage` preserved.

Key distractors:
- B tests whether students think non-tracker URLs are excluded
- C tests whether students miss the `http` → `https` replacement
- D tests whether students think `ref=homepage` starts with `utm`
- E tests whether students think URLs without `?` are excluded

---

## Question 2: Choosing the Right Loop

**For each of the following tasks, select whether a `for` loop or a `while` loop is the best (most suitable, idiomatic) choice.**

**(2a)** Process every item in a list of 100 student grades and count how many are above 90.

- A) `for` loop
- B) `while` loop
  - Note: We know the exact collection to iterate through (the list of grades) and we need to visit every item. This is the textbook use case for a `for` loop, now a `while`: you *could* solve with `while`, but it's unnecessarily clunkier.

**Correct answer: A**

Rationale: We know the exact collection to iterate through (the list of grades) and we need to visit every item. This is the textbook use case for a `for` loop.

---

**(2b)** Keep asking the user for a password until they enter the correct one.

- A) `for` loop
  - Note: We don't know in advance how many attempts it will take. We need to keep going until a condition is met (correct password entered). This requires a `while` loop.
- B) `while` loop

**Correct answer: B**

Rationale: We don't know in advance how many attempts it will take. We need to keep going until a condition is met (correct password entered). This requires a `while` loop.

---

**(2c)** Search through a list of names and stop as soon as you find "Joel".

- A) `for` loop (with `break`)
  - Note: You could use a `for` loop with `break` to stop early, OR a `while` loop with an index that advances until the name is found or you reach the end. *Both* are reasonable approaches. The `for` + `break` approach is slightly simpler since you don't need to manage the index yourself.
- B) `while` loop
  - Note: You could use a `for` loop with `break` to stop early, OR a `while` loop with an index that advances until the name is found or you reach the end. *Both* are reasonable approaches. The `for` + `break` approach is slightly simpler since you don't need to manage the index yourself.
- C) Either would work well

**Correct answer: C**

Rationale: You could use a `for` loop with `break` to stop early, or a `while` loop with an index that advances until the name is found or you reach the end. Both are reasonable approaches. The `for` + `break` approach is slightly simpler since you don't need to manage the index yourself.

---

## Question 3: Pattern Recognition

**Consider this code that filters a list based on a condition:**

```python
prices = [12.50, 3.99, 25.00, 8.75, 45.00, 2.50]
expensive = []
for price in prices:
    if price > 10:
        expensive.append(price)
```

**Which of the following programs uses the SAME computational pattern?**

- **A)**
```python
words = ["hello", "hi", "hey", "howdy"]
total = 0
for word in words:
    total += len(word)
```
Note: The original code uses the **filter pattern**: iterate through a list, check a condition, and collect only the items that pass into a new list. A is an **accumulator** pattern (summing values, no conditional collection), not a filter.

- **B)**
```python
temps = [72, 85, 68, 91, 77, 95, 60]
hot_days = []
for temp in temps:
    if temp > 90:
        hot_days.append(temp)
```
Note: Correct! B is a filter (collect temps > 90) — same pattern, different data and condition.

- **C)**
```python
names = ["Joel", "Sarah", "John"]
upper_names = []
for name in names:
    upper_names.append(name.upper())
```
Note: The original code uses the **filter pattern**: iterate through a list, check a condition, and collect only the items that pass into a new list. D is a **transform/map** pattern (doubling every item with no filtering), not a filter.

- **D)**
```python
nums = [1, 2, 3, 4, 5]
doubled = []
for num in nums:
    doubled.append(num * 2)
```
Note: The original code uses the **filter pattern**: iterate through a list, check a condition, and collect only the items that pass into a new list. C is a **transform/map** pattern (applying a transformation to every item with no filtering), not a filter.

**Correct answer: B**

Rationale: The original code uses the **filter pattern**: iterate through a list, check a condition, and collect only the items that pass into a new list.

- B is a filter (collect temps > 90) — same pattern, different data and condition.
- A is an **accumulator** pattern (summing values, no conditional collection).
- C is a **transform/map** pattern (applying a transformation to every item with no filtering).
- D is also a **transform/map** pattern (doubling every item with no filtering).

---

## Question 4: Find the Bug

**A student wrote the following program to clean up a list of course codes by converting them to uppercase. But it doesn't work — the output is still the original list with mixed casing. Which line has the bug, and why?**

```python
codes = ["inst126", "CMSC132", "Inst201", "math140"]
for i in range(len(codes)):
    codes[i].upper()          
print(codes)
```

- A) The `range(len(codes))` should just be `range(codes)` — you can't use `len()` with `range()`.
  - Note: `range(len(codes))` is perfectly valid syntax! The issue is that strings are immutable — `.upper()` returns a *new* string but does not modify the original. We need to reassign: `codes[i] = codes[i].upper()`.
- B) Line A calls `.upper()` but doesn't save the result. It should be `codes[i] = codes[i].upper()` because strings are immutable.
- C) The `for` loop should use `for code in codes:` instead of index-based iteration — that's why the `.upper()` doesn't work.
  - Note: index-based iteration is fine! The issue is that strings are immutable — `.upper()` returns a *new* string but does not modify the original. We need to reassign: `codes[i] = codes[i].upper()`. Plus, a `for code in codes` loop would have the same problem since `code = code.upper()` wouldn't modify the list either! 
- D) `.upper()` doesn't work on strings that are already partially uppercase like `"CMSC132"`.
  - Note: `.upper()` works on any string regardless of existing casing

**Correct answer: B**

Rationale: Strings are immutable — `.upper()` returns a *new* string but does not modify the original. The student needs to reassign: `codes[i] = codes[i].upper()`.

Key distractors:
- A is wrong because `range(len(codes))` is perfectly valid syntax
- C is wrong because index-based iteration is fine; the issue is immutability, not the loop style (and actually, a `for code in codes` loop would have the same problem since `code = code.upper()` wouldn't modify the list either!)
- D is wrong because `.upper()` works on any string regardless of existing casing

---

## Notes for instructor

**Concepts tested across questions:**

| Concept | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| for loops | x | x | x | x |
| while loops | | x | | |
| String methods (.replace, .startswith, .split) | x | | | x |
| `in` operator (substring check) | x | | | |
| List building (.append) | x | | x | |
| Conditionals inside loops | x | | x | |
| String immutability | | | | x |
| Filter pattern | | | x | |
| Transform pattern | | | x | |
| Accumulator pattern | x | | x | |
| for vs while reasoning | | x | | |

**Bloom's taxonomy levels:**
- Q1: Apply (trace execution)
- Q2: Analyze (choose appropriate construct for a scenario)
- Q3: Analyze (recognize structural similarity across different problems)
- Q4: Evaluate (diagnose a bug and identify the root cause)

**ELMS implementation notes:**
- Q1: Single-answer multiple choice
- Q2: Three separate sub-questions, each single-answer MC (could be grouped as one ELMS question with parts, or three quick standalone questions)
- Q3: Single-answer multiple choice
- Q4: Single-answer multiple choice
