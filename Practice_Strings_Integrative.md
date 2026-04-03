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

# Practice: Integrative String Problems

## Problem 1: Clean and summarize sales data

You have a list of messy sales records. Each record is a string in the format `"item:price"`, but the prices have dollar signs and the item names have inconsistent casing and extra spaces.

**Your task:** For each record, print a cleaned line in the format: `"Item Name - $XX.XX"`

```{code-cell} ipython3
records = ["  COFFEE :$4.50", "Bagel: $3.75 ", "  juice:$5.00", " MUFFIN :$2.25"]
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
records = ["  COFFEE :$4.50", "Bagel: $3.75 ", "  juice:$5.00", " MUFFIN :$2.25"]
for record in records:
    item, price_str = record.split(":")
    item = item.strip().title()
    price = float(price_str.strip().replace("$", ""))
    print(f"{item} - ${price:.2f}")
```

Output:
```
Coffee - $4.50
Bagel - $3.75
Juice - $5.00
Muffin - $2.25
```

Key ideas: `.split(":")` to separate item from price, `.strip().title()` to normalize the item name, `.strip().replace("$", "")` to clean the price so we can convert to `float`, f-string with `:.2f` to format the output.
`````

## Problem 2: Parse emails and report by domain

You have a list of email addresses with messy formatting. Normalize them to lowercase, parse out the domain (the part after `@`), and print a line for each: `"{email} -> {domain}"`.

```{code-cell} ipython3
emails = ["  JoelChan@UMD.EDU", "sarah@Gmail.Com ", " RONY@terpmail.UMD.edu", "Pat@YAHOO.COM "]
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
emails = ["  JoelChan@UMD.EDU", "sarah@Gmail.Com ", " RONY@terpmail.UMD.edu", "Pat@YAHOO.COM "]
for email in emails:
    clean = email.strip().lower()
    domain = clean.split("@")[1]
    print(f"{clean} -> {domain}")
```

Output:
```
joelchan@umd.edu -> umd.edu
sarah@gmail.com -> gmail.com
rony@terpmail.umd.edu -> terpmail.umd.edu
pat@yahoo.com -> yahoo.com
```

Key ideas: `.strip().lower()` to normalize, `.split("@")[1]` to grab the domain, f-string for output.
`````

## Problem 3: Build a grade report from a messy string

You receive a single string of comma-separated student records. Each record has the format `"name:score"` and records are separated by commas. Scores are out of 50.

**Your task:** Parse each record, compute the percentage, and print: `"{name} - {score}/50 ({pct:.0f}%)"`. At the end, print the class average as `"Class average: {avg:.1f}%"`.

```{code-cell} ipython3
data = "Joel:42, Rony:48, Sravya:35, Kacie:44, Pat:50"
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
data = "Joel:42, Rony:48, Sravya:35, Kacie:44, Pat:50"
total_pct = 0
count = 0
for record in data.split(","):
    record = record.strip()
    name, score_str = record.split(":")
    score = int(score_str)
    pct = score / 50 * 100
    print(f"{name} - {score}/50 ({pct:.0f}%)")
    total_pct += pct
    count += 1
avg = total_pct / count
print(f"Class average: {avg:.1f}%")
```

Output:
```
Joel - 42/50 (84%)
Rony - 48/50 (96%)
Sravya - 35/50 (70%)
Kacie - 44/50 (88%)
Pat - 50/50 (100%)
Class average: 87.6%
```

Key ideas: `.split(",")` to get records, `.strip()` because of spaces after commas, `.split(":")` to separate name from score, `int()` to convert, f-string with `:.0f` and `:.1f` for formatting.
`````

## Problem 4: Normalize and deduplicate tags

You have a list of hashtags that are messy: some have `#`, some don't, casing varies, and there are duplicates. Clean them up and build a list of unique tags (lowercase, no `#`). Then print a summary: `"Found {n} unique tags: {tag1}, {tag2}, ..."`.

