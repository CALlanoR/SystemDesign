# Python Sets
Python set is an unordered collection of multiple items having different datatypes. In Python, sets are mutable, unindexed and do not contain duplicates. The order of elements in a set is not preserved and can change.
- Can store None values.
- Implemented using hash tables internally.
- Do not implement interfaces like Serializable or Cloneable.
- Python sets are not inherently thread-safe; synchronization is needed if used across threads.

## Creating a Set in Python
```python
d = {1, 2, 3, 4, 5}
print(d)
# result:
{1, 2, 3, 4, 5}
```
## Using the set() function

Python Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces, separated by a 'comma'.

```python
set1 = set()
print(set1)

# result:
set()

set1 = set("GeeksForGeeks")
print(set1)

# result:
{'F', 'G', 'e', 'k', 'o', 'r', 's'}

# Creating a Set with the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# result:
{'For', 'Geeks'}

# Creating a Set with the use of a tuple
tup = ("Geeks", "for", "Geeks")
print(set(tup))

# result:
{'Geeks', 'for'}

# Creating a Set with the use of a dictionary
d = {"Geeks": 1, "for": 2, "Geeks": 3}
print(set(d))

# result:
{'Geeks', 'for'}
```

## Unordered, Unindexed and Mutability
In set, the order of elements is not guaranteed to be the same as the order in which they were added. The output could vary each time we run the program. Also the duplicate items entered are removed by itself.

```python
# Unordered
set1 = {3, 1, 4, 1, 5, 9, 2}
print(set1)

# result:
{1, 2, 3, 4, 5, 9} # Output may vary

# Unindexed
my_set = {1, 2, 3}
print(my_set[0])

# result:
TypeError: 'set' object is not subscriptable

# Mutable
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

# result:
{1, 2, 3, 4}

# Add multiple items
set1.update([5, 6])
print(set1)

# result:
{1, 2, 3, 4, 5, 6}
```

## Accessing a Set in Python
We can loop through a set to access set items as set is unindexed and do not support accessing elements by indexing. Also we can use in keyword which is membership operator to check if an item exists in a set.

```python
# Loop through a set
my_set = {1, 2, 3}
for item in my_set:
    print(item)

# result:
1
2
3

# Check if an item exists in a set
my_set = {1, 2, 3}
print(2 in my_set)

# result:
True
```

## Removing Items from a Set
We can remove an element from a set in Python using several methods: remove(), discard() and pop(). Each method works slightly differently:


### Remove or discard
remove() method removes a specified element from the set. If the element is not present in the set, it raises a KeyError. discard() method also removes a specified element from the set. Unlike remove(), if the element is not found, it does not raise an error.

```python
# Remove an item
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)

# result:
{1, 3}

# Remove an item
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)

# result:
{1, 3}

set1 = {1, 2, 3, 4, 5}
# Attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e) 
```

### pop method
pop() method removes and returns an arbitrary element from the set. This means we don't know which element will be removed. If the set is empty, it raises a KeyError.

Note: If the set is unordered then there's no such way to determine which element is popped by using the pop() function. 

```python
my_set = {1, 2, 3}
my_set.pop()
print(my_set)

# result:
{2, 3}
```

# clear method
clear() method removes all elements from the set, leaving it empty.

```python
my_set = {1, 2, 3}
my_set.clear()
print(my_set)

# result:
set()
```

## Frozen Sets in Python
A frozenset in Python is a built-in data type that is similar to a set but with one key difference that is immutability. This means that once a frozenset is created, we cannot modify its elements that is we cannot add, remove or change any items in it. Like regular sets, a frozenset cannot contain duplicate elements.

```python
# Creating a frozenset from a list
fset = frozenset([1, 2, 3, 4, 5])
print(fset)  

# Creating a frozenset from a set
set1 = {3, 1, 4, 1, 5}
fset = frozenset(set1)
print(fset)
```

## Maximum and Minimum element in a Set in Python

```python
# Find the maximum element in a set
my_set = {1, 2, 3, 4, 5}
max_element = max(my_set)
min_element = min(my_set)
print(max_element)
print(min_element)

# result:
5
1
```

## Using sorted() function
The built-in sorted() function in Python can be used to get the maximum or minimum of all the elements in a set. We can use it to sort the set and then access the first and the last element for min and max values.

```python
# Using sorted() function
my_set = {1, 2, 3, 4, 5}
sorted_set = sorted(my_set)
print(sorted_set)

# result:
[1, 2, 3, 4, 5]

print("Minimum element: ", sorted_set[0])
print("Maximum element: ", sorted_set[-1])

# result:
Minimum element:  1
Maximum element:  5
```

## Python Set Operations (Union, Intersection, Difference and Symmetric Difference)

### Union
The union of two sets is a set containing all the elements from both sets. It can be performed using the union() method or the | operator.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using union() method
union_set = set1.union(set2)
print(union_set)

# result:
{1, 2, 3, 4, 5}

# Using | operator
union_set = set1 | set2
print(union_set)

# result:
{1, 2, 3, 4, 5}
```

### Intersection
The intersection of two sets is a set containing only the elements that are common to both sets. It can be performed using the intersection() method or the & operator.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using intersection() method
intersection_set = set1.intersection(set2)
print(intersection_set)

# result:
{3}

# Using & operator
intersection_set = set1 & set2
print(intersection_set)

# result:
{3}
```

### Difference
The difference of two sets is a set containing the elements that are in the first set but not in the second set. It can be performed using the difference() method or the - operator.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using difference() method
difference_set = set1.difference(set2)
print(difference_set)

# result:
{1, 2}

# Using - operator
difference_set = set1 - set2
print(difference_set)

# result:
{1, 2}
```

### Symmetric Difference
The symmetric difference of two sets is a set containing the elements that are in either of the sets, but not in both. It can be performed using the symmetric_difference() method or the ^ operator.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using symmetric_difference() method
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)

# result:
{1, 2, 4, 5}

# Using ^ operator
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)

# result:
{1, 2, 4, 5}
```

### Superset and Subset
A superset is a set that contains all the elements of another set. A subset is a set that is contained within another set.

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Check if set1 is a subset of set2
print(set1.issubset(set2))

# result:
True

# Check if set2 is a superset of set1
print(set2.issuperset(set1))

# result:
True
```

