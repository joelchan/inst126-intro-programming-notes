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

# Practice: Module 2 Projects (Lists, Iteration, Strings)

## Problem 1: Reformat and count names

Process the list to convert each name from `"Firstname Lastname"` to `"Lastname, Firstname"` format. Keep the original casing as-is in the reformatted list (don't normalize it).

Then count the number of names that have lastname `"Wright"`. Be careful! There are some inconsistencies in upper/lowercase, so you'll need to do a **case-insensitive comparison** when counting.

Print the reformatted list, then print a message formatted like:
`"There are M names with lastname Wright"`

For example, the first three elements of the output list should be:
`["Thompson, Amelia", "Martinez, Oscar", "Wright, Sophie"]`

Here is the correct full output:

```
['Thompson, Amelia', 'Martinez, Oscar', 'Wright, Sophie', 'Harrison, Miles', 'Wright, Isabella', 'Patel, Lucas', 'Murphy, Chloe', 'Rodriguez, Leo', 'Lee, Ella', 'Kim, David', 'Chen, Emily', 'Davis, Oliver', 'Robinson, Lily', 'Adams, Caleb', 'wright, Ava', 'Garcia, Nathan', 'Hernandez, Grace', 'Brown, Ethan', 'Taylor, Avery', 'WrighT, Jacob']
There are 4 names with lastname Wright
```

```{code-cell} ipython3
names = [
    'Amelia Thompson',
    'Oscar Martinez',
    'Sophie Wright',
    'Miles Harrison',
    'Isabella Wright',
    'Lucas Patel',
    'Chloe Murphy',
    'Leo Rodriguez',
    'Ella Lee',
    'David Kim',
    'Emily Chen',
    'Oliver Davis',
    'Lily Robinson',
    'Caleb Adams',
    'Ava wright',
    'Nathan Garcia',
    'Grace Hernandez',
    'Ethan Brown',
    'Avery Taylor',
    'Jacob WrighT'
]

# your code here
```

## Problem 2: Clean a dataset

Clean this dataset. The values are stored as strings and need to be converted to integers. The valid range is 0 to 100 (inclusive). Apply these rules:
- Anything coded `-999` is a **missing value** — remove it
- Anything **above 100** is an **outlier** — remove it

Produce a cleaned list of integers, compute the average of the cleaned values, and report how many outliers and missing values you removed.

Your output message should show only 3 decimal places.

Here is the correct output:

```
[67, 96, 95, 78, 36, 94, 67, 85, 96, 60, 73, 45, 6, 17, 24, 82, 82, 100, 44, 81, 12, 60]
After removing 4 missing values and 4 outliers, average value is 63.636
```

```{code-cell} ipython3
data = ['67', '96', '95', '78', '36', '94', '67', '85', '96', '60',
        '73', '45', '6', '17', '24', '82', '125', '150', '136', '106',
        '82', '100', '44', '81', '12', '-999', '-999', '-999', '-999', '60']

# your code here
```

## Problem 3: Process submissions with late penalties

Here is a list of submissions to process. Each submission is a string with three comma-separated parts:
1. The **score** (0 to 100)
2. Whether the submission was **late** (`0` = on time, `1` = late)
3. Whether the submission has a **late exception** (`0` = no, `1` = yes)

Your task:
- Apply a **20% late penalty** (multiply score by 0.8) to submissions that are late **and** do not have an exception
- Leave all other scores unchanged
- Produce a final list of scores and count the number of penalized submissions

Print the final scores list, then print:
`"The average score (after penalizing N late submissions) is M"`

where M is formatted with 2 decimal places.

Here is the correct output:

```
[62, 80, 5, 12.0, 64.0, 97, 61, 20, 56, 74, 73, 89, 57, 27.2, 63, 2, 27, 60, 33, 65.6]
The average score (after penalizing 4 late submissions) is 51.39
```

*Note: Due to floating-point arithmetic, you might see values like `27.200000000000003` instead of `27.2`. That's normal! The important thing is the values are approximately correct.*

```{code-cell} ipython3
submissions = ['62,0,0', '80,0,0', '5,0,0', '15,1,0', '80,1,0', '97,0,0',
               '61,0,0', '20,1,1', '56,0,0', '74,0,0', '73,0,0', '89,0,0',
               '57,0,0', '34,1,0', '63,0,0', '2,0,0', '27,0,0', '60,0,0',
               '33,1,1', '82,1,0']

# your code here
```

## Problem 4: Analyze survey responses

You have survey responses where each response is a string in the format `"name|rating|comment"`. Ratings are 1-5. Some responses have messy whitespace and inconsistent casing in names.

Your task:
- Clean each name (strip whitespace, convert to title case)
- Collect only the responses with a rating of 4 or 5 into a "positive" list
- Print each positive response as: `"{name} (rating: {rating}): {comment}"`
- At the end, print: `"{N} out of {total} responses were positive ({pct:.1f}%)"`

Here is the correct output:

```
Joel (rating: 5): Great course
Sravya (rating: 4): Learned a lot
Kacie (rating: 5): Best class ever
Pat (rating: 4): Very helpful
4 out of 7 responses were positive (57.1%)
```

```{code-cell} ipython3
responses = [
    "  joel |5|Great course",
    " RONY|2|Too fast",
    "sravya |4|Learned a lot",
    "  Kacie|5|Best class ever",
    "Miles |3|It was okay",
    " pat |4|Very helpful",
    "ANNA|1|Not for me"
]

# your code here
```

## Problem 5: Generate email addresses from a roster

You have a roster string where each line has a student record in the format `"LastName,FirstName,GradYear"`. Generate a UMD email address for each student using the pattern: `firstname.lastname@umd.edu` (all lowercase, no spaces).

Collect the emails into a list, and also count how many students are graduating in 2026.

Print each generated email, then print:
`"Generated {N} emails. {M} students graduating in 2026."`

Here is the correct output:

```
amelia.thompson@umd.edu
oscar.martinez@umd.edu
sophie.wright@umd.edu
miles.harrison@umd.edu
isabella.wright@umd.edu
lucas.patel@umd.edu
Generated 6 emails. 3 students graduating in 2026.
```

```{code-cell} ipython3
roster = "Thompson,Amelia,2026\nMartinez,Oscar,2025\nWright,Sophie,2026\nHarrison,Miles,2027\nWright,Isabella,2025\nPatel,Lucas,2026"

# your code here
```

## Problem 6: Inventory price update

You have inventory data as a list of strings, each in the format `"item_name:quantity:price"`. Prices have dollar signs and the item names have inconsistent casing.

Your task:
- Apply a 15% price increase to any item with quantity below 10 (low stock markup)
- Clean item names to title case
- Print a report line for each item: `"{name} - Qty: {qty}, Price: ${new_price:.2f}"` (mark low-stock items with `" [LOW STOCK]"` at the end)
- At the end, print the total inventory value (sum of quantity * price for each item): `"Total inventory value: ${total:.2f}"`

Here is the correct output:

```
Laptop - Qty: 5, Price: $1149.85 [LOW STOCK]
Mouse - Qty: 50, Price: $24.99
Keyboard - Qty: 8, Price: $57.44 [LOW STOCK]
Monitor - Qty: 12, Price: $299.99
Headphones - Qty: 3, Price: $86.19 [LOW STOCK]
Total inventory value: $8355.14
```

```{code-cell} ipython3
inventory = [
    "LAPTOP:5:$999.00",
    "mouse:50:$24.99",
    "KEYBOARD:8:$49.95",
    "Monitor:12:$299.99",
    "headphones:3:$74.95"
]

# your code here
```

## Problem 7: Filetype screener

You're building a tool to filter files by extension — for example, keeping only code or notebook files.

Write a program that:

1. Takes as input:
    - A list of filepaths (strings).
    - A list of allowed filetypes (like `[".ipynb", ".py"]`).
2. Produces:
    - A list of only the **file names** (not full paths) that have an allowed extension. For example, `"analysis.ipynb"` from the path `"/Users/bob/projects/analysis.ipynb"`.
    - A message like: `"Kept N files. Screened out M files that were not an allowed filetype."`, where M is the number of files removed.

*Hint:* You can get the filename from a path by splitting on `"/"` and taking the last element. To check the extension, try `.endswith()`.

Here is the correct output:

```
['analysis.ipynb', 'code.py', 'final_report.ipynb', 'clean_data.ipynb']
Kept 4 files. Screened out 14 files that were not an allowed filetype.
```

Bonus variations:
- Modify your program to also grab the usernames (the part after `/Users/`) of files that had non-allowed filetypes, so you can notify them!
- Modify your program so its job is to screen *out* banned filetypes (e.g., `.exe` or `.sh` programs that can contain malware) instead of screening *in* allowed ones.

```{code-cell} ipython3
file_paths = [
    "/Users/alice/Documents/report.docx",
    "/Users/alice/Downloads/data.csv",
    "/Users/bob/projects/analysis.ipynb",
    "/Users/bob/Desktop/notes.txt",
    "/Users/charlie/Documents/presentation.pdf",
    "/Users/charlie/Music/track.mp3",
    "/Users/dana/Videos/tutorial.mov",
    "/Users/dana/Projects/code.py",
    "/Users/eve/Downloads/archive.zip",
    "/Users/eve/Documents/summary.pdf",
    "/Users/frank/Desktop/final_report.ipynb",
    "/Users/frank/Documents/todo.txt",
    "/Users/grace/Pictures/image.png",
    "/Users/heidi/Documents/research.pdf",
    "/Users/heidi/Downloads/script.sh",
    "/Users/ivan/Desktop/malware.exe",
    "/Users/ivan/Documents/clean_data.ipynb",
    "/Users/judy/Projects/old_version.bak"
]

# we only want code files like jupyter notebooks and .py scripts
allowed = [".ipynb", ".py"]

# your code here
```

## Problem 8: Age survey data cleaning

You're working with user survey data, and one of the questions asked for the participant's age — but the responses came in as free text.

Some entries are:
- Clean numeric values (e.g., `"25"`, `" 40 "`).
- Numeric values with extra words (e.g., `"42 years"`, `"21 years old"`).
- Non-numeric or junk entries (e.g., `"twenty-nine"`, `"N/A"`, `"unknown"`).

Write a program that extracts valid integer ages using this strategy:
1. Strip whitespace from the entry.
2. If the whole stripped string is numeric (`.isnumeric()`), it's a valid age.
3. Otherwise, split on whitespace (`.split()`) and check if the **first word** is numeric — if so, use that as the age.
4. Everything else is invalid — skip it.

Produce:
- A list of valid ages as integers.
- A count of invalid entries.
- A summary: `"Found N valid ages (M invalid). Mean age is X, ranging from Y to Z"`, where X is formatted to 1 decimal place.

Here is the correct output:

```
[25, 30, 42, 19, 50, 65, 61, 21, 100, 0, 28, 17, 41]
Found 13 valid ages (22 invalid). Mean age is 38.4, ranging from 0 to 100
```

```{code-cell} ipython3
age_entries = [
    "25",
    " 30 ",
    "twenty-nine",
    "N/A",
    " 42 years ",
    "unknown",
    "19",
    "eighteen",
    "  50",
    "Thirty",
    "65 ",
    "nineteeen",
    "61",
    "thirty-five ",
    " 21 years old",
    "forty two",
    "100",
    "seventy-five",
    "age: 33",
    "0",
    "  28",
    " 22yrs",
    "sixty",
    "eighty-four",
    "no idea",
    "thirty  ",
    "age is 45",
    "17",
    "One hundred and two",
    "35.5",
    " 41 ",
    "twenty two",
    "thirty three",
    "fifty-five",
    "age: seventy"
]

# your code here
```

## Problem 9: Make URLs more secure and private

You have a list of URLs. Some of them include tracking parameters like `utm_source`, `utm_medium`, or `utm_campaign`. And some use insecure `http://` instead of `https://`.

Write a program that:
- Takes the list of URLs and tracking parameter types as input.
- Produces:
    - A new list of cleaned URLs, where "clean" means:
        - Each URL no longer contains tracking parameters
        - Each URL begins with `https://`
    - A message like: `"Cleaned N URLs. Removed M tracking parameters total."`

*Hint:* URLs have the structure `base?param=value`. You can split on `"?"` to separate the base from the parameters. To check if a parameter is a tracker, check if it starts with any of the tracker param names. For the `http` → `https` fix, try `.replace()`.

Here is the correct output (first 5 cleaned URLs shown):

```
https://example.com/page
https://shop.com/item
https://news.com/article
https://cleanpage.org/about
https://blog.net/post?ref=homepage
...
Cleaned 37 URLs. Removed 20 tracking parameters total.
```

Note: URLs with non-tracking parameters like `?ref=homepage` or `?id=349` should keep those parameters intact.

Bonus:
- Also output a list of unique tracking sources (e.g., `twitter`, `email`, `instagram`).

```{code-cell} ipython3
urls = [
    "https://example.com/page?utm_source=twitter",
    "http://shop.com/item?utm_medium=email",
    "https://news.com/article?utm_campaign=launch",
    "http://cleanpage.org/about",
    "https://blog.net/post?ref=homepage",
    "http://foodie.co/recipe?utm_source=instagram",
    "https://travel.io/deal?utm_medium=social",
    "http://university.edu/apply?utm_campaign=f23",
    "https://movies.tv/watch?utm_source=youtube",
    "http://gallery.art/show?utm_medium=newsletter",
    "https://books.io/review?utm_campaign=holiday",
    "http://tools.dev/toolkit?ref=github",
    "https://weather.app/today",
    "http://events.org/signup?utm_source=facebook",
    "https://blog.dev/article?utm_medium=referral",
    "http://startup.biz/launch?utm_campaign=beta",
    "https://games.fun/play?ref=homepage",
    "http://codebase.dev/docs?utm_source=reddit",
    "https://products.shop/item?utm_medium=cpc",
    "http://videos.stream/clip?utm_campaign=drop",
    "https://example.org/home",
    "http://design.studio/portfolio?utm_source=dribbble",
    "https://charity.org/donate?utm_medium=email",
    "http://forum.net/post?id=349",
    "https://news.site/article?utm_campaign=viral",
    "http://library.info/search?ref=bookclub",
    "https://notes.app/doc?id=42",
    "http://inbox.me/mail?utm_medium=promo",
    "https://courses.edu/class?utm_source=google",
    "http://deals.biz/sale?utm_campaign=flash",
    "https://fashion.co/lookbook",
    "http://artist.page/portfolio?utm_source=behance",
    "https://journal.site/post?id=83",
    "http://photoshare.net/photo?utm_medium=ads",
    "https://planner.tools/task?id=11",
    "http://fitness.app/workout?utm_campaign=new_year",
    "https://simpleweb.dev/article"
]

tracker_params = ["utm_source", "utm_medium", "utm_campaign"]

# your code here
```

## Problem 10: VHS title cleaner

You've digitized a collection of old VHS tapes, but the label metadata contains messy extra tags — like `"[TV Rip]"` or `"[Do Not Duplicate]"` — that were added during recording or copying.

Write a program that:
1. Takes a list of movie titles.
2. Removes any tag from the list of junk tags. These tags:
    - Are always wrapped in square brackets.
    - May appear at the start or end of the title.
    - May use mixed capitalization (e.g., `[tv rip]`, `[ReMaStErEd]`).
3. Produces:
    - A cleaned list of titles (with extra whitespace stripped after removing tags).
    - A message like: `"Cleaned N movie titles that had unwanted VHS tags"`

*Hint:* Since the tags appear in mixed casing but `.replace()` is case-sensitive, one approach is to lowercase the entire title, then replace each junk tag with `""`, then `.strip()` the result. The downside is you lose the original title casing — but you can fix that with `.title()` at the end (good enough for most cases).

Here are the first 5 cleaned titles:

```
The Matrix
Jurassic Park
Titanic
Back To The Future
Star Wars: A New Hope
...
Cleaned 24 movie titles that had unwanted VHS tags
```

```{code-cell} ipython3
titles = [
    "The Matrix [tv rip]",
    "[Do Not Duplicate] Jurassic Park",
    "Titanic [VHS Transfer]",
    "[remastered] Back to the Future",
    "Star Wars: A New Hope",
    "The Lion King [TV RIP]",
    "[do not duplicate] Home Alone",
    "Forrest Gump",
    "The Godfather [Vhs Transfer]",
    "[TV Rip] Pulp Fiction",
    "Indiana Jones [Remastered]",
    "[Remastered] The Sixth Sense",
    "Fight Club [tv rip]",
    "The Dark Knight",
    "[TV rip] Gladiator",
    "Shrek [DO NOT DUPLICATE]",
    "[ReMaSTeRed] The Lord of the Rings",
    "Saving Private Ryan [vhs transfer]",
    "The Shawshank Redemption",
    "[Tv Rip] Inception",
    "Toy Story [Do Not Duplicate]",
    "The Silence of the Lambs",
    "[REMAStered] Finding Nemo",
    "Braveheart [TV RIP]",
    "[do not duplicate] The Notebook",
    "Cast Away [vhs transfer]",
    "The Truman Show",
    "Aliens [ReMaStErEd]",
    "[VHS Transfer] Monsters, Inc.",
    "The Goonies [Tv RiP]"
]

junk_tags = [
    "[tv rip]",
    "[do not duplicate]",
    "[remastered]",
    "[vhs transfer]"
]

# your code here
```

