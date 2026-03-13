# Python Lists
In Python, a list is a built-in data structure that can hold an ordered collection of items. Unlike arrays in some languages, Python lists are very flexible:

- Can contain duplicate items
- Mutable: items can be modified, replaced, or removed
- Ordered: maintains the order in which items are added
- Index-based: items are accessed using their position (starting from 0)
- Can store mixed data types (integers, strings, booleans, even other lists)

## Creating a List
Lists can be created in several ways, such as using square brackets, the list() constructor or by repeating elements. Let's look at each method one by one with example:

1. Using Square Brackets

```python
a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types

print(a)
print(b)
print(c)
# result:
[1, 2, 3, 4, 5]
['apple', 'banana', 'cherry']
[1, 'hello', 3.14, True]
```

2. Using list() constructor

```python
a = list((1, 2, 3, 4, 5)) # List from tuple
b = list(['apple', 'banana', 'cherry']) # List from list
c = list('hello') # List from string

print(a)
print(b)
print(c)
# result:
[1, 2, 3, 4, 5]
['apple', 'banana', 'cherry']
['h', 'e', 'l', 'l', 'o']
```

## 3. Creating List with Repeated Elements
We can use the multiplication operator * to create a list with repeated items.

```python
a = [1, 2, 3] * 3 # List with repeated elements
print(a)
# result:
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## Accessing List Elements

Elements in a list are accessed using indexing. Python indexes start at 0, so a[0] gives the first element. Negative indexes allow access from the end (e.g., -1 gives the last element).

```python
a = [1, 2, 3, 4, 5]
print(a[0]) # First element
print(a[2]) # Third element
print(a[-1]) # Last element
print(a[-3]) # Third element from the end
# result:
1
3
5
3
```

## List Slicing
List slicing allows you to extract a portion of a list by specifying the start and end indices.

```python
a = [1, 2, 3, 4, 5]
print(a[1:3]) # Elements from index 1 to 2
print(a[:3]) # Elements from the beginning to index 0
print(a[3:]) # Elements from index 3 to the end
print(a[::-1]) # Reverse the list
# result:
[2, 3]
[1, 2, 3]
[4, 5]
[5, 4, 3, 2, 1]
```

## Modifying List Elements
Since lists are mutable, you can modify their elements after creation.

```python
a = [1, 2, 3, 4, 5]
a[0] = 10 # Modify the first element
a[2] = 30 # Modify the third element
print(a)
# result:
[10, 2, 30, 4, 5]
```

## Adding Elements to a List
There are several ways to add elements to a list:

1. Using append() method

```python
a = [1, 2, 3]
a.append(4) # Add element to the end
print(a)
# result:
[1, 2, 3, 4]
```

2. Using insert() method

```python
a = [1, 2, 3]
a.insert(1, 10) # Insert element at specific position
print(a)
# result:
[1, 10, 2, 3]
```

3. Using extend() method

```python
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b) # Add elements from another list
print(a)
# result:
[1, 2, 3, 4, 5, 6]
```

4. Using concatenation

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b # Concatenate lists
print(c)
# result:
[1, 2, 3, 4, 5, 6]
```

## Removing Elements from a List
There are several ways to remove elements from a list:

1. Using remove() method

```python
a = [1, 2, 3, 4, 5]
a.remove(3) # Remove specific element
print(a)
# result:
[1, 2, 4, 5]
```

2. Using pop() method

```python
a = [1, 2, 3, 4, 5]
a.pop() # Remove last element
print(a)
a.pop(1) # Remove element at specific position
print(a)
# result:
[1, 2, 3, 4]
[1, 3, 4]
```

3. Using del keyword

```python
a = [1, 2, 3, 4, 5]
del a[2] # Delete element at specific position
print(a)
del a # Delete the entire list
# result:
[1, 2, 4, 5]
```

4. Using clear() method

```python
a = [1, 2, 3, 4, 5]
a.clear() # Remove all elements
print(a)
# result:
[]
```

## Iterating Over Lists
We can iterate over lists using loops, which is useful for performing actions on each item.

```python
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)
# result:
1
2
3
4
5
```

## Nested Lists
A nested list is a list within another list, which is useful for representing matrices or tables. We can access nested elements by chaining indexes.

```python
a = [1, 2, [3, 4, 5], 6, 7]
print(a[2]) # Access nested list
print(a[2][1]) # Access element in nested list
# result:
[3, 4, 5]
4
```

```python
matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[1][2])
# result:
6
```

## Common List Operations

| Operation | Description |
| --- | --- |
| `len(list)` | Returns the number of elements in the list. |
| `sum(list)` | Returns the sum of all elements in the list. |
| `max(list)` | Returns the largest element in the list. |
| `min(list)` | Returns the smallest element in the list. |
| `list.count(element)` | Returns the number of occurrences of an element. |
| `list.index(element)` | Returns the index of the first occurrence of an element. |
| `list.sort()` | Sorts the list in ascending order. |
| `list.reverse()` | Reverses the order of elements in the list. |
| `list.copy()` | Returns a shallow copy of the list. |
| `list.clear()` | Removes all elements from the list. |

