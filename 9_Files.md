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

# 9: Files

## What are files?

From Python's perspective, files are data that is outside of the program's main memory. The PY4E textbook calls it "secondary memory".

Secondary memory is essential, because main memory, which holds all the data you create while your Python program is running, goes away once the program stops.

Secondary memory is a place to have data that is persistent. Sort of like long-term memory in humans.

I like this picture from the [PY4E textbook](https://www.py4e.com/html3/07-files) to illustrate the point:

<img src="https://www.py4e.com/images/arch.svg" height=600 width=800></img>

The middle box is where the Python program "lives".

Sometimes Python needs a way to connect to the outside world: "input and output devices" on the left, "network" (e.g., the internet!) on the right, and "secondary memory" (e.g., the hard drive! files!) on the right.

So far our programs have been self-contained (except for talking to the outside world via `input()` and `print()`).

Now we will talk about how to access and write to files in secondary memory so our data can persist beyond a single Python session/program, and also access data that is... more than we can just write into a single Python file or Jupyter cell.

## The `open()` function, and the file handle object

Python interacts with files using the **file handle** object. The `open()` function, as you might suspect, opens a file handle for a file.

Here is an example. What do you think is in `fhand`?

```{code-cell} ipython3
fhand = open('assets/mbox-email-receipts.txt', 'r')
print(fhand)
```

The main parameters of `.open()` are:
1. Path: The *path* to the file you want to connect to
2. Mode: A specification of *how* you want to connect (to read, to write, etc.).

But its return value is *not* the contents of the file! Instead, its output is a **file handle** object: `io.TextIOWrapper`.

I like this picture from the PY4E textbook:

<img src="https://www.py4e.com/images/handle.svg" height=800 width=600></img>

What kind of thing is it? What does it allow us to do?

Just like lists have methods like `.append()`, strings have methods like `.upper()` and `.split()`, and dictionaries have methods like `.update()` and `.get()`, file handle objects have key methods that enable us to work with the actual file:
- read the contents of the file (with `.read()` or `.readlines()`)
- write to the file (with `.write()` or `.writelines()`)

So, in the example above, I've opened a file handle for the mbox-email-receipts.txt file, in the reading mode (`r`), which enables me to use `.read()` to read the contents of the file.

We'll return to the concepts of mode and operations in a bit. First, we need to understand how to direct Python to a file so we can actually open a file handle to it!

## File paths

File paths are a way of giving Python directions to the file's location.

In the example above, the file path was `'assets/mbox-email-receipts.txt'`

There are two parts to a file path:
1. The filename itself.
2. The path/directions to the folder it's in "from where you are"

The filename is obvious, but the path/directions part is not. So let's take a closer look.

### Path, aka directions to a folder

Think of a file path like giving directions to a room in a building. To write a path, you need to know:
1. **Where you are** (your program's **current working directory**)
2. **Where the file is** (the target folder)
3. **How to get there** (the path connecting them)

The building blocks of a path are:
- **Folder names** — the names of directories you need to go through
- **`/`** — a separator between folder names (and between the last folder and the filename). Think of it as "go into..."
- **`..`** — means "go up one level" (to the parent folder). You only need this when the file is *outside* of your current directory — for example, in a sibling folder or a parent folder.

For example, in our earlier path `'assets/mbox-email-receipts.txt'`:
- `assets` is the folder name
- `/` separates the folder from the filename
- `mbox-email-receipts.txt` is the file

This path works because the `assets` folder is inside our current working directory. We can verify this using the `os` library:

```{code-cell} ipython3
import os # get all the data and functions from the os library

cwd = os.getcwd() # show me where I am on the hard drive
current_view = os.listdir() # list all the names of things I can immediately see in my current location

print(f"You are currently in {cwd}\n")
print(f"Here are all the things you can see:")
for thingname in current_view:
    print(thingname)
```

#### When would you need `..`?

Imagine your files are organized like this:

```
my_project/
├── code/
│   └── analysis.py      ← your program is here
│   └── inputs/
        └── rawdata.csv
├── outputs/
│   └── results.csv
└── README.md
```

If your program `analysis.py` is running inside the `code/` folder, you can read `rawdata.csv` with the filepath `"inputs/rawdata.csv"` (which basically says "look for the `inputs` folder, then go inside and look for the file with the name `rawdata.csv`). But you can't do that with the file `results.csv`, because it is *not* in a subfolder — it's in a **sibling** folder called `outputs/`. To reach it, you need to first go **up** one level (from `code/` to `my_project/`), *then* **down** into `outputs/`, and after you are in that folder, look for the file with the name `results.csv`:

```python
# from inside code/, go up one level (..), then into outputs/
fpath = "../outputs/results.csv"
```

You can read `..` as "go to the parent folder." Here's how the path breaks down:
- `..` — go up from `code/` to `my_project/`
- `/outputs` — go into the `outputs/` folder
- `/results.csv` — that's the file

If you wanted to reach `README.md` (which is one level up, not in any subfolder):

```python
# just go up one level
fpath = "../README.md"
```

You can even chain `..` to go up multiple levels: `../../some_file.txt` goes up two levels. But if you find yourself doing that, it's often a sign that you should reorganize your files!

### Relative vs. absolute file paths

So far we have been discussing **relative** file paths: paths that describe how to locate a file *relative to your program's current working directory*.

It is also possible to specify **absolute** file paths: the full location of a file from the root of your filesystem, like `/Users/joel/Documents/data.csv` on Mac or `C:\Users\joel\Documents\data.csv` on Windows.

Absolute paths are almost never a good idea for code you plan to share or submit. If you use an absolute path, your program will break on anyone else's computer, because their filesystem will have different usernames, folder structures, and locations.

For this reason, in this class, we want you to practice writing **relative** file paths for all of your programs that deal with files.

### A practical note: "where am I?" depends on your setup

There's one wrinkle with relative paths that trips up a lot of beginners: **your current working directory depends on how you run your script**, not where the script file lives.

For example, if your script `analysis.py` is in `project1/code/`, you might expect that `open("notes.txt")` opens a file in the same folder. And it will — *if* Python's working directory is `project1/code/`. But some editors (like VS Code) run your script from the **top-level folder you opened in the editor**, not from the script's own folder. So if you opened the `school/` folder in VS Code, the working directory might be `school/`, and `open("notes.txt")` would look for `notes.txt` in `school/` — not in `project1/code/`.

#### The simplification we use in this class

To avoid this confusion, in our assignments we include a small "hotfix" at the top of your Python files:

```python
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
```

This tells Python: **"change the working directory to whatever folder this script is in."** With this line in place, relative paths like `"notes.txt"` and `"Subfile/data.csv"` always work as you'd expect — relative to the script itself.

You'll see this in your PCE assignments with a `DO NOT MODIFY` comment. Just leave it there and write your paths relative to the script's location. I'll also include it in any practice files I share in class, and recommend that you put it in your own practice files as well while you're getting comfortable with the idea of relative paths. To simplify things in VSCode for practice purposes, you can also enable the following setting in the Python extension (that lets you run Python files in VSCode):

1. **Open Settings**: Press Ctrl+, (Windows/Linux) or Cmd+, (macOS).
2. **Search**: Type python.terminal.executeInFileDir (or search for "Python Terminal").
3. **Enable**: Check the box for "Python > Terminal: Execute In File Dir". This ensures the terminal changes its directory to the file's folder before executing your code.

#### What about "real" projects?

In professional settings, programs are often run from the **top-level project directory** (the *root* of the repository). In that case, all paths are relative to the project root, not to any individual script. 

For example, consider our example above again:

```
my_project/
├── code/
│   └── analysis.py      ← your program is here
│   └── inputs/
        └── rawdata.csv
├── outputs/
│   └── results.csv
└── README.md
```

a script in `code/analysis.py` might open a file in a sibling folder with the path `outputs/results.csv` (no `..` operator!) and succeed *if* the program is run from the project root (`my_project`) where both `code/` and `outputs/` are visible.

The core intuition of relative paths is the same as in our program/script-centric opening examples — you're still describing "how to get from some starting point to where the file is." The only thing that changes is your starting point: **the script's folder** (what we use in this class) vs. **the project root** (common in professional practice). 

Running programs in this way (from the project root) is helpful especially when (like in our PCEs), functions within `.py` (or other files) are *imported* and used in other files, which may be in a different location. This is one reason why, for example, VSCode's Python defaults to running scripts from the "currently open folder" (which often in practice will be the project root - i.e., the option `Terminal: Execute in File Dir` is disabled by default; when you get to professional practice, you'l'l probably want to go back to disabling this setting). 

## Working with files

The second parameter of `open()` specifies the **mode** — what you intend to do with the file. Think of it as a permission system: you can only do operations that match the mode you opened with. Let's look at each mode together with the operations it enables.


### Reading files (mode `'r'`)

To read a file, open it with `'r'` (or leave the mode out entirely — `'r'` is the default).

```{code-cell} ipython3
path = "assets/"
fname = "mbox-email-receipts.txt"
fpath = f"{path}{fname}"

# open in read mode
fhand = open(fpath, 'r')
```

Once you have a file handle open for reading, there are two main ways to get the contents:

**`.read()`** reads the whole file as a single `string`:

```{code-cell} ipython3
fhand = open(fpath, 'r')
content_s = fhand.read()
content_s
```

**`.readlines()`** reads the whole file as a `list` of strings (one per line):

```{code-cell} ipython3
fhand = open(fpath, 'r')
content_list = fhand.readlines()
content_list
```

In both cases, you end up with strings. You can then parse them to do what you want — for example, splitting the single string on `"\n"` to get individual lines:

```{code-cell} ipython3
content_s.split("\n")
```

#### Iterating through a file line by line

You can also loop directly over a file handle, which gives you one line at a time — just like iterating over a list. This is handy when you want to process each line without loading the entire file into memory.

```{code-cell} ipython3
thursday_records = []
fhand = open(fpath, 'r')
for line in fhand:
    if 'Thu' in line:
        thursday_records.append(line)

thursday_records
```

#### Chaining open + read

Since `open()` returns a file object, you can chain `.read()` or `.readlines()` directly onto it — no need for an intermediate variable:

```{code-cell} ipython3
fstring = open("assets/newfile2.txt", "r").read()
fstring
```

This is the same **chaining** concept from strings: each expression produces a result, and you can immediately call a method on that result. `open(...)` produces a file object → `.read()` is called on it → returns a string.

In the next module we will learn how the `pandas` library connects to files to cover common parsing situations (e.g., I have a spreadsheet, I want to go straight into a `dataframe` for analysis). More on that later! The concepts of accessing files will still apply.

### Writing files (mode `'w'`)

To write to a file, open it with `'w'`. This gives you access to the `.write()` method — think of it as similar to `print()`, except it writes to a file instead of the screen.

```{code-cell} ipython3
path = "assets/"
fname = "newfile.txt"
fpath = f"{path}{fname}"

fhand = open(fpath, 'w')
fhand.write("Hello world, my programming friends!")
fhand.close()
```

A few important things to know about `'w'` mode:

**It creates the file if it doesn't exist.** You don't need to create the file beforehand — Python will make it for you.

```{code-cell} ipython3
path = "assets/"
fname = "newfile-from-class.txt"
fpath = f"{path}{fname}"

fhand = open(fpath, 'w')
fhand.write("This is a new file from class!")
fhand.close()
```

**It overwrites the file if it already exists!** Be careful — opening in `'w'` mode erases the previous contents.

```{code-cell} ipython3
path = "assets/"
fname = "newfile.txt"
fpath = f"{path}{fname}"

fhand = open(fpath, 'w')
fhand.write("Hello world from INST126!")
fhand.close()
```

**You can write multiple times before closing:**

```{code-cell} ipython3
path = "assets/"
fname = "newfile5.txt"
fpath = f"{path}{fname}"

fhand = open(fpath, 'w')
fhand.write("Hello INST126!")
fhand.write("\n\nAnother line")
fhand.close()
```

**If you opened in read mode, Python won't let you write** — this is good for security!

```{code-cell} ipython3
:tags: [raises-exception]

fhand = open("assets/newfile.txt", 'r')
fhand.write("This will fail!")
fhand.close()
```

#### Closing files and the `with` pattern

You may be told that you need to `.close()` a file to safely exit the connection. As best we can tell, this used to be very important, but in Python 3 we haven't been able to find concrete, repeatable consequences of forgetting it *in this course*. However, it can matter in professional settings: https://realpython.com/why-close-file-python/

To avoid worrying about it, you can use the **`with` pattern**, which automatically closes the file when the block finishes:

```{code-cell} ipython3
path = "assets/"
fname = "newfile.txt"
fpath = f"{path}{fname}"

with open(fpath, 'w') as fhand:
    fhand.write("Hello world! Something new")
# file is automatically closed here
```

The `with` pattern works for reading too:

```{code-cell} ipython3
with open("assets/newfile2.txt", 'r') as fhand:
    content = fhand.read()
print(content)
```

### Appending to files (mode `'a'`)

Append mode is a variant of write mode: it lets you add content to the **end** of a file without erasing what's already there.

```{code-cell} ipython3
path = "assets/"
fname = "newfile.txt"
fpath = f"{path}{fname}"

fhand = open(fpath, 'a')
fhand.write("\nMore stuff from INST126!")
fhand.close()
```

This is useful when you want to build up a file over time — like a log file.

### Summary of modes

| Mode | What it does | Creates file? | Overwrites? |
|---|---|---|---|
| `'r'` | Read only (default) | No — error if missing | No |
| `'w'` | Write (from scratch) | Yes | Yes! |
| `'a'` | Append (add to end) | Yes | No |

There are more advanced modes (e.g., `'rb'` for reading binary files), but `'r'`, `'w'`, and `'a'` cover most of what you'll need.

## Practice: working with files

### Practice: Code Tracing with Files

For each question, predict what happens when the code runs. Use this folder structure for all questions:

```
my_project/
├── app/
│   ├── main.py          ← your program
│   └── config.txt       (contains: "debug=True")
├── data/
│   ├── names.txt        (contains: "Alice\nBob\nCharlie")
│   └── scores.csv       (contains: "Alice,95\nBob,82\nCharlie,91")
└── readme.txt            (contains: "Welcome to my project")
```

#### Trace 1

```python
fhand = open("config.txt", "r")
content = fhand.read()
print(content)
print(type(content))
```

- A) `debug=True` then `<class 'str'>`
- B) `debug=True` then `<class 'list'>`
- C) `['debug=True']` then `<class 'list'>`
- D) `config.txt` then `<class 'str'>`

