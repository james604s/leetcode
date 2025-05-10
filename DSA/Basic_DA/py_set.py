"""
Description: A set is an unordered collection of unique elements. 
  Sets are helpful for membership testing, removing duplicates from a sequence, 
  and performing mathematical set operations like union, intersection, and difference.

Time Complexity:
Read: O(1) - Checking if an element is in the set (e.g., 4 in my_set) is O(1) on average.
Write:
- Adding/Removing: O(1) - Adding or removing an element is O(1) on average.
- Set Operations:
- - Union: O(len(set1) + len(set2)) - Combining two sets into one.
- - Intersection: O(min(len(set1), len(set2))) - Finding common elements between two sets.
- - Difference: O(len(set1)) - Finding elements in one set but not another.
"""

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Adding an element
my_set.add(6)  # my_set = {1, 2, 3, 4, 5, 6}
print(my_set)

# Removing an element
my_set.remove(3)  # my_set = {1, 2, 4, 5, 6}
print(my_set)

# Checking membership
is_in_set = 4 in my_set  # is_in_set = True
print(is_in_set)

# Set operations: union, intersection, difference
other_set = {4, 5, 6, 7, 8}
print(other_set)

union_set = my_set.union(other_set)  # union_set = {1, 2, 4, 5, 6, 7, 8}
print(union_set)

intersection_set = my_set.intersection(other_set)  # intersection_set = {4, 5, 6}
print(intersection_set)

difference_set = my_set.difference(other_set)  # difference_set = {1, 2}
print(difference_set)

print(f' Here is my_set {my_set} and other_set {other_set}')
print(f' Here is union_set {union_set}')
print(f' Here is intersection_set {intersection_set}')
print(f' Here is difference_set {difference_set}')


