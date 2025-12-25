import os

BASE = "dp"
os.makedirs(BASE, exist_ok=True)

content = """# Dynamic Programming — Pattern-Based Problem Collection

Here’s the DP list I wish someone had explained properly earlier —
so you don’t waste time like I did.

Dynamic Programming is not about memorizing formulas or solutions.
It’s about learning how to recognize patterns, define the right state,
and transition between states correctly.

This repository is organized to help you do exactly that.

---

## Why this DP list exists

Most people fail at DP because they:
- Solve problems randomly
- Jump into code too early
- Don’t understand why a transition works

This list is curated pattern-first, not difficulty-first.
If you follow it in order, DP starts feeling systematic instead of magical.

---

## How to use this repository

- Pick one folder (one DP pattern) at a time
- For every problem:
  1. Write down the DP state in plain English
  2. Define the transition
  3. Identify base cases
  4. Only then write code

Do not rush to optimize space.
Correctness and clarity matter more.

---

## Patterns covered in this repository

### 1. Linear DP
Problems where the state moves forward one step at a time.

Folder: `1.Linear DP`

---

### 2. Knapsack
Subset selection with constraints.

Folder: `2.Knapsack`

---

### 3. Multi-Dimensional DP
DP with multiple changing parameters.

Folder: `3.Multi Dimensions DP`

---

### 4. Interval DP
DP over ranges.

Folder: `4.Interval DP`

---

### 5. Bitmask DP
DP using bitmasks to compress state.

Folder: `5.bit DP`

---

### 6. Digit DP
DP over digits of a number.

Folder: `6.Digit DP`

---

### 7. DP on Trees
DP combined with DFS.

Folder: `7.DP on Trees`

---

### 8. String DP
DP on strings and substrings.

Folder: `8.String DP`

---

### 9. Probability DP
DP involving probability and expectation.

Folder: `9.Probability DP`

---

### 10. Classic DP Patterns
Foundational DP techniques.

Folder: `10.Classic DPs`

---

### 11. DP + Tricks / Data Structures
DP combined with other techniques.

Folder: `11.DP + Alpha (Tricks/DS)`

---

### 12. Insertion DP
DP involving permutations and ordering constraints.

Folder: `12.Insertion DP`

---

### 13. Graph DP
DP applied on graphs or DAGs.

Folder: `13.Graph DP`

---

### 14. Memoization
Recursive DP with caching.

Folder: `14.Memoization`

---

### 15. Binary Lifting
DP for jumping ancestors or steps.

Folder: `15.Binary Lifting`

---

### 16. Math + DP
DP mixed with mathematical observations.

Folder: `16.Math`

---

## Repository philosophy

- No copied problem statements
- No unnecessary comments
- Focus on thinking, not clutter
- Pattern recognition over memorization

If you understand these patterns,
most DP interview questions become variations — not surprises.
"""

with open(os.path.join(BASE, "README.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("DP README generated successfully (UTF-8).")