````{admonition} Answer:
:class: toggle

**A) `debug=True` then `<class 'str'>`**

`.read()` returns the entire file contents as a single **string**. It doesn't split it into lines or wrap it in a list.
````

#### Trace 2

```python
fhand = open("../data/names.txt", "r")
lines = fhand.readlines()
print(len(lines))
print(lines[0])
```

- A) `1` then `Alice\nBob\nCharlie`
- B) `3` then `Alice\n`
- C) `3` then `Alice`
- D) `15` then `A`

````{admonition} Answer:
:class: toggle

**B) `3` then `Alice\n`**

`.readlines()` returns a **list** of strings, one per line. The file has 3 lines, so `len(lines)` is 3. Each line *includes* the trailing `\n` newline character (except possibly the last line). So `lines[0]` is `"Alice\n"`, not `"Alice"`.

Note the path: `../data/names.txt` goes up from `app/` to `my_project/`, then into `data/`.
````

#### Trace 3

```python
fhand = open("config.txt", "w")
fhand.write("debug=False")
fhand.close()

fhand = open("config.txt", "r")
print(fhand.read())
```

- A) `debug=True\ndebug=False`
- B) `debug=True`
- C) `debug=False`
- D) Error: can't open the same file twice

````{admonition} Answer:
:class: toggle

