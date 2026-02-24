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


# Ejemplo2 
# Sintax:
# newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


# Ejemplo 3
newlist = [x for x in range(10) if x < 5] 
print(newlist)

# Ejemplo 4
newlist = [x.upper() for x in fruits]
print(newlist)

# Ejemplo 5
newlist1 = [x if x != "banana" else "orange" for x in fruits]
print(newlist1)

# Ejemplo 6 (crear una lista con rango)
a = [i for i in range(10)]
print(a)

# Ejemplo 7 Using nested loops
c = [(x, y) for x in range(3) for y in range(3)]
print(c)

# Ejemplo 8 Flattening a list of lists
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)