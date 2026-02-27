# Python Tuples
A tuple in Python is an immutable ordered collection of elements.
- Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
- Tuples can hold elements of different data types.
- The main characteristics of tuples are being ordered, heterogeneous and immutable.

## Creating a Tuple
A tuple is created by placing all the items inside parentheses (), separated by commas. A tuple can have any number of items and they can be of different data types.

```python
a = (1, 2, 3, 4, 5) # Tuple of integers
b = ('apple', 'banana', 'cherry') # Tuple of strings
c = (1, 'hello', 3.14, True) # Mixed data types

print(a)
print(b)
print(c)
# result:
(1, 2, 3, 4, 5)
('apple', 'banana', 'cherry')
(1, 'hello', 3.14, True)
```

## Creating a Tuple with Mixed Datatypes
Tuples can contain elements of various data types, including other tuples, lists, dictionaries and even functions.

```python
a = (1, 'hello', 3.14, True, [1, 2, 3], {'a': 1, 'b': 2}, (4, 5, 6))
print(a)
# result:
(1, 'hello', 3.14, True, [1, 2, 3], {'a': 1, 'b': 2}, (4, 5, 6))
```

### Creating a Tuple with nested tuples
```python
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)
# result:
(0, 1, 2, 3, ('python', 'geek'))
```

### Creating a Tuple with repetition
```python
tup1 = ('Geeks',) * 3
print(tup1) 
# result:
('Geeks', 'Geeks', 'Geeks')
```

### Creating a Tuple with the use of loop
```python
tup = ('Geeks')
for i in range(5):
    tup = (tup,)
    print(tup)
# result:
('Geeks',)
('Geeks', 'Geeks')
('Geeks', 'Geeks', 'Geeks')
('Geeks', 'Geeks', 'Geeks', 'Geeks')
('Geeks', 'Geeks', 'Geeks', 'Geeks', 'Geeks')
```

## Accessing of Tuples
We can access the elements of a tuple by using indexing and slicing, similar to how we access elements in a list. Indexing starts at 0 for the first element and goes up to n-1, where n is the number of elements in the tuple. Negative indexing starts from -1 for the last element and goes backward.

```python
a = (1, 2, 3, 4, 5)
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

## Tuple Slicing
Tuple slicing allows you to extract a portion of a tuple by specifying the start and end indices.

```python
a = (1, 2, 3, 4, 5)
print(a[1:3]) # Elements from index 1 to 2
print(a[:3]) # Elements from the beginning to index 0
print(a[3:]) # Elements from index 3 to the end
print(a[::-1]) # Reverse the tuple
# result:
(2, 3)
(1, 2, 3)
(4, 5)
(5, 4, 3, 2, 1)
```

## Tuple Concatenation
Tuple concatenation allows you to combine two or more tuples into a new tuple.

```python
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b # Concatenate tuples
print(c)
# result:
(1, 2, 3, 4, 5, 6)
```

## Deleting a Tuple
Since tuples are immutable, we cannot delete individual elements of a tuple. However, we can delete an entire tuple using del statement.

```python
a = (1, 2, 3, 4, 5)
del a # Delete the entire tuple
print(a)
# result:
NameError: name 'a' is not defined
```

## Tuple Unpacking with Asterisk (*)
In Python, the " * " operator can be used in tuple unpacking to grab multiple items into a list. This is useful when you want to extract just a few specific elements and collect the rest together.

```python
a = (1, 2, 3, 4, 5)
first, *middle, last = a
print(first)
print(middle)
print(last)
# result:
1
[2, 3, 4]
5
```