**C) `debug=False`**

Opening in `'w'` mode **erases** the previous contents and starts fresh. The original `"debug=True"` is gone. After writing and closing, re-opening in `'r'` mode shows only the new content. If you wanted to keep the original and add to it, you'd use `'a'` (append) mode.
````

#### Trace 4

```python
fhand = open("config.txt", "a")
fhand.write("\nverbose=True")
fhand.close()

fhand = open("config.txt", "r")
print(fhand.read())
```

- A) `verbose=True`
- B) `debug=True`
- C) `debug=True\nverbose=True`
- D) Error: can't append and then read

````{admonition} Answer:
:class: toggle

**C) `debug=True\nverbose=True`**

`'a'` mode **appends** to the end of the file without erasing existing content. So the original `"debug=True"` stays, and `"\nverbose=True"` is added after it. When printed, the `\n` creates a line break, so you'd see:
```
debug=True
verbose=True
```
````

#### Trace 5

```python
fhand = open("config.txt", "r")
fhand.write("new content")
```

- A) The file now contains `"new content"`
- B) The file is unchanged; the write is silently ignored
- C) `UnsupportedOperation` error
- D) `FileNotFoundError`

````{admonition} Answer:
:class: toggle

**C) `UnsupportedOperation` error**

The file was opened in read mode (`'r'`), so Python won't let you write to it. This is a safety feature — the mode acts as a permission system. You'd need `'w'` or `'a'` to write.
````

