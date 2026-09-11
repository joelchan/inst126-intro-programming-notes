---
jupytext:
  formats: md:myst
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

# Reading Colored Code (Syntax Highlighting)

## Why is the code colored?

Before this website or your editor shows you any code, it reads the code and sorts every piece into a category: keyword, string, number, comment, function name, variable name. Then it paints each category its own color. This is known as **[syntax highlighting](https://en.wikipedia.org/wiki/Syntax_highlighting)**.

The color will tell you what Python *thinks* a piece of code is, based on what you actually wrote. When something shows up in the wrong color, Python is reading your code differently than you meant it, and you can catch that before you run anything.

Note! The color tells you nothing about whether the code is *right*. Code can be correctly colored and still do the wrong thing.

```{admonition} Tip
Color answers "what kind of thing is this?" It does not answer "does this do what I want?"
```

## How syntax highlighting works in this notebook

This small program uses most of the categories you'll meet in the course:

```python
# figure out what a shift is worth
def compute_pay(hours, rate):
    pay = hours * rate
    if hours > 40 and rate > 0:
        pay = pay + 100
    return pay

shiftHours = 38
shiftRate = 15.5
shiftPay = compute_pay(hours=shiftHours, rate=shiftRate)
print(f"Your pay for this shift: ${shiftPay:.2f}")
```

This site has a light mode and a dark mode, and you can switch between them with the button in the top bar. The categories stay the same either way; only the paint changes.

| Category | Examples | Light mode | Dark mode |
| --- | --- | --- | --- |
| Comment | `# figure out what a shift is worth` | green | green |
| String | `"hello"`, `'a'`, `"42"` | dark red | salmon |
| Number | `42`, `15.5` | dark green | pale green |
| Keyword | `def`, `if`, `else`, `for`, `while`, `return`, `and`, `or`, `not`, `in`, `is`, `True`, `False`, `None` | blue | blue |
| Import keyword | `import`, `from` | purple | pink |
| Built-in function | `print`, `len`, `range`, `input`, `int`, `str` | brown | yellow |
| Function you defined | `compute_pay`, both where it is defined and where it is called | brown | yellow |
| Variable name | `hours`, `rate`, `pay` | navy | light blue |
| Operators and punctuation | `=`, `+`, `*`, `>`, `(`, `)`, `,`, `:` | black | light gray |

Two notes on what is specific to this site:
1.  We only apply syntax highlighting to code. Plain text is not colored. This includes the result printed underneath a code cell, such as an output, an error message, or the contents of a data file. 
2.  Code blocks here are numbered from 1 within each block so we can say "look at line 4" in class. VS Code numbers the whole file instead.

## How syntax highlighting works in editors like VS Code

Syntax *categories* are the same in any editor, because the sorting comes from Python's rules rather than from the editor. But the colors for each category often are different in other editors, since the category-color mappings are controlled by syntax highlighting themes. 

VS Code ships with several themes, and the default has changed over time. Recent versions start you on a theme called Dark 2026, where strings are light blue, comments are gray, function names are purple, and `def` is red.

To make your editor match these notes, switch to **Dark+** or **Light+**:

- Press `Cmd`+`K` then `Cmd`+`T` (Mac) or `Ctrl`+`K` then `Ctrl`+`T` (Windows/Linux)
- Or open the Command Palette (`Cmd`/`Ctrl`+`Shift`+`P`) and run **Preferences: Color Theme**

```{admonition} Squiggly underlines are a different feature
:class: tip
VS Code also draws red and yellow squiggles under code and pops up boxes when you hover. That is not syntax highlighting. It's a separate helper that guesses whether something is a mistake. Color tells you what the editor thinks a piece of code is; a squiggle tells you it thinks something is broken. You get color on this website, and color plus squiggles in VS Code.
```

## Syntax highlighting can help you catch typos before you run anything

Syntax highlighting is helpful for keeping track of what's going on in your code, and also what might be broken: specifically, syntax highlighting can alert you to when the *categories* you actually wrote in your code (e.g., string vs. int) are different from what you meant.

Here are some examples.

### 1. Missing quote for a string

```python
print("Hello, world)
total = 3 + 4
```

The closing parenthesis on line 1 is string-colored, the same as `Hello, world`. The opening `"` never closed, so the `)` got swallowed into the string. Close the quote before the parenthesis: `print("Hello, world")`.

Triple quotes make a bigger mess. An unclosed `"""` runs away for the rest of the file, so a large block of your program turning string-colored usually means a missing `"""`.

### 2. Misspelled function name

```python
pirnt("hello")
length = len("hello")
```

`len` on line 2 is in the built-in color. `pirnt` on line 1 is in the plain variable color, because Python has never heard of `pirnt` and assumes it's a variable you made up instead of a function. Misspellings of `print`, `len`, `range`, and `input` all show up this way.

### 3. String vs. Boolean `True` and `False`

```python
ready = true
ready2 = True
```

`True` on line 2 is keyword-colored, so we know it's a Boolean literal. `true` on line 1 is not. Python reads it as a variable that was never created, so the line gives you a `NameError`. The same goes for `False` and `None`.

### 4. Int vs. str numbers

```python
age = 42
age_text = "42"
```

Line 1 is int-colored and line 2 is string-colored. Both put the characters `4` and `2` on your screen, but they are different types: `age + 1` works and `age_text + 1` is a `TypeError`.

So when you hit a `TypeError` about `str` and `int`, scan for a value that is string-colored where you expected number-colored.


```{admonition} Try it
:class: tip
Open a new file in VS Code and type in the broken examples above. Find the color clue before you run anything. Then fix it and watch the colors change.
```
