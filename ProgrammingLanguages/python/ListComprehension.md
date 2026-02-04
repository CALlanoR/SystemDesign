# List Comprehension
List comprehension is a concise and powerful way to create new lists by applying an expression to each item in an existing iterable (like a list, tuple or range). It helps you write clean, readable and efficient code compared to traditional loops.

Example: 
```python
a = [2,3,4,5]
res = [val ** 2 for val in a]
print(res)

result: [4,9,16,25]
```

## Why Use List Comprehension?
- Cleaner code: Combines looping, filtering and transformation in one line.
- More readable: Avoids verbose loops and temporary variables.
- Faster execution: Often faster than equivalent for-loops.

## Conditional Statements in List Comprehension
List comprehensions can use conditions to select or transform items based on specific rules. This allows creating customized lists more concisely and improves code readability and efficiency.

Example:

```python
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)

result: [2,4]
```