#### Trace 6

```python
fhand = open("names.txt", "r")
content = fhand.read()
print(content)
```

- A) `Alice\nBob\nCharlie`
- B) `FileNotFoundError`
- C) An empty string `""`
- D) `None`

````{admonition} Answer:
:class: toggle

**B) `FileNotFoundError`**

`names.txt` is in the `data/` folder, not in `app/` where our program runs. The correct path would be `"../data/names.txt"`. Python is very literal — if the path doesn't exactly match where the file is, it crashes.
````

#### Trace 7

```python
fhand = open("../data/scores.csv", "r")
names = []
for line in fhand:
    parts = line.strip().split(",")
    names.append(parts[0])
print(names)
```

- A) `['Alice,95', 'Bob,82', 'Charlie,91']`
- B) `['Alice', 'Bob', 'Charlie']`
- C) `['95', '82', '91']`
- D) `[['Alice', '95'], ['Bob', '82'], ['Charlie', '91']]`

````{admonition} Answer:
:class: toggle

**B) `['Alice', 'Bob', 'Charlie']`**

Each iteration gives one line. `.strip()` removes the trailing `\n`. `.split(",")` splits into `['Alice', '95']` etc. `parts[0]` grabs just the name. This is a common pattern for parsing CSV-like data line by line.
````

