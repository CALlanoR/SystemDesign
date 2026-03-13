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

Examples of list comprehension:

1. Creating a list from a range
```python
a = [i for i in range(10)]
print(a)
# result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

2. Using nested loops
```python
c = [(x, y) for x in range(3) for y in range(3)]
print(c)
# result: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

3. Flattening a list of lists
```python
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)
# result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

4. Conditional filtering
```python
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)
# result: [2,4]
```

```python
# Sintaxis: [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# result: ['apple', 'banana', 'cherry', 'kiwi', 'mango']
```

```python
newlist = [x for x in range(10) if x < 5] 
print(newlist)
# result: [0, 1, 2, 3, 4]
```

5. Element transformation
```python
newlist = [x.upper() for x in fruits]
print(newlist)
# result: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
```

```python
symbols = "$#@&*"
codes = [ord(symbol) for symbol in symbols]
print(codes)
# result: [36, 35, 64, 38, 42]
```

6. Conditional if-else
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x if x != "banana" else "orange" for x in fruits]
print(newlist1)
# result: ['apple', 'orange', 'cherry', 'kiwi', 'mango']
```



