content = """# Data Structures & Algorithms

This repository contains a curated collection of LeetCode problems
organized to build strong problem-solving fundamentals.

The focus is on learning patterns instead of solving problems randomly.

---

## Structure

- `dp/`
  - Dynamic Programming problems grouped by pattern

- `pattern_problems/`
  - Core interview problems grouped by technique

---

## Language

- C++/Java
- Clean and interview-ready
- No copied problem statements

---

## Goal

To improve consistency, pattern recognition, and interview preparation.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Simple README generated successfully.")