#### Trace 8

```python
fhand = open("config.txt", "w")
fhand.write("mode=test")
# forgot to close!
fhand2 = open("config.txt", "r")
content = fhand2.read()
print(len(content))
```

- A) `9`
- B) `0`
- C) `9` or `0` (unpredictable)
- D) Error: file is locked

````{admonition} Answer:
:class: toggle

**C) `9` or `0` (unpredictable)**

When you write without closing (or using `with`), the data might still be in a buffer and not yet written to disk. Reading the file before the write is flushed could give you an empty file (`0`) or the full content (`9`), depending on timing and your OS. This is why closing files (or using `with`) matters!
````

#### Trace 9

```python
with open("../data/names.txt", "r") as f:
    first_line = f.readline()
print(first_line.strip())
print(f.read())
```

- A) `Alice` then `Bob\nCharlie`
- B) `Alice` then `ValueError` (file is closed)
- C) `Alice\n` then `Bob\nCharlie`
- D) `Alice` then an empty string

````{admonition} Answer:
:class: toggle

**B) `Alice` then `ValueError` (file is closed)**

The `with` block automatically closes the file when the block ends. `first_line` works fine (it was read *inside* the block). But `f.read()` on line 3 is *outside* the block — the file is already closed, so Python raises a `ValueError: I/O operation on closed file`.
````

#### Trace 10

```python
data = open("../data/scores.csv", "r").read().strip().split("\n")
print(len(data))
print(data[1])
```

- A) `3` then `Bob,82`
- B) `1` then `Alice,95\nBob,82\nCharlie,91`
- C) `3` then `Bob`
- D) Error: too many operations chained

````{admonition} Answer:
:class: toggle

**A) `3` then `Bob,82`**

This chains four operations: `open()` returns a file object → `.read()` returns the whole file as one string → `.strip()` removes trailing whitespace/newlines → `.split("\n")` splits into a list of lines. The result is `['Alice,95', 'Bob,82', 'Charlie,91']` — 3 items, and index `[1]` is `'Bob,82'`.
````

### Practice: file paths

Sample files for all path exercises are in the `sample_files/` folder if you want to test your answers!

Each set starts with easier problems (same folder, subfolders) and builds up to harder ones (going up with `..`).

Each set starts with easier problems (same folder, subfolders) and builds up to harder ones (going up with `..`).

#### Practice Set 1: School project

```
school/
├── projects/
│   ├── project1/
│   │   ├── code/
│   │   │   ├── analysis.py      ← your program (for P1-P4)
│   │   │   └── notes.txt
│   │   └── data/
│   │       └── survey.csv
│   └── project2/
│       ├── main.py              ← your program (for P5-P6)
│       └── output/
│           └── results.csv
├── notes/
│   └── lecture1.txt
└── grades.csv
```

**P1.** Your program is `analysis.py`. Open `notes.txt`, which is in the **same folder**.

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "notes.txt"
```

The file is right next to your program — just use the filename, no path needed.
`````

**P2.** Your program is `main.py`. Open `results.csv`, which is in a **subfolder** called `output/`.

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "output/results.csv"
```

Go into the `output/` subfolder, then the file. No `..` needed — you're going *down*.
`````

**P3.** Your program is `analysis.py`. Open `survey.csv`, which is in a **sibling folder** (`data/`).

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "../data/survey.csv"
```

From `code/`, go up to `project1/` (`..`), then into `data/`, then the file.
`````

**P4.** Your program is `analysis.py`. Open `grades.csv`, which is **several levels up**.

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "../../../grades.csv"
```

From `code/`, go up to `project1/` (`..`), up to `projects/` (`../..`), up to `school/` (`../../..`), and there's `grades.csv`.
`````

**P5.** Your program is `main.py`. Open `lecture1.txt` (in the `notes/` folder).

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "../../notes/lecture1.txt"
```

From `project2/`, go up to `projects/` (`..`), up to `school/` (`../..`), then into `notes/`, then the file.
`````

