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

# Warmup: Code Tracing (Lists + Loops)

These problems combine lists with definite and indefinite loops. Predict the output before running each cell!

## Trace 1

```{code-cell} ipython3
:tags: [remove-output]

scores = [10, 20, 30, 40]
total = 0
for score in scores:
    total = total + score
print(total)
```

**What is the output?**

A) `40`
B) `100`
C) `10`
D) `10 20 30 40`

````{admonition} Answer:
:class: toggle

**B) `100`**

The `for` loop iterates through every item in the list, adding each one to `total`. After all four iterations: 0 + 10 + 20 + 30 + 40 = 100.
````

## Trace 2

```{code-cell} ipython3
:tags: [remove-output]

words = ["hi", "bye", "ok"]
result = []
for word in words:
    result.append(word.upper())
print(result)
```

**What is the output?**

A) `["hi", "bye", "ok"]`
B) `["HI", "BYE", "OK"]`
C) `HI BYE OK`
D) `["Hi", "Bye", "Ok"]`

````{admonition} Answer:
:class: toggle

**B) `["HI", "BYE", "OK"]`**

Each iteration calls `.upper()` on the current word and appends the result to `result`. `.upper()` returns a new all-uppercase string. The list itself is printed, so you see the brackets and quotes.
````

## Trace 3

```{code-cell} ipython3
:tags: [remove-output]

nums = [5, 12, 3, 8, 1]
big = []
for num in nums:
    if num > 4:
        big.append(num)
print(big)
print(len(big))
```

**What is the output?**

A) `[5, 12, 8]` then `3`
B) `[5, 12, 3, 8]` then `4`
C) `[12, 8]` then `2`
D) `[5, 12, 8]` then `5`

````{admonition} Answer:
:class: toggle

**A) `[5, 12, 8]` then `3`**

The loop checks each number: 5 > 4 (yes), 12 > 4 (yes), 3 > 4 (no), 8 > 4 (yes), 1 > 4 (no). Three items pass the filter, so `len(big)` is 3.
````

## Trace 4

```{code-cell} ipython3
:tags: [remove-output]

items = [3, 1, 4, 1, 5]
for i in range(len(items)):
    items[i] = items[i] * 2
print(items)
```

**What is the output?**

A) `[3, 1, 4, 1, 5]`
B) `[6, 2, 8, 2, 10]`
C) `[6, 1, 4, 1, 5]`
D) `Error`

````{admonition} Answer:
:class: toggle

**B) `[6, 2, 8, 2, 10]`**

This uses index-based iteration with `range(len(items))`, which gives indices 0, 1, 2, 3, 4. Each iteration doubles the item at that index *in place* (lists are mutable!). After the loop, every element has been doubled.
````

## Trace 5

```{code-cell} ipython3
:tags: [remove-output]

data = [10, 20, 30]
i = 0
while i < len(data):
    print(data[i])
    i += 2
```

**What is the output?**

A) `10` then `20` then `30`
B) `10` then `30`
C) `10` then `20`
D) `10`

````{admonition} Answer:
:class: toggle

**B) `10` then `30`**

The `while` loop starts with `i = 0` and increments by 2 each time:
- `i = 0`: prints `data[0]` → `10`, then `i` becomes 2
- `i = 2`: prints `data[2]` → `30`, then `i` becomes 4
- `i = 4`: 4 < 3 is `False`, loop ends

So it skips every other item.
````

## Trace 6

```{code-cell} ipython3
:tags: [remove-output]

basket = ["apple", "banana", "cherry"]
target = "banana"
found = False
idx = 0
while not found and idx < len(basket):
    if basket[idx] == target:
        found = True
    else:
        idx += 1
print(idx)
print(found)
```

**What is the output?**

A) `0` then `True`
B) `1` then `True`
C) `2` then `True`
D) `3` then `False`

````{admonition} Answer:
:class: toggle

**B) `1` then `True`**

The loop searches for `"banana"`:
- `idx = 0`: `"apple" == "banana"` is `False`, so `idx` becomes 1
- `idx = 1`: `"banana" == "banana"` is `True`, so `found` becomes `True`
- The `while` condition `not found` is now `False`, so the loop ends

`idx` is 1 (the index where `"banana"` was found) and `found` is `True`.
````
