# Lab Assignment 3: Python Functions

**Course:** School of Computer Engineering and Technology  
**Assignment No:** 3  

## Problem Statement
To check whether or not the triangle is a right-angled triangle using function.

## Aim
Write a Python program that accepts the length of three sides of a triangle as inputs. The program should indicate whether or not the triangle is a right-angled triangle using function.

## Objectives
* To learn and implement Function.

## Theory

### 1. System defined function and User defined functions
* **System-defined functions:** These are built-in functions provided globally by the Python interpreter (e.g., `print()`, `input()`, `len()`, `sorted()`). They are always available for use without any external definition.
* **User-defined functions:** These are custom blocks of code created by programmers to fulfill specific tasks. They help decompose large codebases into modular, manageable chunks.

### 2. def keyword with following terms
* **Function Declaration / Definition:** The syntax using the `def` keyword followed by the function name and parenthesized parameters, which specifies what the function does (e.g., `def is_right_triangle(a, b, c):`).
* **Function Calling:** Invoking or executing the defined function block from another part of the script by passing required arguments (e.g., `is_right_triangle(3, 4, 5)`).

## Platform
Windows/Ubuntu - Python Editor (Jupyter Notebook, IDLE, or any IDE).

## Algorithm/Pseudo code
1. Start the program.
2. Define a function named `check_right_angle` that accepts three numeric parameters representing sides of a triangle.
3. Inside the function, identify the largest side to treat it as the hypotenuse.
4. Calculate the sum of squares of the two smaller sides.
5. Check if the square of the largest side matches this sum (`hypotenuse^2 == side1^2 + side2^2`).
6. Return `True` if equal, otherwise return `False`.
7. In the main block, take three side lengths as input from the user.
8. Call `check_right_angle` using these inputs.
9. Display whether the triangle is right-angled based on the function's return value.
10. End the program.

## Input
```text
Enter the length of the first side: 3
Enter the length of the second side: 4
Enter the length of the third side: 5
```
## Output
```text
The given sides form a right-angled triangle.
```
## Conclusion
Studied python function.

## FAQs

### 1. What is a Function in Python Programming?
A function is a self-contained block of reusable code designed to perform a single, specific task. Functions provide better modularity for your application, make code easier to read, and eliminate redundancy by allowing you to execute the same logic multiple times without rewriting it.

### 2. Is it Mandatory for a Python Function to Return a Value?
No, it is not mandatory. If a Python function does not contain an explicit `return` statement, or if it executes a bare `return` without an accompanying value, it automatically and implicitly returns `None` to the caller.

### 3. Name some standard Python errors?
* **`SyntaxError`:** Raised when the parser encounters a line of code that violates Python's grammatical rules.
* **`TypeError`:** Occurs when an operation or function is applied to an object of an inappropriate data type.
* **`ValueError`:** Triggered when a function receives an argument of the correct type but an invalid or inappropriate value.
* **`IndexError`:** Raised when attempting to access a sequence (like a list or tuple) using an index that is out of its valid range.
* **`KeyError`:** Occurs when looking up a specific key in a dictionary that does not exist.