**P6.** Your program is running from the `school/` folder. Open `survey.csv`, `lecture1.txt`, and `grades.csv`.

```{code-cell} ipython3
# fpath_survey = ???
# fpath_lecture = ???
# fpath_grades = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath_survey = "projects/project1/data/survey.csv"
fpath_lecture = "notes/lecture1.txt"
fpath_grades = "grades.csv"
```

From `school/`, everything is below you — no `..` needed. `grades.csv` is right here, so it's just the filename.
`````

#### Practice Set 2: Web project

```
webapp/
├── src/
│   ├── pages/
│   │   ├── home.py          ← your program
│   │   └── styles.css
│   └── utils/
│       └── helpers.py
├── config/
│   └── settings.json
├── public/
│   ├── index.html
│   └── images/
│       └── logo.png
└── README.md
```

**P7.** Your program is `home.py`. Open `styles.css`, which is in the **same folder**.

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "styles.css"
```

Same folder — just the filename.
`````

**P8.** Your program is `home.py`. Open `helpers.py` (in the sibling `utils/` folder).

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "../utils/helpers.py"
```

From `pages/`, go up to `src/` (`..`), then into `utils/`, then the file.
`````

**P9.** Your program is `home.py`. Open `settings.json` (in the `config/` folder).

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "../../config/settings.json"
```

From `pages/`, go up to `src/` (`..`), up to `webapp/` (`../..`), then into `config/`, then the file.
`````

**P10.** Your program is `home.py`. Open `README.md` (at the top of the project).

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "../../README.md"
```

From `pages/`, go up to `src/` (`..`), up to `webapp/` (`../..`), and `README.md` is right there.
`````

#### Practice Set 3: Research project

```
research/
├── experiment1/
│   ├── raw_data/
│   │   └── responses.csv
│   └── scripts/
│       ├── analyze.py       ← your program
│       └── log.txt
├── experiment2/
│   └── raw_data/
│       └── responses.csv
├── shared/
│   └── templates/
│       └── report_template.txt
└── participants.csv
```

**P11.** Your program is `analyze.py`. Open `log.txt`, which is in the **same folder**.

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "log.txt"
```

Same folder — just the filename.
`````

**P12.** Your program is `analyze.py`. Open experiment 1's `responses.csv` (in the sibling `raw_data/` folder).

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "../raw_data/responses.csv"
```

From `scripts/`, go up to `experiment1/` (`..`), then into `raw_data/`, then the file.
`````

**P13.** Your program is `analyze.py`. Open experiment **2**'s `responses.csv`.

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "../../experiment2/raw_data/responses.csv"
```

From `scripts/`, go up to `experiment1/` (`..`), up to `research/` (`../..`), then into `experiment2/`, then `raw_data/`, then the file.
`````

**P14.** Your program is `analyze.py`. Open `participants.csv` (at the top level).

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "../../participants.csv"
```

From `scripts/`, go up to `experiment1/` (`..`), up to `research/` (`../..`), and `participants.csv` is right there.
`````

#### Practice Set 4: Music app

```
music_app/
├── library/
│   ├── rock/
│   │   └── tracks.csv
│   └── jazz/
│       └── tracks.csv
├── playlists/
│   └── my_playlists.csv
├── tools/
│   ├── organizer.py         ← your program (for P15-P18)
│   ├── settings.txt
│   └── output/
│       └── report.csv
└── config.json
```

**P15.** Your program is `organizer.py`. Open `settings.txt`, which is in the **same folder**.

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "settings.txt"
```

Same folder — just the filename.
`````

**P16.** Your program is `organizer.py`. Open `report.csv`, which is in a **subfolder** called `output/`.

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "output/report.csv"
```

Go into the `output/` subfolder, then the file. No `..` needed.
`````

**P17.** Your program is `organizer.py`. Open `config.json` (one level up).

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "../config.json"
```

From `tools/`, go up to `music_app/` (`..`), and `config.json` is right there.
`````

**P18.** Your program is `organizer.py`. Open the rock `tracks.csv`.

```{code-cell} ipython3
# fpath = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath = "../library/rock/tracks.csv"
```

From `tools/`, go up to `music_app/` (`..`), then into `library/`, then `rock/`, then the file.
`````

**P19.** Your program is running from the `music_app/` folder. Open the jazz `tracks.csv`, `my_playlists.csv`, and `config.json`.

```{code-cell} ipython3
# fpath_jazz = ???
# fpath_playlists = ???
# fpath_config = ???
```

