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

# Practice: Dictionary Scenarios

For each scenario, start by creating the dictionary, then complete the retrieval and update operations.

---

## Scenario 1: Gradebook (basic)

You're building a simple gradebook that maps student names to their current grade (a single letter grade).

### Setup

Create a dictionary called `gradebook` with the following entries:

| Student | Grade |
|---|---|
| Joel | B |
| Sarah | A |
| Rony | A+ |
| Kacie | B+ |
| Miles | C |

```{code-cell} ipython3
# create the gradebook dictionary here
```

### Retrieve

**R1.** Print Joel's grade.

```{code-cell} ipython3
# your code here
```

**R2.** Check if "Pat" is in the gradebook. If so, print their grade; otherwise print `"Pat is not in the gradebook"`.

```{code-cell} ipython3
# your code here
```

**R3.** Use `.get()` to look up "Zara" in the gradebook. If she's not there, print `"Zara: no grade on file"`.

```{code-cell} ipython3
# your code here
```

### Update

**U1.** Miles turned in extra credit — update his grade to `"B-"`.

```{code-cell} ipython3
# your code here
```

**U2.** A new student, Pat, joined the class with a grade of `"B"`. Add them to the gradebook.

```{code-cell} ipython3
# your code here
```

**U3.** Sarah and Rony both got final grade adjustments: Sarah is now `"A-"` and Rony is now `"A"`. Update both in a single operation.

```{code-cell} ipython3
# your code here
```

---

## Scenario 2: Restaurant menu (basic)

You're modeling a simple restaurant menu that maps dish names to their price.

### Setup

Create a dictionary called `menu` with the following entries:

| Dish | Price |
|---|---|
| burger | 12.99 |
| salad | 9.50 |
| pasta | 14.75 |
| soup | 7.25 |
| fries | 5.00 |

```{code-cell} ipython3
# create the menu dictionary here
```

### Retrieve

**R1.** A customer asks how much the pasta costs. Print the price formatted as: `"pasta: $14.75"`.

```{code-cell} ipython3
# your code here
```

**R2.** A customer wants to know the price of fries. Print it formatted as `"fries: $5.00"`.

```{code-cell} ipython3
# your code here
```

**R3.** A customer asks for "milkshake". Use `.get()` with a default to print `"milkshake: not on the menu"` if it doesn't exist.

```{code-cell} ipython3
# your code here
```

### Update

**U1.** The soup price increased to `$8.50`. Update the menu.

```{code-cell} ipython3
# your code here
```

**U2.** Add a new item: `"tacos"` at `$11.25`.

```{code-cell} ipython3
# your code here
```

**U3.** The burger and pasta prices both went up by $1.00. Update both in a single `.update()` call.

```{code-cell} ipython3
# your code here
```

---

## Scenario 3: Social media profile (basic)

You're modeling a simple social media profile where each key is a profile field.

### Setup

Create a dictionary called `profile` with the following entries:

| Field | Value |
|---|---|
| username | terp_coder |
| display_name | Joel C. |
| followers | 142 |
| bio | INST126 instructor |
| verified | False |

```{code-cell} ipython3
# create the profile dictionary here
```

### Retrieve

**R1.** Print the display name and bio in the format: `"{display_name} — {bio}"`.

```{code-cell} ipython3
# your code here
```

**R2.** Check if the account is verified. Print `"Verified account"` or `"Not verified"` accordingly.

```{code-cell} ipython3
# your code here
```