```{code-cell} ipython3
tags = ["#Python", " python", "#DATA", "data", " #Python ", "coding", "#Coding", "  DATA "]
unique_tags = []
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
tags = ["#Python", " python", "#DATA", "data", " #Python ", "coding", "#Coding", "  DATA "]
unique_tags = []
for tag in tags:
    cleaned = tag.strip().lower().replace("#", "")
    if cleaned not in unique_tags:
        unique_tags.append(cleaned)

# build the summary string
tag_list = ""
for i in range(len(unique_tags)):
    tag_list += unique_tags[i]
    if i < len(unique_tags) - 1:
        tag_list += ", "

print(f"Found {len(unique_tags)} unique tags: {tag_list}")
```

Output:
```
Found 3 unique tags: python, data, coding
```

Key ideas: `.strip().lower().replace("#", "")` to normalize, `not in` to deduplicate, f-string with `len()` for the count. Building the comma-separated string is a nice string-building exercise (there are fancier ways to do this with `", ".join()` but the loop approach works with what we've learned).
`````

## Problem 5: Parse and reformat dates

You have a list of dates in `"MM/DD/YYYY"` format. Reformat each one to `"YYYY-MM-DD"` format (the international standard) and collect into a new list. Print each original and reformatted date: `"{original} -> {reformatted}"`.

```{code-cell} ipython3
dates = ["03/15/2025", "12/01/2024", "07/04/2026", "01/31/2025"]
reformatted_dates = []
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
dates = ["03/15/2025", "12/01/2024", "07/04/2026", "01/31/2025"]
reformatted_dates = []
for date in dates:
    month, day, year = date.split("/")
    new_date = f"{year}-{month}-{day}"
    reformatted_dates.append(new_date)
    print(f"{date} -> {new_date}")
```

Output:
```
03/15/2025 -> 2025-03-15
12/01/2024 -> 2024-12-01
07/04/2026 -> 2026-07-04
01/31/2025 -> 2025-01-31
```

Key ideas: `.split("/")` with unpacking to get the three parts, f-string to reassemble in a different order. This is a very common real-world task!
`````

## Problem 6: Clean messy CSV and produce a formatted table

You receive a messy CSV string. The header row tells you the columns. There are extra spaces everywhere. Parse it, clean it, and print a neatly formatted table where each row looks like: `"{name:<10} {department:<6} ${salary:>10,.2f}"`.

*Hint:* inside f-string braces, `<10` means left-align in 10 characters, `>10` means right-align in 10 characters, and `,.2f` adds commas to a number with 2 decimal places.

```{code-cell} ipython3
csv_data = " Name , Dept , Salary \n Joel , INST , 85000 \n Sarah , CMSC , 92000 \n Rony , INST , 78000 \n Pat , INFO , 88500 "
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
csv_data = " Name , Dept , Salary \n Joel , INST , 85000 \n Sarah , CMSC , 92000 \n Rony , INST , 78000 \n Pat , INFO , 88500 "
rows = csv_data.split("\n")

# print header
print(f"{'Name':<10} {'Dept':<6} {'Salary':>12}")
print("-" * 30)

# skip header row (index 0), process data rows
for row in rows[1:]:
    parts = row.split(",")
    name = parts[0].strip()
    dept = parts[1].strip()
    salary = float(parts[2].strip())
    print(f"{name:<10} {dept:<6} ${salary:>10,.2f}")
```

Output:
```
Name       Dept   Salary
------------------------------
Joel       INST    $85,000.00
Sarah      CMSC    $92,000.00
Rony       INST    $78,000.00
Pat        INFO    $88,500.00
```

Key ideas: `.split("\n")` to get rows, `.split(",")` to get columns, `.strip()` on every piece, `float()` to convert salary, f-string alignment specifiers (`<`, `>`) and `,.2f` for comma-formatted currency. This problem brings together everything: parsing, cleaning, and formatting.
`````