`````{admonition} Answer:
:class: toggle

```python
fpath_jazz = "library/jazz/tracks.csv"
fpath_playlists = "playlists/my_playlists.csv"
fpath_config = "config.json"
```

From `music_app/`, everything is below you — no `..` needed.
`````

### Practice: reading, writing, and iterating

**P20.** Read the entire contents of `assets/mbox-email-receipts.txt` into a single string and print how many characters it contains.

```{code-cell} ipython3
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
fhand = open("assets/mbox-email-receipts.txt", "r")
content = fhand.read()
print(len(content))
```
`````

**P21.** Read `assets/mbox-email-receipts.txt` using `.readlines()` and print how many lines the file has.

```{code-cell} ipython3
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
fhand = open("assets/mbox-email-receipts.txt", "r")
lines = fhand.readlines()
print(len(lines))
```
`````

**P22.** Write your name and your favorite programming concept (on separate lines) to a new file called `assets/about_me.txt`.

```{code-cell} ipython3
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
fhand = open("assets/about_me.txt", "w")
fhand.write("Joel\n")
fhand.write("Dictionaries\n")
fhand.close()
```

Or with the `with` pattern:

```python
with open("assets/about_me.txt", "w") as fhand:
    fhand.write("Joel\n")
    fhand.write("Dictionaries\n")
```
`````

**P23.** The file `assets/about_me.txt` already exists from the previous exercise. **Append** a third line to it that says `"INST126"` — without erasing what's already there.

```{code-cell} ipython3
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
fhand = open("assets/about_me.txt", "a")
fhand.write("INST126\n")
fhand.close()
```

Key: use `'a'` (append), not `'w'` (write). `'w'` would erase the existing content!
`````

**P24.** Write a list of names to a file called `assets/roster.txt`, one name per line.

```{code-cell} ipython3
names = ["Joel", "Sarah", "Rony", "Kacie"]
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
names = ["Joel", "Sarah", "Rony", "Kacie"]
with open("assets/roster.txt", "w") as fhand:
    for name in names:
        fhand.write(name + "\n")
```
`````

**P25.** Iterate through `assets/mbox-email-receipts.txt` line by line. Collect only the lines that contain `"Jan  4"` into a list, and print how many there are.

```{code-cell} ipython3
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
jan4_records = []
fhand = open("assets/mbox-email-receipts.txt", "r")
for line in fhand:
    if "Jan  4" in line:
        jan4_records.append(line)
print(len(jan4_records))
```
`````

**P26.** Iterate through `assets/mbox-email-receipts.txt` line by line. For each line, extract the email address (the second word) and collect all unique email addresses into a list. Print the list and its length.

*Hint: each line looks like `"From someone@example.com Thu Jan  3 ..."`. Use `.split()` and index `[1]` to get the email.*

```{code-cell} ipython3
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
unique_emails = []
fhand = open("assets/mbox-email-receipts.txt", "r")
for line in fhand:
    email = line.split()[1]
    if email not in unique_emails:
        unique_emails.append(email)
print(unique_emails)
print(len(unique_emails))
```
`````

**P27.** Read `assets/mbox-email-receipts.txt`, extract the email address from each line, and write just the email addresses to a new file called `assets/emails_only.txt` (one per line).

```{code-cell} ipython3
# your code here
```

`````{admonition} Answer:
:class: toggle

```python
with open("assets/mbox-email-receipts.txt", "r") as infile:
    with open("assets/emails_only.txt", "w") as outfile:
        for line in infile:
            email = line.split()[1]
            outfile.write(email + "\n")
```

This combines reading, parsing, and writing — a very common pattern!
`````

## Common errors with files

### Can't find the file: FileNotFoundError

```{code-cell} ipython3
:tags: [raises-exception]

fhand = open("mbox-email-receipts.txt", 'r')
print(fhand.read())
```

In basically all cases, the issue/mismatch is between your understanding of where the thing is (path) or what its name is (fname) and what you actually told Python.

This could be a:
- Misspelling (remember how literal Python is?)
- Wrong/missing directions (e.g., missing a folder, or an operation)

### Wrong connection type/permission: UnsupportedOperation

```{code-cell} ipython3
# opened in read mode, and reading works fine
fhand = open("assets/mbox-email-receipts.txt", 'r')
print(fhand.read())
fhand.close()
```

```{code-cell} ipython3
:tags: [raises-exception]