**R3.** Print the follower count formatted as: `"terp_coder has 142 followers"` (use the values from the dictionary, don't hardcode them).

```{code-cell} ipython3
# your code here
```

### Update

**U1.** The user gained 8 new followers. Update the follower count (don't just hardcode 150 — add 8 to the current value).

```{code-cell} ipython3
# your code here
```

**U2.** The user changed their bio to `"Python enthusiast | UMD"`. Update it.

```{code-cell} ipython3
# your code here
```

**U3.** The account got verified, and they also want to add a new field `"website"` with the value `"https://joelchan.me"`. Do both updates at once.

```{code-cell} ipython3
# your code here
```

---

## Scenario 4: Course directory (nested)

You're building a course directory where each course code maps to a dictionary of course details.

### Setup

Create a dictionary called `courses` with the following structure:

```
courses = {
    "INST126": {"title": "Intro to Programming", "instructor": "Joel", "capacity": 40, "enrolled": 38},
    "INST201": {"title": "Intro to Info Science", "instructor": "Sarah", "capacity": 35, "enrolled": 35},
    "INST326": {"title": "OO Programming", "instructor": "Pat", "capacity": 30, "enrolled": 22}
}
```

```{code-cell} ipython3
# create the courses dictionary here
```

### Retrieve

**R1.** Print the instructor for INST126.

```{code-cell} ipython3
# your code here
```

**R2.** Print how many open seats INST126 has (capacity minus enrolled), formatted as: `"INST126: {n} seats available"`.

```{code-cell} ipython3
# your code here
```

**R3.** A student wants to know the title and instructor for INST326. Print: `"INST326: OO Programming (taught by Pat)"`.

```{code-cell} ipython3
# your code here
```

### Update

**U1.** 3 more students enrolled in INST326. Update the enrolled count.

```{code-cell} ipython3
# your code here
```

**U2.** INST201 got a new instructor: "Rony". Update it.

```{code-cell} ipython3
# your code here
```

**U3.** Add a new course: `"INST314"` with title `"Statistics"`, instructor `"Kacie"`, capacity `25`, and enrolled `0`.

```{code-cell} ipython3
# your code here
```

---

## Scenario 5: Streaming catalog (nested)

You're modeling a simple streaming catalog where each show title maps to a dictionary of details.

### Setup

Create a dictionary called `catalog` with the following structure:

```
catalog = {
    "Stranger Things": {"genre": "sci-fi", "seasons": 4, "rating": 8.7},
    "The Office": {"genre": "comedy", "seasons": 9, "rating": 8.9},
    "Breaking Bad": {"genre": "drama", "seasons": 5, "rating": 9.5},
    "Ted Lasso": {"genre": "comedy", "seasons": 3, "rating": 8.8}
}
```

```{code-cell} ipython3
# create the catalog dictionary here
```

### Retrieve

**R1.** Print the rating of Breaking Bad.

```{code-cell} ipython3
# your code here
```

**R2.** Print how many seasons The Office has, formatted as: `"The Office: 9 seasons"`.

```{code-cell} ipython3
# your code here
```

**R3.** Check if "Wednesday" is in the catalog. Print `"Wednesday is available"` or `"Wednesday is not in the catalog"`.

```{code-cell} ipython3
# your code here
```

### Update

**U1.** Stranger Things released a new season. Update its season count to 5.

```{code-cell} ipython3
# your code here
```

**U2.** After the new season, the rating for Stranger Things was updated to `8.9`. Update it.

```{code-cell} ipython3
# your code here
```

**U3.** Add a new show: `"Wednesday"` with genre `"comedy"`, seasons `1`, and rating `8.1`.

```{code-cell} ipython3
# your code here
```

---

## Scenario 6: Website config (nested)

You're working with a website configuration dictionary that stores settings for different sections of the site.

### Setup

Create a dictionary called `config` with the following structure:

```
config = {
    "homepage": {"title": "Welcome", "show_banner": True, "max_posts": 10},
    "blog": {"title": "Our Blog", "show_banner": False, "max_posts": 25},
    "about": {"title": "About Us", "show_banner": True, "max_posts": 0}
}
```

```{code-cell} ipython3
# create the config dictionary here
```

### Retrieve

**R1.** Print the title of the blog page.

```{code-cell} ipython3
# your code here
```

**R2.** Check whether the blog page has the banner enabled. Print `"Blog banner: on"` or `"Blog banner: off"` accordingly.

```{code-cell} ipython3
# your code here
```

**R3.** Print the homepage title and max posts, formatted as: `"Homepage: 'Welcome' (max 10 posts)"`.

```{code-cell} ipython3
# your code here
```

### Update

**U1.** Enable the banner on the blog page.

```{code-cell} ipython3
# your code here
```

**U2.** The homepage should now show a max of 15 posts instead of 10. Update it.

```{code-cell} ipython3
# your code here
```

**U3.** Add a new page: `"contact"` with title `"Contact Us"`, `show_banner` set to `False`, and `max_posts` set to `0`.

```{code-cell} ipython3
# your code here
```