# opened in read mode
# but tried to write to it
fhand = open("assets/mbox-email-receipts.txt", 'r')
print(fhand.write("Hello world"))
```

```{code-cell} ipython3
import os
os.listdir()
```

## Writing different kinds of things to files

Often we just pass strings directly into `.write()` to write data to a file. But sometimes we want to write specific kinds of data structures to a file and preserve its structure in some way. One example is saving a dictionary to a file.

We could write the dictionary to the file like this:

```{code-cell} ipython3
d = {"a": 1, "b": 2, "c": 3}
with open("dictionary.txt", "w") as f:
    f.write(str(d)) # write the string representation of the dictionary to the file
```

But sometimes you want to write the dictionary in a more structured way, like [JSON](https://www.json.org/json-en.html) (which stands for JavaScript Object Notation; a standard way to represent data structures in string form to pass data between programs in a way that makes it easy to export/import with consistent structure and make parsing easy, often on the Internet).

To do this, we can use the `json` library to neatly package up a dictionary to be able to write it to a file and have confidence that it retains its essential structure and can easily be read back into a dictionary from a file.

The code for doing so might look like this:

```{code-cell} ipython3
import json
# write the dictionary to a file in JSON format
with open("dictionary.json", "w") as f:
    str_d = json.dumps(d, indent=4) # convert the dictionary to a JSON string, with an indentation of 4 spaces
    f.write(str_d) # write the JSON string to the file
```

Then the contents of the file will look like this:

```
{
    "a": 1,
    "b": 2,
    "c": 3
}
```

This is nice and easy to read for humans, and especially pays off for longer and more complex dictionaries. For instance:

```{code-cell} ipython3
complex_d = {
    "a": 1,
    "b": 2,
    "c": {
        "d": 3,
        "e": 4
    },
    "f": [5, 6, 7],
    "g": {
        "h": 8,
        "i": {
            "j": 9,
            "k": 10
        }
    }
}

with open("complex_dictionary.json", "w") as f:
    str_d = json.dumps(complex_d, indent=4) # convert the dictionary to a JSON string, with an indentation of 4 spaces
    f.write(str_d) # write the JSON string to the file
```

The `.json` file contents will look like this:

```
{
    "a": 1,
    "b": 2,
    "c": {
        "d": 3,
        "e": 4
    },
    "f": [
        5,
        6,
        7
    ],
    "g": {
        "h": 8,
        "i": {
            "j": 9,
            "k": 10
        }
    }
}
```

Instead of
```
{'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}, 'f': [5, 6, 7], 'g': {'h': 8, 'i': {'j': 9, 'k': 10}}}
```

As a bonus, you can use the `json.loads()` function to read the contents of a `.json` file directly into a dictionary in a Python program, like this:

```{code-cell} ipython3
with open("dictionary.json", "r") as f:
    str_d = f.read() # read the contents of the file into a string
    d = json.loads(str_d) # convert the JSON string back to a dictionary
    print(d)
```

The `dump()` and `load()` functions from the `json` library make this work even simpler!

```{code-cell} ipython3
# write the dictionary to a file in JSON format
with open("dictionary.json", "w") as f:
    json.dump(d, f, indent=4) # convert the dictionary to a JSON string, with an indentation of 4 spaces, and write to f
```

```{code-cell} ipython3
with open("dictionary.json", "r") as f:
    d = json.load(f) # read the contents of the JSON file into a dictionary
    print(d)
```

### Aside: What is a library?

You can think of a library (also called a module) as a **collection of functions and data structures**. You *import* a library (or subsets of it) into your program so you have access to special functions or data structures.

You are already using Python's standard library, which includes built-in functions like `print()`, and built-in data structures like `str` and `dict`. Every time you fire up Python, these are "imported" into your program in the background.

As you advance in your programming career, you will often find that you want to solve some (sub)problems that others have tried to do, and wrote a collection of functions and/or data structures to solve those problems really well, and saved that collection into a library that others can use. Take advantage of this!

For instance, `os` is a library that has convenient methods for handling files:

```{code-cell} ipython3
# import the os library
import os
# see the current working directory
print(os.getcwd())
# list the contents of the current working directory
print(os.listdir())
# check if a file exists
print(os.path.exists("assets/mbox-email-receipts.txt"))
# make a file path using os.path.join
path = os.path.join("assets", "mbox-email-receipts.txt")
print(path)
```

The `import` keyword followed by the name of the library makes the functions and data structures in the library available to your running Python interpreter. This is analogous to how `def` makes a function available for your program to call/use.

Once you import a library, you can access the functions in that library by first declaring the name of the library (e.g., `json`), then a `.`, then the name of the method (e.g., `dumps()`): notice that the syntax is similar to calling methods for data structures (e.g., `some_list.append()`).
